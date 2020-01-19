from django import forms
from visualisation.models import Campaign
from easy_select2 import Select2Multiple


class DataFilterForm(forms.Form):
    distinct_data_sources = Campaign.objects.all().values_list("data_source").distinct()
    distinct_data_sources = [item[0] for item in list(distinct_data_sources)]
    distinct_data_sources = list(enumerate(distinct_data_sources))

    campaigns_list = Campaign.objects.all().values_list("name").distinct()
    campaigns_list = [item[0] for item in list(campaigns_list)]
    campaigns_list.insert(0, "All")
    campaigns_list = [(str(index), item) for index, item in enumerate(campaigns_list)]

    campaigns = forms.MultipleChoiceField(choices=campaigns_list, widget=Select2Multiple)

    data_sources = forms.MultipleChoiceField(choices=distinct_data_sources)
