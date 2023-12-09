from Databases.mySQL import connectToDB
from responses import *

def getPolicyList(eventMethod, eventBody):
    """
    Retrieves a list of policies from the database.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body.

    Returns:
        list: A list of policy objects.

    Raises:
        Exception: If an error occurs during the process.
    """
    try:
        # Connect to the database
        conn = connectToDB()

        if not conn:
            return mysql_connection_error_response

        # Retrieve policy data from the database
        cursor = conn.cursor()
        cursor.execute("SELECT scheme_id, title, issued_by, eligibility, process, basic_description, link, time FROM policy")
        result = cursor.fetchall()

        if not result:
            return no_search_results_response

        policyList = []
        for row in result:
            scheme_id, title, issued_by, eligibility, process, basic_description, link, time = row
            policyList.append({
                'scheme_id': str(scheme_id),
                'title': str(title),
                'issued_by': str(issued_by),
                'eligibility': str(eligibility),
                'process': str(process),
                'basic_description': str(basic_description),
                'link': str(link),
                'time': str(time)
            })

        conn.close()

        return policyList

    except Exception as e:
        return internal_server_error_response
