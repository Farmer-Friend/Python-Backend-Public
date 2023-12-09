from Databases.mySQL import connectToDB, checkSession
from responses import (
    internal_server_error_response, method_not_allowed_response,
    missing_parameters_response, mysql_connection_error_response,
    success_response, user_not_logged_in_response)


def handle_activity_service(function_path, event_method, event_body):
    """
        Handle activity services.

        Args:
            method_path (str): The method path.
            event_method (str): The event method.
            event_body (dict): The event body.

        Returns:
            Response: The response object.
        """
    # Check if the method path and event method are valid
    if event_method != 'POST':
        return method_not_allowed_response

    try:
        # Extract the required parameters from the event body

        
        action = event_body.get('action')
        ip_address = event_body.get('ipAddress')
        session_id = event_body.get('session_token')

        # Check if any of the required parameters are missing
        if None in (session_id, action, ip_address):
            return missing_parameters_response

        # Connect to the database
        with connectToDB() as conn:
            # Check if the session is valid
            user_id = checkSession(conn, session_id)

            # If the session is not valid, return user not logged in response
            if not user_id:
                return user_not_logged_in_response

            # Insert the activity log into the database
            cursor = conn.cursor()
            query = (
                "INSERT INTO activity_log (user_id, session_key, action, ip_address) "
                "VALUES (%s, %s, %s, %s)"
            )
            cursor.execute(query, (user_id, session_id, action, ip_address))
            conn.commit()
            cursor.close()

            # Return success response
            return success_response

        # Return MySQL connection error response
        return mysql_connection_error_response

    except Exception as e:
        # Return internal server error response
        return internal_server_error_response
