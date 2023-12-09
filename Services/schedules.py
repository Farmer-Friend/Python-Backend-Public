from responses import internal_server_error_response, path_not_found_response
from Services.scheduleServices import (
    getScheduleDetails,
    addSchedule,
    deleteSchedule,
    updateSchedule,
    getScheduleList,
)

method_mapping = {
    'getScheduleDetails': getScheduleDetails.getScheduleDetails,
    'addSchedule': addSchedule.addSchedule,
    'deleteSchedule': deleteSchedule.deleteSchedule,
    'updateSchedule': updateSchedule.updateSchedule,
    'getScheduleList': getScheduleList.getScheduleList,
}

# 
# -- Schedules
# CREATE TABLE Schedules (
#     schedule_id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255),
#     crop_id INT,
#     crop_name VARCHAR(255),
#     start_date TIMESTAMP,
#     end_date TIMESTAMP,
#     area INT,
#     owner_id INT,
#     basic_description TEXT,
#     FOREIGN KEY (owner_id) REFERENCES Users(user_id)
# );

# Handle schedule services

# 1. Get schedule details
# Request:
# {
#     "id": "id"
# }

# Response Body:
# {
#     "id": "1",
#     "title": "title",
#     "cropId": "cropId",
#     "cropName": "cropName",
#     "startDate": "startDate",
#     "endDate": "endDate",
#     "area": "area",
#     "ownerId": "ownerId",
#     "basicDescription": "basicDescription"
# }

# 2. Add schedule
# Request:
# {
#     "sessionId": "sessionId",
#     "title": "title",
#     "cropId": "cropId",
#     "startDate": "startDate",
#     "endDate": "endDate",
#     "area": "area",
#     "ownerId": "ownerId",
#     "basicDescription": "basicDescription"
# }

# Response Body:
# {
#     "id": "1",
# }

# 3. Delete schedule
# Request:
# {
#     "sessionId": "sessionId",
#     "id": "id"
# }

# Response Body:
# {
#     "message": "Successfully deleted schedule."
# }

# 4. Update schedule
# Request:
# {
#     "sessionId": "sessionId",
#     "id": "id",
#     "title": "title",
#     "cropId": "cropId",
#     "startDate": "startDate",
#     "endDate": "endDate",
#     "area": "area",
#     "basicDescription": "basicDescription"
# }

# Response Body:
# {
#     "message": "Successfully updated schedule.",
#      "id": "1"
# }


# 5. Get schedule list
# Request:
# {
#     "sessionId": "sessionId"
# }

# Response Body:
# {
#     "schedules": [{
#         "id": "1",
#         "title": "title",
#         "cropId": "cropId",
#         "cropName": "cropName",
#         "startDate": "startDate",
#         "endDate": "endDate",
#         "area": "area",
#         "ownerId": "ownerId",
#         "basicDescription": "basicDescription"
#     }]
# }









def handle_schedule_services(function_path, eventMethod, eventBody):
    """
    This function routes the incoming request to the appropriate schedule service function based on the function_path.

    Args:
        function_path (str): The path of the function to be executed.
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body.

    Returns:
        dict: The response of the executed function.

    Raises:
        Exception: If an error occurs during the execution of the function.
    """
    try:
        if function_path not in method_mapping:
            return path_not_found_response

        return method_mapping[function_path](eventMethod, eventBody)

    except Exception as e:
        return internal_server_error_response
