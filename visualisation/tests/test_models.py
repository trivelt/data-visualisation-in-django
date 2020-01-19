from django.test import TestCase
from visualisation.models import Campaign


class TestMetricsGroupedByDateManager(TestCase):
    def setUp(self):
        Campaign.objects.create(date='2019-10-15', name='Test', data_source='TestSource', clicks=20, impressions=50)
        Campaign.objects.create(date='2019-10-15', name='Bar', data_source='BarSource', clicks=30, impressions=40)
        Campaign.objects.create(date='2019-10-18', name='Foo', data_source='TestSource', clicks=45, impressions=100)
        Campaign.objects.create(date='2019-10-18', name='Test', data_source='TestSource', clicks=60, impressions=80)

    def test_all_should_return_all_metrics_grouped_by_date(self):
        grouped_metrics = Campaign.metrics_grouped_by_date.all()
        self.assertListEqual(list(grouped_metrics.values_list('total_clicks', flat=True)), [50, 105])
        self.assertListEqual(list(grouped_metrics.values_list('total_impressions', flat=True)), [90, 180])

    def test_filter_by_source_and_campaign_should_return_filtered_metrics_grouped_by_date(self):
        grouped_metrics = Campaign.metrics_grouped_by_date.filter_by_source_and_campaign(data_sources=["TestSource"],
                                                                                         campaigns=['Test'])
        self.assertListEqual(list(grouped_metrics.values_list('total_clicks', flat=True)), [20, 60])
