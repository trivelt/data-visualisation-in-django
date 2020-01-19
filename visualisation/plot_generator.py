from bokeh.plotting import figure
from bokeh.models import Range1d, LinearAxis
from bokeh.embed import components


class PlotGenerator:
    def __init__(self, x, y_clicks, y_impressions):
        self.x = x
        self.y_clicks = y_clicks
        self.y_impressions = y_impressions

    def generate(self):
        self._create_plot_figure()
        self._create_vertical_axis()
        self._set_toolbar_location()
        self._draw_lines()
        script, div = components(self.plot)
        return script, div

    def _create_plot_figure(self):
        self.plot = figure(
            title="Line Graph",
            x_axis_label="Date",
            x_axis_type='datetime',
            plot_width=1200,
            plot_height=400
        )

    def _create_vertical_axis(self):
        self.plot.yaxis.axis_label = 'Clicks'
        max_clicks_value = max(self.y_clicks) if self.y_clicks else 0
        self.plot.y_range = Range1d(start=0, end=max_clicks_value)

        max_impressions_value = max(self.y_impressions) if self.y_impressions else 0
        self.plot.extra_y_ranges['impressions'] = Range1d(start=0, end=max_impressions_value)
        self.plot.add_layout(LinearAxis(y_range_name='impressions', axis_label='Impressions'), 'right')

    def _set_toolbar_location(self):
        self.plot.toolbar_location = 'above'

    def _draw_lines(self):
        self.plot.line(
            x=self.x,
            y=self.y_clicks,
            legend_label='Clicks',
            color='red'
        )

        self.plot.line(
            x=self.x,
            y=self.y_impressions,
            legend_label='Impressions',
            y_range_name='impressions',
            color='blue'
        )
