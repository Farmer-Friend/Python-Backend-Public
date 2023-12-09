import hashlib
import datetime
import bcrypt
from responses import (
    method_not_allowed_response,
    missing_parameters_response,
    mysql_connection_error_response,
    internal_server_error_response,
    unauthorized_response,
    user_already_exists_response,
    user_already_logged_in_response
)
from Databases.mySQL import connectToDB, checkSession


def register(eventMethod, eventBody):
    """
    Register a user with the provided information.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing user information.

    Returns:
        dict: The response containing session token and user information.

    Raises:
        Exception: If any error occurs during the registration process.
    """
    try:
        conn = connectToDB()

        if not conn:
            return mysql_connection_error_response

        if eventMethod == 'GET':
            sessionToken = eventBody.get('sessionToken', None)
            user_id = eventBody.get('user_id', None)
            if not sessionToken or not user_id:
                return {
                    'statusCode': 200
                }
            elif checkSession(conn, sessionToken, user_id):
                return user_already_logged_in_response
            else:
                return {
                    'statusCode': 200
                }

        if eventMethod != 'POST':
            return method_not_allowed_response

        # Collect User Data
        phoneNo = eventBody.get('phoneNo', None)
        password = eventBody.get('password', None)
        ipAddress = eventBody.get('ipAddress', None)
        name = eventBody.get('name', None)
        email = eventBody.get('email', None)
        experience = eventBody.get('experience', None)

        if not name or not email or not experience:
            return missing_parameters_response

        hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        cursor = conn.cursor()

        # Check if user already exists
        query = "SELECT * FROM users WHERE phone_no=?"
        cursor.execute(query, (phoneNo,))

        if cursor.fetchone():
            return user_already_exists_response

        # Create a random 8 char user_id for user
        user_id = hashlib.sha256(str(datetime.datetime.now()).encode()).hexdigest()[:8]

        # Insert user data
        query = "INSERT INTO users(user_id, phone_no, password, name, email, experience_in_farming) VALUES(?,?,?,?,?,?)"
        cursor.execute(query, (user_id, phoneNo, hashedPassword, name, email, experience))

        # Create Session from phoneno and timestamp and store in database
        session = hashlib.sha256((phoneNo + str(datetime.datetime.now())).encode()).hexdigest()

        cursor.execute('INSERT INTO activity_log(user_id, session_key, ip_Address, activity) VALUES(?,?,?,"register")',
                       (user_id, session, ipAddress))
        
        # Insert into transactions table
        cursor.execute("INSERT INTO transactions(user_id, action ) VALUES(?,'register')", (user_id,))

        conn.commit()
        cursor.close()

        return {
            'sessionToken': session,
            'user_id': user_id,
            'name': name,
            'email': email,
            'experience': experience
        }

    except Exception as e:
        print(e)
        return internal_server_error_response
