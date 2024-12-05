from datetime import datetime, timezone
import uuid
from bson import ObjectId
from flask import request

def create_breadcrumb():
    """Create a breadcrumb dictionary from HTTP headers."""
    return {
        "atTime": datetime.now(timezone.utc),
        "byUser": ObjectId(request.headers.get('X-User-Id')),
        "fromIp": request.remote_addr,  
        "correlationId": request.headers.get('X-Correlation-Id', str(uuid.uuid4()))  
    }
