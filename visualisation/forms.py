from django import forms
from easy_select2 import Select2Multiple
from visualisation.models import Campaign


class DataFilterForm(forms.Form):
    campaigns = forms.MultipleChoiceField(choices=[], widget=Select2Multiple, required=False)
    data_sources = forms.MultipleChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        self.distinct_data_sources = Campaign.get_distinct_data_sources()
        self.distinct_data_sources = list(enumerate(self.distinct_data_sources))

        self.campaigns_list = Campaign.get_distinct_campaigns()
        self.campaigns_list.insert(0, "All")
        self.campaigns_list = [(str(index), item) for index, item in enumerate(self.campaigns_list)]

        self.fields['campaigns'].choices = self.campaigns_list
        self.fields['data_sources'].choices = self.distinct_data_sources

    def selected_campaigns(self):
        if not self.is_valid():
            return []
        campaigns = [self.campaigns_list[int(index)][1] for index in self.cleaned_data['campaigns']]
        return [] if "All" in campaigns else campaigns

    def selected_data_sources(self):
        if not self.is_valid():
            return []
        return [self.distinct_data_sources[int(index)][1] for index in self.cleaned_data['data_sources']]
