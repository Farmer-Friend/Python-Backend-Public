import json
from Databases.mySQL import connectToDB
from responses import *

def searchPolicy(eventMethod, eventBody):
    """
    Search for policies based on a keyword in the title or basic description.
    
    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing the keyword.
        
    Returns:
        dict or list: The response containing the search results or an error message.
    """
    try:
        if eventMethod not in ['POST', 'GET']:
            return method_not_allowed_response
        
        keyword = eventBody.get('queryStringParameters')
        
        if not keyword:
            return missing_parameters_response
        
        keyword = keyword.lower()
        
        conn = connectToDB()
        if not conn:
            return mysql_connection_error_response
        
        cursor = conn.cursor()
        
        # Search in title or basic_description (case insensitive)
        query = """
            SELECT scheme_id, title, issued_by, eligibility, process, basic_description, link, time
            FROM policy
            WHERE lower(title) LIKE '%{}%' OR lower(basic_description) LIKE '%{}%';
        """.format(keyword, keyword)
        
        cursor.execute(query)
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
        return {
            "statusCode": 501,
            "body": json.dumps({
                "message": "Error in function searchPolicy: " + str(e)
            })
        }
