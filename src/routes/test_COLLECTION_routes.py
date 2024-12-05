import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from src.routes.COLLECTION_routes import create_COLLECTION_routes
from src.utils.ejson_encoder import MongoJSONEncoder

class TestCOLLECTIONRoutes(unittest.TestCase):

    def setUp(self):
        # Test Data
        self.sample_COLLECTION = {"TODO - Define Sample Data"}
        
        # Set up the Flask test app and register the blueprint
        self.app = Flask(__name__)
        self.app.json = MongoJSONEncoder(self.app)        
        COLLECTION_routes = create_COLLECTION_routes()
        self.app.register_blueprint(COLLECTION_routes, url_prefix='/api/COLLECTION')
        self.client = self.app.test_client()

    @patch('src.routes.COLLECTION_routes.COLLECTIONService.create_COLLECTION')
    def test_create_COLLECTION_success(self, mock_create):
        # Mock the COLLECTIONService's get_or_create_COLLECTION method
        mock_create.return_value = self.sample_COLLECTION

        response = self.client.post('/api/COLLECTION/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertEqual(data, self.sample_COLLECTION)

    # TODO: Write more tests

if __name__ == '__main__':
    unittest.main()