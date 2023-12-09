import bcrypt
from responses import (
    method_not_allowed_response,
    success_response,
    missing_parameters_response,
    mysql_connection_error_response,
    internal_server_error_response,
    unauthorized_response,
    user_not_found_response
)
from Databases.mySQL import connectToDB, checkSession


def changepassword(eventMethod, eventBody):
    """
    Change the user's password.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing user_id, oldPassword, newPassword, sessionToken, and ipAddress.

    Returns:
        dict: The response object.

    Raises:
        Exception: If any error occurs during the password change process.
    """
    if eventMethod != 'POST':
        return method_not_allowed_response

    try:
        # Connect to the database
        conn = connectToDB()

        # Check if the connection failed
        if not conn:
            return mysql_connection_error_response

        # Extract request parameters
        oldPassword = eventBody.get('oldPassword')
        newPassword = eventBody.get('newPassword')
        sessionToken = eventBody.get('sessionToken')
        ipAddress = eventBody.get('ipAddress')

        # Check if any required parameter is missing
        if not all([ oldPassword, newPassword, sessionToken, ipAddress]):
            return missing_parameters_response

        user_id=checkSession(sessionToken)
        if not user_id:
            return unauthorized_response
        
        # Create a cursor object
        cursor = conn.cursor()

        # Construct the SQL query
        query1="SELECT password FROM users WHERE id = ?"
        query2="UPDATE users SET password = ? WHERE id = ?"

        # Execute the query with the keyword as a parameter
        cursor.execute(query1, (user_id,))
        # Fetch all the search results
        password = cursor.fetchone()

        # Check if there are no search results
        if not password:
            return user_not_found_response
        
        # Check if the old password is correct
        if not bcrypt.checkpw(oldPassword.encode(), password[0].encode()):
            return unauthorized_response
        
        # Hash the new password
        hashedPassword = bcrypt.hashpw(newPassword.encode(), bcrypt.gensalt())

        # Execute the query with the keyword as a parameter
        cursor.execute(query2, (hashedPassword, user_id))

        # Insert into transaction
        cursor.execute(
            "INSERT INTO transactions (user_id,action) VALUES (?, 'changepassword')",
            (user_id)
        )

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()

        return success_response
    
    except Exception as e:
        return internal_server_error_response