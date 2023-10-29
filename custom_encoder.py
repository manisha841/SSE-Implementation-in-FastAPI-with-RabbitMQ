import json
from datetime import datetime
from uuid import UUID


class CustomEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle UUID and datetime serialization."""

    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
