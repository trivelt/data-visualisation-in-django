from django import forms
from easy_select2 import Select2Multiple
from visualisation.models import Campaign


class DataFilterForm(forms.Form):
    distinct_data_sources = Campaign.get_distinct_data_sources()
    distinct_data_sources = list(enumerate(distinct_data_sources))

    campaigns_list = Campaign.get_distinct_campaigns()
    campaigns_list.insert(0, "All")
    campaigns_list = [(str(index), item) for index, item in enumerate(campaigns_list)]

    campaigns = forms.MultipleChoiceField(choices=campaigns_list, widget=Select2Multiple, required=False)
    data_sources = forms.MultipleChoiceField(choices=distinct_data_sources, required=False)

    def selected_campaigns(self):
        if not self.is_valid():
            return []
        campaigns = [self.campaigns_list[int(index)][1] for index in self.cleaned_data['campaigns']]
        return [] if "All" in campaigns else campaigns

    def selected_data_sources(self):
        if not self.is_valid():
            return []
        return [self.distinct_data_sources[int(index)][1] for index in self.cleaned_data['data_sources']]
