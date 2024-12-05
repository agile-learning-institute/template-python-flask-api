import unittest
import os
from src.config.config import config

class TestConfigEnvironment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Class-level setup: Initialize configuration items"""
        cls.config_items = [
            "BUILT_AT", "CONFIG_FOLDER", "VERSION_COLLECTION", "ENUMERATORS_COLLECTION"
            # TODO Other CI's
        ]
        
    def setUp(self):
        """Re-initialize the config for each test."""
        # Set all environment variables to "ENV_VALUE"
        os.environ["PORT"] = "9999"
        for var in self.config_items:
            os.environ[var] = "ENV_VALUE"

        # Initialize the Config object
        config.initialize()
        
        # Reset environment variables 
        if os.environ["PORT"]:
            del os.environ["PORT"]
        for var in self.config_items:
            if os.environ[var]:
                del os.environ[var]

    def test_environment_properties_in_getters(self):
        self.assertEqual(config.get_config_folder(), "ENV_VALUE")
        self.assertEqual(config.get_port(), 9999)
        self.assertEqual(config.get_version_collection_name(), "ENV_VALUE")
        self.assertEqual(config.get_enumerators_collection_name(), "ENV_VALUE")
        # TODO Other Properties

    def test_environment_config_items(self):
        self._test_config_environment_value("BUILT_AT")
        self._test_config_environment_value("CONFIG_FOLDER")
        self._test_config_environment_value("VERSION_COLLECTION")
        self._test_config_environment_value("ENUMERATORS_COLLECTION")
        # TODO More Tests

    def _test_config_environment_value(self, config_name):
        """Helper function to check environment values."""
        items = config.config_items
        item = next((i for i in items if i['name'] == config_name), None)
        self.assertIsNotNone(item)
        self.assertEqual(item['name'], config_name)
        self.assertEqual(item['from'], "environment")
        self.assertEqual(item['value'], "ENV_VALUE")

if __name__ == '__main__':
    unittest.main()