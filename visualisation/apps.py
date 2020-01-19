from django.apps import AppConfig
from django.conf import settings


class VisualisationConfig(AppConfig):
    name = 'visualisation'

    def ready(self):
        if settings.CSV_DATA_FILE:
            from .data_loader import DataLoader
            data_loader = DataLoader(csv_file_name=settings.CSV_DATA_FILE)
            data_loader.load()
