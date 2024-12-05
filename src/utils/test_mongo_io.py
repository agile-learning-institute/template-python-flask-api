from copy import deepcopy
from datetime import datetime, timezone
import unittest

from bson import ObjectId
from src.config.config import config
from src.utils.mongo_io import MongoIO

class TestMongoIO(unittest.TestCase):
    
    def setUp(self):
        # Test Data - Matches test data from database
        # TODO Setup Test Data

        MongoIO._instance = None
        mongo_io = MongoIO.get_instance()
        mongo_io.initialize()

    def tearDown(self):
        mongo_io = MongoIO.get_instance()
        mongo_io.delete_COLLECTION("TEST_ID")
        mongo_io.disconnect()
    
    def test_singleton_behavior(self):
        # Test that MongoIO is a singleton
        mongo_io1 = MongoIO.get_instance()
        mongo_io2 = MongoIO.get_instance()
        self.assertIs(mongo_io1, mongo_io2, "MongoIO should be a singleton")

    def test_config_loaded(self):
        # Test that MongoIO is a singleton
        self.assertIsInstance(config.versions, list)
        self.assertEqual(len(config.versions), 11)

        self.assertIsInstance(config.enumerators, dict)

    # TODO Write more tests
        
