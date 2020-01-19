from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.models import Range1d, LinearAxis
from bokeh.embed import components
from django.db.models import Sum

from visualisation.models import Campaign
from visualisation.forms import DataFilterForm


def index(request):
    clicks_grouped_by_date = Campaign.objects.values('date').order_by('date').annotate(total_clicks=Sum('clicks'))
    impressions_grouped_by_date = Campaign.objects.values('date').order_by('date').annotate(total_impressions=Sum('impressions'))

    x = clicks_grouped_by_date.values_list('date', flat=True)
    y_clicks = clicks_grouped_by_date.values_list('total_clicks', flat=True)
    y_impressions = impressions_grouped_by_date.values_list('total_impressions', flat=True)

    plot= figure(
        title="Line Graph",
        x_axis_label="Date",
        x_axis_type='datetime',
        plot_width=1200,
        plot_height=400
    )

    plot.yaxis.axis_label = 'Clicks'
    plot.y_range = Range1d(start=0, end=max(y_clicks))

    plot.extra_y_ranges['impressions'] = Range1d(start=0, end=max(y_impressions))
    plot.add_layout(LinearAxis(y_range_name='impressions', axis_label='Impressions'), 'right')

    plot.line(
        x=x,
        y=y_clicks,
        legend='Clicks',
        color='red'
    )

    plot.line(
        x=x,
        y=y_impressions,
        legend='Impressions',
        y_range_name='impressions',
        color='blue'
    )

    plot.toolbar_location = 'above'

    script, div = components(plot)
    form = DataFilterForm()
    return render(request, 'visualisation/base.html', {'script': script, 'div': div, 'form': form})
