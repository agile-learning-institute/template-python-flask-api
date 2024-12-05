import unittest
import os
from src.config.config import config

class TestConfigFiles(unittest.TestCase):

    def setUp(self):
        """Re-initialize the config for each test."""
        # Set Config Folder location
        os.environ["CONFIG_FOLDER"] = "./test/resources/configTest"

        # Initialize the Config object
        config.initialize()
        
        # Reset config folder location 
        del os.environ["CONFIG_FOLDER"]

    def test_file_properties_in_getters(self):
        self.assertEqual(config.get_port(), 9999)
        self.assertEqual(config.get_version_collection_name(), "TEST_VALUE")
        self.assertEqual(config.get_enumerators_collection_name(), "TEST_VALUE")
        # TODO Additional properties

    def test_file_config_items(self):
        self._test_config_file_value("DB_NAME")
        self._test_config_file_value("VERSION_COLLECTION")
        self._test_config_file_value("ENUMERATORS_COLLECTION")
        # TODO Additional properties

    def _test_config_file_value(self, config_name):
        """Helper function to check file values."""
        items = config.config_items
        item = next((i for i in items if i['name'] == config_name), None)
        self.assertIsNotNone(item)
        self.assertEqual(item['name'], config_name)
        self.assertEqual(item['from'], "file")
        self.assertEqual(item['value'], "TEST_VALUE")

if __name__ == '__main__':
    unittest.main()