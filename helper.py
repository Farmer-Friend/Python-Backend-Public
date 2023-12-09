from Services import users, crops, news, schedules, policy, marketplace, activity
from responses import path_not_found_response, external_server_error_response,method_not_allowed_response

# Define a dictionary to map service paths to service functions
service_mapping = {
    'users': users.handle_user_services,
    'crops': crops.handle_crop_services,
    'news': news.handle_news_services,
    'schedules': schedules.handle_schedule_services,
    'governmentPolicies': policy.handle_policy_services,
    'marketPlace': marketplace.handle_marketplace_services,
    'activity': activity.handle_activity_service
}

def helperFunction(servicePath, methodPath, eventMethod, eventBody):
    """
    Helper function to handle requests based on the provided service path, method path, event method, and event body.

    Args:
        servicePath (str): The service path.
        methodPath (str): The method path.
        eventMethod (str): The event method.
        eventBody (dict): The event body.

    Returns:
        dict: The response based on the request.

    Raises:
        Exception: If an error occurs during the request handling.
    """
    try:
        if eventMethod not in ['GET', 'POST']:
            return method_not_allowed_response

        print("servicePath: ", servicePath)

        # Find the corresponding service function based on the service path
        service_function = service_mapping.get(servicePath)
        if service_function:
            return service_function(methodPath, eventMethod, eventBody)
        else:
            return path_not_found_response

    except Exception as e:
        print(e)
        return external_server_error_response
