from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class DataTransformer:
    def __init__(self, data):
        self.data = data
        self.transformed_valid_data = True

    def transform(self):
        try:
            date, date_source, name, clicks, impressions = self.data

            date = self._convert_date_format(date)
            impressions = self._set_default_number_as_zero(impressions)

            return {
                'date': date,
                'name': name,
                'data_source': date_source,
                'clicks': clicks,
                'impressions': impressions
            }
        except Exception as exc:
            logger.warning("Ommiting invalid row %s: %s", self.data, exc)
            self.transformed_valid_data = False
            return None

    def _convert_date_format(self, date_string):
        date = datetime.strptime(date_string, '%d.%m.%Y')
        return date.strftime('%Y-%m-%d')

    def _set_default_number_as_zero(self, value):
        return value if value else 0
