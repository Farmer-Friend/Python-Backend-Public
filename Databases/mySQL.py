import os
import logging
import mysql.connector

# Credentials
_HOST_MySQL = os.getenv('MYSQL_HOST')
_USER_MySQL = os.getenv('MYSQL_USER')
_PASSWORD_MySQL = os.getenv('MYSQL_PASSWORD')
_DATABASE_MySQL = os.getenv('MYSQL_DATABASE')

def connectToDB():
    """
    Connects to the MySQL database.

    Returns:
        connection: MySQL database connection object.
    """
    try:
        connection = mysql.connector.connect(
            host=_HOST_MySQL,
            user=_USER_MySQL,
            password=_PASSWORD_MySQL,
            database=_DATABASE_MySQL
        )
        return connection
    except mysql.connector.Error as e:
        logging.error(f"Failed to connect to the database: {e}")
        return None

def ping():
    """
    Checks if the database connection is successful.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        with connectToDB() as connection:
            if connection is None:
                return False
            else:
                return True
    except mysql.connector.Error:
        return False

def checkSession(session_id):
    """
    Checks if a session exists in the database.

    Args:
        session_id (str): Session ID to check.

    Returns:
        int or False: User ID associated with the session if it exists, False otherwise.
    """
    try:
        with connectToDB() as connection:
            if connection is None:
                return False
            else:
                cursor = connection.cursor()
                query = "SELECT user_id FROM activity_log WHERE session_key = %s"
                cursor.execute(query, (session_id,))
                result = cursor.fetchone()
                if result is None:
                    return False
                else:
                    return result[0]
    except mysql.connector.Error:
        return False
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



def addTransaction(userID,action):
    """
    Adds a transaction to the database.

    Args:
        userID (str): User ID of the user performing the transaction.
        action (str): Action performed by the user.
    """
    try:
        with connectToDB() as connection:
            if connection is None:
                return False
            else:
                cursor = connection.cursor()
                query = "INSERT INTO activity_log (user_id, action) VALUES (%s, %s)"
                cursor.execute(query, (userID, action))
                connection.commit()
                return True
    except mysql.connector.Error:
        return False
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            