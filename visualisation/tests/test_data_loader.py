from unittest import TestCase
from unittest.mock import MagicMock, patch
from visualisation.data_loader import DataLoader


class TestDataLoader(TestCase):
    def setUp(self):
        self.data_loader = DataLoader("file.csv")

    def test_load_should_load_new_data_replacing_old_ones(self):
        self.data_loader._remove_old_data = MagicMock()
        self.data_loader._load_new_data = MagicMock()

        self.data_loader.load()

        self.data_loader._remove_old_data.assert_called_once()
        self.data_loader._load_new_data.assert_called_once()

    @patch('visualisation.data_loader.Campaign')
    def test_remove_old_data_should_clear_all_campaign_objects(self, campaign):
        self.data_loader._remove_old_data()
        campaign.objects.all.return_value.delete.assert_called_once()
