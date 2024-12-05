from datetime import datetime
from bson import ObjectId
from flask import jsonify
from src.utils.mongo_io import MongoIO
import logging
logger = logging.getLogger(__name__)

class COLLECTIONService:

    @staticmethod 
    def _check_user_access(COLLECTION_id, token):
        """Role Based Access Control logic"""
        # TODO Implement RBAC Logic - if <has access> return
        
        # User has No Access! Log a warning and raise an exception
        logger.warn(f"Access Denied: {COLLECTION_id}, {token['user_id']}, {token['roles']}")
        raise Exception("Access Denied")
      
    @staticmethod
    def create_COLLECTION(COLLECTION_id, token, breadcrumb):
        """Get a COLLECTION if it exits, if not create a new one and return that"""
        COLLECTIONService._check_user_access(COLLECTION_id, token)

        mongo_io = MongoIO()
        mongo_io.create_COLLECTION(COLLECTION_id, breadcrumb)
        COLLECTION = mongo_io.get_COLLECTION(COLLECTION_id)
        return COLLECTION

    @staticmethod
    def get_COLLECTION(COLLECTION_id, token, breadcrumb):
        """Get a COLLECTION if it exits, if not create a new one and return that"""
        COLLECTIONService._check_user_access(COLLECTION_id, token)

        mongo_io = MongoIO()
        mongo_io.get_COLLECTION(COLLECTION_id, breadcrumb)
        COLLECTION = mongo_io.get_COLLECTION(COLLECTION_id)
        return COLLECTION

    @staticmethod
    def update_COLLECTION(COLLECTION_id, patch_data, token, breadcrumb):
        """Update the specified COLLECTION"""
        COLLECTIONService._check_user_access(COLLECTION_id, token)

        # Add breadcrumb to patch_data
        patch_data["lastSaved"] = breadcrumb
        mongo_io = MongoIO()
        mongo_io.update_COLLECTION(COLLECTION_id, patch_data)
        COLLECTION = mongo_io.get_COLLECTION(COLLECTION_id)
        return COLLECTION

