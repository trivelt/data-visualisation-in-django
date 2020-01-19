from unittest import TestCase
from visualisation.data_transformer import DataTransformer


class TestDataTransformer(TestCase):
    def test_transform_should_convert_date_format(self):
        data = ("05.10.2020", '', '', '', '')
        transformed_data = DataTransformer(data).transform()
        self.assertEqual(transformed_data['date'], "2020-10-05")

    def test_transform_should_return_number_of_impressions_when_not_empty(self):
        number_of_impressions = 100
        data = ("05.10.2020", '', '', '', number_of_impressions)
        transformed_data = DataTransformer(data).transform()
        self.assertEqual(transformed_data['impressions'], number_of_impressions)

    def test_transform_should_return_zero_clicks_when_emty(self):
        data = ("05.10.2020", '', '', '', '')
        transformed_data = DataTransformer(data).transform()
        self.assertEqual(transformed_data['impressions'], 0)

    def test_transform_should_convert_data_list_into_dict(self):
        data = ("05.10.2020", 'Likes Campaign #1', 'Facebook Ads', '50', '150')
        date, data_source, name, clicks, impressions = data
        expected_date = '2020-10-05'

        transformed_data = DataTransformer(data).transform()

        self.assertDictEqual(transformed_data, {
            'date': expected_date,
            'name': name,
            'data_source': data_source,
            'clicks': clicks,
            'impressions': impressions
        })
