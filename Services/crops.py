from responses import path_not_found_response, internal_server_error_response
from Services.cropServices import searchCrops, getCropDetails, getCropList

method_mapping = {
    'searchCrops':searchCrops.search_crops,
    'getCropDetails':getCropDetails.get_crop_details,
    'getCropList':getCropList.get_crop_list
}

# Product services handler

# Request and Response format

# 1. Search Crops
# Request
# {
#     "queryStringParameters": "rice"
# }

# Response body
# {
#     'crops':[{
#         'cropId': '1',
#         'cropName': 'Rice',
#         .....
#     }]
# }


# 2. Get Crop Details
# Request
# {
#    "cropId": "1"
# }

# Response body
# {
#     'cropId': '1',
#     'cropName': 'Rice',
#     .....
# }

# 3. Get Crop List
# Request
# {
# }

# Response body
# {
#     'crops':[{
#         'cropId': '1',
#         'cropName': 'Rice',
#         .....
#     }]
# }


def handle_crop_services(function_path, event_method, event_body):
    """
    Handle crop services based on the provided event path, method, and body.

    Args:
        event_path (str): The path of the event.
        event_method (str): The method of the event.
        event_body (dict): The body of the event.

    Returns:
        The response based on the provided event path and method.
    """
    try:

        if function_path not in method_mapping:
            return path_not_found_response

        return method_mapping[function_path](event_method, event_body)
    
    except Exception as e:
        return internal_server_error_response