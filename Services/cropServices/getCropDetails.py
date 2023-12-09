from bson.objectid import ObjectId
from responses import method_not_allowed_response, internal_server_error_response, missing_parameters_response, item_details_not_found_response
from Databases.mongoDB import client
import os

# Get the database name and collection name from environment variables
dbName = os.getenv('MONGO_DB', 'Crops')
collectionName = os.getenv('MONGO_COLLECTION', 'english')


def get_crop_details(event_method, event_body):
    """
    Get crop details from MongoDB based on the provided cropId.

    Args:
        event_method (str): The method of the event.
        event_body (dict): The body of the event containing the cropId.

    Returns:
        dict: The crop details as a dictionary.

    Raises:
        Exception: If any error occurs during the process.
    """

    # Check if the event method is allowed
    if event_method not in ['GET', 'POST']:
        return method_not_allowed_response

    try:
        # Get the cropId from the event body
        crop_id = event_body.get('cropId')

        # Check if cropId is provided
        if crop_id is None:
            return missing_parameters_response

        # Convert the cropId to ObjectId
        crop_id = ObjectId(crop_id)

        # Search the database for the cropId provided
        collection = client[dbName][collectionName]

        # Find the crop details
        crop_details = collection.find_one({'_id': crop_id})

        # Check if crop details are found
        if crop_details is None:
            return item_details_not_found_response

        # Convert ObjectId to string
        crop_details['_id'] = str(crop_details['_id'])

        # Return the crop details
        return crop_details

    except Exception as e:
        print(e)
        return internal_server_error_response
