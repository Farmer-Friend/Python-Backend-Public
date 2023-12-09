from Databases.mySQL import connectToDB
from responses import (
    method_not_allowed_response,
    missing_parameters_response,
    mysql_connection_error_response,
    internal_server_error_response,
    unauthorized_response
)


def logout(eventMethod, eventBody):
    """
    Logs out a user by inserting a logout activity into the activity log table.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing user details.

    Returns:
        dict: A response message indicating the success or failure of the logout operation.
    """

    # Check if the request method is allowed
    if eventMethod not in ['GET', 'POST']:
        return method_not_allowed_response

    try:
        # Connect to the database
        conn = connectToDB()

        # Check if the database connection is successful
        if not conn:
            return mysql_connection_error_response

        # Get the user details from the request body
        user_id = eventBody.get('user_id')
        ipAddress = eventBody.get('ipAddress')
        sessionToken = eventBody.get('sessionToken')

        # Check if all required parameters are present
        if not (sessionToken and user_id and ipAddress):
            return unauthorized_response

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Insert the logout activity into the activity log table
        cursor.execute(
            "INSERT INTO activity_log (user_id, ip_address, session, activity) VALUES (?, ?, ?, 'logout')",
            (user_id, ipAddress, sessionToken)
        )

        # Insert into transaction 
        cursor.execute(
            "INSERT INTO transactions (user_id,action) VALUES (?, 'logout')",
            (user_id)
        )

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

        return {
            'message': 'Logged out successfully'
        }

    except Exception as e:
        # Handle any exceptions and return an internal server error response
        return internal_server_error_response
