from django.db import models


class Campaign(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=300)
    data_source = models.CharField(max_length=200)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
