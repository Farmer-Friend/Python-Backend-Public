from flask import Response

# 200 - OK
service_not_implemented_response = Response(
    '{"message": "Service not implemented"}', status=200, mimetype='application/json'
)

# Success Response
success_response = Response(
    '{"message": "Success"}', status=200, mimetype='application/json'
)

# 400 - Bad Request
bad_request_response = Response(
    '{"message": "Bad request"}', status=400, mimetype='application/json'
)


# 401 - Unauthorized
unauthorized_response = Response(
    '{"message": "Unauthorized"}', status=401, mimetype='application/json'
)

# 404 - Not Found
page_not_found_response = Response(
    '{"message": "Page not found"}', status=404, mimetype='application/json'
)

# 405 - Method Not Allowed
method_not_allowed_response = Response(
    '{"message": "Method not allowed"}', status=405, mimetype='application/json'
)

# 406 - Not Acceptable
path_not_found_response = Response(
    '{"message": "Path not found"}', status=406, mimetype='application/json'
)

# 500 - Internal Server Error
internal_server_error_response = Response(
    '{"message": "Internal Server Error"}', status=500, mimetype='application/json'
)

# 502 - Bad Gateway
external_server_error_response = Response(
    '{"message": "External Server Error"}', status=502, mimetype='application/json'
)

# 503 - Service Unavailable
missing_parameters_response = Response(
    '{"message": "Missing Parameters"}', status=503, mimetype='application/json'
)

# 504 - Gateway Timeout
no_search_results_response = Response(
    '{"message": "No search results"}', status=504, mimetype='application/json'
)

# 505 - HTTP Version Not Supported
item_details_not_found_response = Response(
    '{"message": "Item details not found"}', status=505, mimetype='application/json'
)

## User Services

# 701 - Custom Status Code for Failed Login
failed_login_response = Response(
    '{"message": "Failed Login", "error": "Invalid password"}',
    status=701,
    mimetype='application/json',
)

# 702 - Custom Status Code for User Not Found
user_not_found_response = Response(
    '{"message": "User not found", "error": "User not found"}',
    status=702,
    mimetype='application/json',
)

# 703 - Custom Status Code for User Already Exists
user_already_exists_response = Response(
    '{"message": "User already exists", "error": "User already exists"}',
    status=703,
    mimetype='application/json',
)

# 704 - Custom Status Code for User Already Logged In
user_already_logged_in_response = Response(
    '{"message": "User already logged in"}', status=704, mimetype='application/json'
)

# 705 - Custom Status Code for User Not Logged In
user_not_logged_in_response = Response(
    '{"message": "User not logged in"}', status=705, mimetype='application/json'
)

## Database Responses

# 901 - Custom Status Code for MySQL Connection Error
mysql_connection_error_response = Response(
    '{"message": "MySQL connection error"}', status=901, mimetype='application/json'
)

# 902 - Custom Status Code for MongoDB Connection Error
mongo_connection_error_response = Response(
    '{"message": "MongoDB connection error"}', status=902, mimetype='application/json'
)
