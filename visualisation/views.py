from django.shortcuts import render

from visualisation.models import Campaign
from visualisation.forms import DataFilterForm
from visualisation.plot_generator import PlotGenerator


def index(request):
    if request.method == "POST":
        form = DataFilterForm(request.POST)
    else:
        form = DataFilterForm()

    metrics_grouped_by_date = _get_filtered_metrics(form)
    x = metrics_grouped_by_date.values_list('date', flat=True)
    y_clicks = metrics_grouped_by_date.values_list('total_clicks', flat=True)
    y_impressions = metrics_grouped_by_date.values_list('total_impressions', flat=True)

    plot_script, plot_div = PlotGenerator(x, y_clicks, y_impressions).generate()
    return render(request, 'visualisation/base.html', {'script': plot_script, 'div': plot_div, 'form': form})


def _get_filtered_metrics(form):
    if form.is_valid():
        return Campaign.metrics_grouped_by_date.filter_by_source_and_campaign(
            data_sources=form.selected_data_sources(),
            campaigns=form.selected_campaigns()
        )
    else:
        return Campaign.metrics_grouped_by_date.all()
