import copy
from datetime import datetime, timezone
import unittest
from unittest.mock import patch

from bson import ObjectId
from src.services.COLLECTION_services import COLLECTIONService
from src.utils.mongo_io import MongoIO

class TestCOLLECTIONService(unittest.TestCase):
    
    def setUp(self):    
        self.maxDiff = None

        # Setup Test Data
        token = {}
        # TODO token for RBAC testing
        # TODO Additional test data as needed
        
    @patch('src.services.COLLECTION_services.MongoIO')
    def test_create_COLLECTION_success(self, mock_mongo_io):
        # Mock the MongoIO methods
        mock_instance = mock_mongo_io.return_value
        mock_instance.get_COLLECTION.return_value = self.test_COLLECTION_one
        mock_instance.get_mentor.return_value = "TEST_ID"

        COLLECTION = COLLECTIONService.get_or_create_COLLECTION("TEST_ID", self.token, self.breadcrumb)
        mock_instance.get_COLLECTION.assert_called_once_with("TEST_ID")
        self.assertEqual(COLLECTION, self.test_COLLECTION_one)
        mock_instance.reset_mock()

    # TODO Write more tests

if __name__ == '__main__':
    unittest.main()