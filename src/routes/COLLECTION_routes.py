from flask import Blueprint, request, jsonify
from src.models.token import create_token
from src.services.COLLECTION_services import COLLECTIONService
from src.models.breadcrumb import create_breadcrumb

import logging
logger = logging.getLogger(__name__)

def create_COLLECTION_routes():
    # Define the Blueprint
    COLLECTION_routes = Blueprint('COLLECTION_routes', __name__)

    # POST /api/COLLECTION/ - Create a COLLECTION
    @COLLECTION_routes.route(methods=['POST'])
    def create_COLLECTION():
        try:
            breadcrumb = create_breadcrumb()
            token = create_token()
            data = request.get_json()
            COLLECTION = COLLECTIONService.post_COLLECTION(data, token, breadcrumb)
            logger.info(f"Get COLLECTION Successful {breadcrumb}")
            return jsonify(COLLECTION), 200
        except Exception as e:
            logger.warn(f"A processing error occurred {e}")
            return jsonify({"error": "A processing error occurred"}), 500

    # GET /api/COLLECTION/{id}/ - Get a COLLECTION
    @COLLECTION_routes.route('/<string:id>', methods=['GET'])
    def get_COLLECTION(id):
        try:
            breadcrumb = create_breadcrumb()
            token = create_token()
            COLLECTION = COLLECTIONService.get_COLLECTION(id, token, breadcrumb)
            logger.info(f"Get COLLECTION Successful {breadcrumb}")
            return jsonify(COLLECTION), 200
        except Exception as e:
            logger.warn(f"A processing error occurred {e}")
            return jsonify({"error": "A processing error occurred"}), 500

    # PATCH /api/COLLECTION/{id} - Update a COLLECTION
    @COLLECTION_routes.route('/<string:id>', methods=['PATCH'])
    def update_COLLECTION(id):
        try:
            token = create_token()
            breadcrumb = create_breadcrumb()
            data = request.get_json()
            COLLECTION = COLLECTIONService.update_COLLECTION(id, data, token, breadcrumb)
            logger.info(f"Update COLLECTION Successful {breadcrumb}")
            return jsonify(COLLECTION), 200
        except Exception as e:
            logger.warn(f"A processing error occurred {e}")
            return jsonify({"error": "A processing error occurred"}), 500
        
    # Ensure the Blueprint is returned correctly
    return COLLECTION_routes