from django.shortcuts import render
from django.db.models import Sum

from visualisation.models import Campaign
from visualisation.forms import DataFilterForm
from visualisation.plot_generator import PlotGenerator


def index(request):
    clicks_grouped_by_date = Campaign.objects.values('date').order_by('date').annotate(total_clicks=Sum('clicks'))
    impressions_grouped_by_date = Campaign.objects.values('date').order_by('date').annotate(total_impressions=Sum('impressions'))

    x = clicks_grouped_by_date.values_list('date', flat=True)
    y_clicks = clicks_grouped_by_date.values_list('total_clicks', flat=True)
    y_impressions = impressions_grouped_by_date.values_list('total_impressions', flat=True)

    form = DataFilterForm()
    plot_script, plot_div = PlotGenerator(x, y_clicks, y_impressions).generate()
    return render(request, 'visualisation/base.html', {'script': plot_script, 'div': plot_div, 'form': form})
