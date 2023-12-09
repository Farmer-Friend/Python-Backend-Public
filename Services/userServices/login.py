from Databases.mySQL import connectToDB, checkSession
import bcrypt
from responses import (
    method_not_allowed_response,
    missing_parameters_response,
    mysql_connection_error_response,
    internal_server_error_response,
    unauthorized_response,
    user_not_found_response,
    user_already_logged_in_response,
    success_response
)
import hashlib
import datetime


def login(eventMethod, eventBody):
    """
    Logs in a user by validating their credentials and creating a login session.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing user details.

    Returns:
        dict: The response containing the login session details.
    """
    try:
        conn = connectToDB()

        if not conn:
            return mysql_connection_error_response

        if eventMethod == 'GET':
            sessionToken = eventBody.get('sessionToken', None)
            if not sessionToken :
                return unauthorized_response
                
            elif checkSession(sessionToken):
                return user_already_logged_in_response
            else:
                return success_response
            
        if eventMethod != 'POST':
            return method_not_allowed_response

        # Get the user details from the body
        phoneNo = eventBody.get('phoneNo')
        password = eventBody.get('password')
        ipAddress = eventBody.get('ipAddress')

        # Check if any required parameter is missing
        if not all([phoneNo, password, ipAddress]):
            return missing_parameters_response

        cursor = conn.cursor()

        cursor.execute("SELECT password,user_id,name,email,experience_in_farming FROM users WHERE phone_no=?", (phoneNo,))
        user = cursor.fetchone()

        # Check if the user exists
        if not user:
            return user_not_found_response

        db_password = user[0]
        user_id = user[1]

        db_password = db_password.decode('utf-8')

        # Check if the password is correct using bcrypt
        if not bcrypt.checkpw(password.encode(), db_password.encode()):
            # Add an attempt to the loginAttempts table
            cursor.execute("INSERT INTO login_attempts(user_id,ip_address,used_password) VALUES(?,?,?)",
                           (user_id, ipAddress, password))
            conn.commit()
            conn.close()
            return unauthorized_response

        # Create a login session for the user by hashing the phoneNo and timestamp
        # The login session will be valid for 14 days
        # The login session will be stored in the database

        # Create a hash of the phoneNo and timestamp
        hashString = phoneNo + str(datetime.datetime.now())
        hashString = hashString.encode('utf-8')

        loginSession = hashlib.sha256(hashString).hexdigest()

        # Store the login session in the database
        cursor.execute("INSERT INTO activity_log(user_id,session_key,ip_address,activity) VALUES(?,?,?,'login')",
                       (user[1], loginSession, ipAddress))
        
        # Insert into transactions table
        cursor.execute("INSERT INTO transactions(user_id, action ) VALUES(?,'login')", (user_id,))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        # Return the login session
        return {
            'sessionToken': loginSession,
            'user_id': user[1],
            'name': user[2],
            'email': user[3],
            'experience_in_farming': user[4]
        }

    except Exception as e:
        return internal_server_error_response
