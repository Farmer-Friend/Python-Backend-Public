from Services.userServices import login, register, logout, changepassword
from responses import internal_server_error_response, path_not_found_response

method_mapping = {
    'login': login.login,
    'register': register.register,
    'logout': logout.logout,
    'changepassword': changepassword.changepassword,
}


# -- Users
# CREATE TABLE Users (
#     user_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     phone_no VARCHAR(20) UNIQUE,
#     email VARCHAR(255),
#     password VARCHAR(255),
#     experience_in_farming INT
# );

# Handle user services

# 1. Login
# Request:
# {
#     "phoneNo": "phoneNo",
#     "password": "password"
# }

# Response Body:
# {
#     "sessionId": "sessionId"
# }

# 2. Register
# Request:
# {
#     "name": "name",
#     "phoneNo": "phoneNo",
#     "email": "email",
#     "password": "password",
#     "experienceInFarming": "experienceInFarming"
# }

# Response Body:
# {
#     "userId": "userId",
#     "sessionId": "sessionId"
# }

# 3. Logout
# Request:
# {
#     "sessionId": "sessionId"
# }

# Response Body:
# {
#     "message": "Logged out successfully"
# }

# 4. Change password
# Request:
# {
#     "sessionId": "sessionId",
#     "oldPassword": "oldPassword",
#     "newPassword": "newPassword"
# }

# Response Body:
# {
#     "sessionId": "sessionId",
#     "message": "Password changed successfully"
# }


def handle_user_services(function_path, eventMethod, eventBody):
    """
    Handles user services based on the provided event path, method, and body.

    Args:
        eventPath (str): The path of the event.
        eventMethod (str): The HTTP method of the event.
        eventBody (dict): The body of the event.

    Returns:
        dict: The response based on the requested user service.
    """
    try:
        if function_path not in method_mapping:
            return path_not_found_response

        return method_mapping[function_path](eventMethod, eventBody)
    
    except Exception as e:
        return internal_server_error_response
