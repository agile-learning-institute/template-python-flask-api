from datetime import datetime
from pathlib import Path
from pymongo import ObjectID
import os
import logging

logger = logging.getLogger(__name__)

class Config:
    _instance = None  # Singleton instance

    def __init__(self):
        if Config._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Config._instance = self
            self.config_items = []
            self.versions = []
            self.enumerators = {}
            self.api_version = ""

            # Private properties
            self._port = 8088
            self._config_folder = "./"
            self._version_collection_name = ""
            self._enumerators_collection_name = ""

            # TODO Additional config properties
            
            # Initialize configuration
            self.initialize()

    def initialize(self):
        """Initialize configuration values."""
        self.config_items = []
        self.versions = []
        self.enumerators = {}
        self.api_version = "1.0." + self._get_config_value("BUILT_AT", "LOCAL", False)
        self._config_folder = self._get_config_value("CONFIG_FOLDER", "/opt/mentorhub-COLLECTION-api", False)
        self._port = int(self._get_config_value("PORT", "8088", False))

        # TODO Additional config item initialization 
        
        logger.info(f"Configuration Initialized: {self.config_items}")
            
    def _get_config_value(self, name, default_value, is_secret):
        """Retrieve a configuration value, first from a file, then environment variable, then default."""
        value = default_value
        from_source = "default"

        # Check for config file first
        file_path = Path(self._config_folder) / name
        if file_path.exists():
            value = file_path.read_text().strip()
            from_source = "file"
        # If no file, check for environment variable
        elif os.getenv(name):
            value = os.getenv(name)
            from_source = "environment"

        # Record the source of the config value
        self.config_items.append({
            "name": name,
            "value": "secret" if is_secret else value,
            "from": from_source
        })
        return value

    # Simple Getters
    def get_port(self):
        return self._port

    def get_config_folder(self):
        return self._config_folder

    def get_version_collection_name(self):
        return self._version_collection_name

    def get_enumerators_collection_name(self):
        return self._enumerators_collection_name

    # TODO Add getters as needed


    # Serializer
    def to_dict(self):
        """Convert the Config object to a dictionary with the required fields."""
        return {
            "api_version": self.api_version,
            "config_items": self.config_items,
            "versions": Config._decode_mongo_types(self.versions),
            "enumerators": Config._decode_mongo_types(self.enumerators)
        }    

    @staticmethod
    def _decode_mongo_types(document):
        """Convert all ObjectId and datetime values to strings"""
        if isinstance(document, dict):
            return {key: Config._decode_mongo_types(value) for key, value in document.items()}
        elif isinstance(document, list):
            return [Config._decode_mongo_types(item) for item in document]
        elif isinstance(document, ObjectId):
            return str(document)
        elif isinstance(document, datetime):
            return document.isoformat()
        else:
            return document

    # Singleton Getter
    @staticmethod
    def get_instance():
        """Get the singleton instance of the Config class."""
        if Config._instance is None:
            Config()
        return Config._instance
        
# Create a singleton instance of Config and export it
config = Config.get_instance()