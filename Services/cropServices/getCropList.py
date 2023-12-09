from Databases.mongoDB import client, ping
from responses import *
from typing import Dict
import json
import os

# Set the default values for the database name and collection name
db_name = os.getenv('MONGO_DB', 'Crops')
collection_name = os.getenv('MONGO_COLLECTION', 'english')


def get_crop_list(eventMethod: str, eventBody: Dict) -> str:
    """
    Get the crop list from the database.

    Args:
        eventMethod (str): The method of the event.
        eventBody (Dict): The body of the event.

    Returns:
        str: JSON string representing the crop list.
    """
    # Check if the event method is allowed
    if eventMethod not in ['GET', 'OPTIONS', 'POST']:
        return method_not_allowed_response

    try:
        # Check if the MongoDB connection is available
        if not ping():
            return mongo_connection_error_response

        # Get crop list from database
        db = client[db_name][collection_name]
        crop_list = list(db.find({}))

        # Convert ObjectId to string for each crop
        for crop in crop_list:
            crop['_id'] = str(crop['_id'])

        return json.dumps(crop_list)

    except Exception as e:
        return internal_server_error_response
