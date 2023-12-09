from responses import path_not_found_response, internal_server_error_response
from Services.policyServices import searchPolicy, getPolicyDetails, getPolicyList

# Mapping of function paths to corresponding methods
method_mapping = {
    'searchPolicy': searchPolicy.searchPolicy,
    'getPolicyDetails': getPolicyDetails.getPolicyDetails,
    'getPolicyList': getPolicyList.getPolicyList
}

# -- Policy
# -- Government Schemes
# CREATE TABLE Policy (
#     scheme_id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255),
#     issued_by VARCHAR(255),
#     eligibility TEXT,
#     process TEXT,
#     basic_description TEXT,
#     link VARCHAR(255),
#     time TIMESTAMP
# );

# Handle policy services

# 1. Search policy
# Request:
# {
#     "queryStringParameters": "title"
# }

# Response Body:
# {
#    "policies": [{
#         "id": "1",
#         "title": "title",
#         "issuedBy": "issuedBy",
#         "eligibility": "eligibility",
#         "process": "process",
#         "basicDescription": "basicDescription",
#         "link": "link",
#         "time": "time"
#     }]
# }

# 2. Get policy details
# Request:
# {
#     "id": "id"
# }

# Response Body:
# {
#     "id": "1",
#     "title": "title",
#     "issuedBy": "issuedBy",
#     "eligibility": "eligibility",
#     "process": "process",
#     "basicDescription": "basicDescription",
#     "link": "link",
#     "time": "time"
# }

# 3. Get policy list
# Request:
# {
#   }

# Response Body:
# {
#     "policies": [{
#         "id": "1",
#         "title": "title",
#         "issuedBy": "issuedBy",
#         "eligibility": "eligibility",
#         "process": "process",
#         "basicDescription": "basicDescription",
#         "link": "link",
#         "time": "time"
#     }]
# }




def handle_policy_services(function_path, eventMethod, eventBody):
    """
    Executes the corresponding policy service method based on the function path.

    Args:
        function_path (str): The path of the function.
        eventMethod (str): The method of the event.
        eventBody (dict): The body of the event.

    Returns:
        dict: The response from the executed policy service method.
    """
    try:
        if function_path not in method_mapping:
            return path_not_found_response
        
        return method_mapping[function_path](eventMethod, eventBody)
        
    except Exception as e:
        return internal_server_error_response
