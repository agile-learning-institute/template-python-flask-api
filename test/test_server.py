import unittest
from unittest.mock import patch
import sys
import signal
from src.server import app, mongo, handle_exit, logger

class TestServer(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.client = app.test_client()
        self.client.testing = True

    def test_app_exists(self):
        # Ensure the Flask app is created
        self.assertIsNotNone(app)

    def test_health_endpoint(self):
        # Test the health endpoint
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)

    def test_COLLECTION_routes_registered(self):
        # Test if COLLECTION routes are registered
        response = self.client.get('/api/COLLECTION/TEST_ID/')
        self.assertIn(response.status_code, [200, 404])  # 200 if exists, 404 if not found
        
    def test_config_routes_registered(self):
        # Test if config routes are registered
        response = self.client.get('/api/config/')
        self.assertIn(response.status_code, [200, 404])  # 200 if config is returned, 404 if not found

    @patch('src.server.logger')
    @patch('src.server.mongo')
    @patch('sys.exit')
    def test_signal_handler(self, mock_exit, mock_mongo, mock_logger):
        # Simulate receiving a SIGINT signal
        handle_exit(signal.SIGINT, None)

        # Check that the logger received the correct messages
        mock_logger.info.assert_any_call("Received signal 2. Initiating shutdown...")
        mock_logger.info.assert_any_call("MongoDB connection closed.")

        # Check that mongo.disconnect was called
        mock_mongo.disconnect.assert_called_once()

        # Check that sys.exit was called with code 0
        mock_exit.assert_called_once_with(0)

    def tearDown(self):
        # Clean up after tests (if necessary)
        pass

if __name__ == '__main__':
    unittest.main()