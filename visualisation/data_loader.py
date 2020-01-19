import csv
from django.db import transaction
from visualisation.models import Campaign

from visualisation.data_transformer import DataTransformer


class DataLoader:
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def load(self):
        self._remove_old_data()
        self._load_new_data()

    def _remove_old_data(self):
        Campaign.objects.all().delete()

    def _load_new_data(self):
        self.to_add = []
        with open(self.csv_file_name, 'r') as csv_file:
            data_reader = csv.reader(csv_file)
            self._skip_header(data_reader)
            for row in data_reader:
                self._load_row(row)
        Campaign.objects.bulk_create(self.to_add)
        self.to_add.clear()

    def _skip_header(self, reader):
        next(reader)

    def _load_row(self, row):
        data_transformer = DataTransformer(row)
        data = data_transformer.transform()
        if not data_transformer.transformed_valid_data:
            return

        self._add_to_database(data)

    def _add_to_database(self, data):
        new_campaign = Campaign(
            date=data['date'],
            data_source=data['data_source'],
            name=data['name'],
            clicks=data['clicks'],
            impressions=data['impressions']
        )
        self.to_add.append(new_campaign)
