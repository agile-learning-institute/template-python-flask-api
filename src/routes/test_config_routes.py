import unittest
from flask import Flask
from src.routes.config_routes import create_config_routes

class TestConfigRoutes(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test app and register the blueprint
        self.app = Flask(__name__)
        config_routes = create_config_routes()
        self.app.register_blueprint(config_routes, url_prefix='/api/config')
        self.client = self.app.test_client()

    def test_get_config_success(self):
        # Simulate a GET request to the /api/config endpoint
        response = self.client.get('/api/config/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()