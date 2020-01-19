from django.db import models
from django.db.models import Sum


class MetricsGroupedByDateManager(models.Manager):
    grouping_field = None

    def get_queryset(self):
        return super().get_queryset().values('date').order_by('date').annotate(
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks')
        )

    def filter_by_source_and_campaign(self, data_sources, campaigns):
        data_sources = data_sources if data_sources else Campaign.get_distinct_data_sources()
        campaigns = campaigns if campaigns else Campaign.get_distinct_campaigns()

        return super().get_queryset().values('date').filter(
            data_source__in=data_sources,
            name__in=campaigns
        ).order_by('date').annotate(
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks')
        )


class Campaign(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=300)
    data_source = models.CharField(max_length=200)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

    objects = models.Manager()
    metrics_grouped_by_date = MetricsGroupedByDateManager()

    @staticmethod
    def get_distinct_data_sources():
        distinct_data_sources = Campaign.objects.all().values_list("data_source").distinct()
        return [item[0] for item in list(distinct_data_sources)]

    @staticmethod
    def get_distinct_campaigns():
        campaigns_list = Campaign.objects.all().values_list("name").distinct()
        return [item[0] for item in list(campaigns_list)]
