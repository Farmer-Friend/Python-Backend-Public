from Databases.mongoDB import ping, client
from responses import *
import os

# Get the database and collection names from environment variables
dbName = os.getenv('MONGO_DB', 'Crops')
collectionName = os.getenv('MONGO_COLLECTION', 'english')


def search_crops(event_method, event_body):
    """
    Search crops in the database based on a keyword.

    Args:
        event_method (str): The HTTP method used for the request.
        event_body (dict): The request body containing the keyword.

    Returns:
        list: A list of dictionaries containing the crop details.

    Raises:
        Exception: If any error occurs during the search process.
    """
    try:
        # Check if the method is GET
        if event_method != 'GET':
            return method_not_allowed_response

        # Check if the database connection is successful
        if not ping():
            return mongo_connection_error_response

        # Extract the keyword from the event body
        keyword = event_body.get('queryStringParameters')

        # Check if the keyword is provided
        if keyword is None:
            return missing_parameters_response

        # Search the database for the keyword provided
        collection = client[dbName][collectionName]
        crops = collection.find({'Name': {'$regex': keyword, '$options': 'i'}})

        # Convert the crops to a list of dictionaries
        crops = [crop for crop in crops]

        # Convert the ObjectId to string
        for crop in crops:
            crop['_id'] = str(crop['_id'])

        # Return the crops
        return crops

    except Exception as e:
        return internal_server_error_response
