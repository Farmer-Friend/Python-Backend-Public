import json
from Databases.mySQL import connectToDB
from responses import *

def getPolicyDetails(eventMethod, eventBody):
    """
    Retrieves policy details based on the provided policyId.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing the policyId.

    Returns:
        dict: The policy details as a dictionary.

    Raises:
        Exception: If any error occurs during the process.
    """

    try:
        policyId = eventBody.get('policyId')

        if not policyId:
            return missing_parameters_response

        conn = connectToDB()
        if not conn:
            return mysql_connection_error_response

        cursor = conn.cursor()

        query = "SELECT scheme_id, title, issued_by, eligibility, process, basic_description, link, time FROM policy WHERE scheme_id = ?"
        cursor.execute(query, (policyId,))

        result = cursor.fetchone()

        if not result:
            return item_details_not_found_response

        scheme_id, title, issued_by, eligibility, process, basic_description, link, time = result

        policyDict = {
            'scheme_id': str(scheme_id),
            'title': str(title),
            'issued_by': str(issued_by),
            'eligibility': str(eligibility),
            'process': str(process),
            'basic_description': str(basic_description),
            'link': str(link),
            'time': str(time)
        }

        conn.close()

        return policyDict

    except Exception as e:
        return internal_server_error_response
