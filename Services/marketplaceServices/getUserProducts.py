from Databases.mySQL import connectToDB, checkSession
from responses import (
    method_not_allowed_response,
    missing_parameters_response,
    mysql_connection_error_response,
    internal_server_error_response,
    unauthorized_response,
    no_search_results_response
)


def getUserProducts(eventMethod, eventBody):
    """
    Get user's products based on the provided session token.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing the session token.

    Returns:
        list: A list of products owned by the user.

    Raises:
        Exception: If any error occurs during the process.
    """

    try:
        if eventMethod != 'POST':
            return method_not_allowed_response

        sessionToken = eventBody.get('sessionToken')

        if sessionToken is None:
            return missing_parameters_response

        user_id = checkSession(sessionToken)

        if not user_id:
            return unauthorized_response

        conn = connectToDB()

        if not conn:
            return mysql_connection_error_response

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Product WHERE owner_id=?", (user_id,))
        products = cursor.fetchall()

        if not products:
            return no_search_results_response

        products_list = []
        for product in products:
            products_list.append({
                'productId': str(product[0]),
                'name': str(product[1]),
                'categoryId': str(product[2]),
                'pricePerUnit': str(product[3]),
                'unitOfMeasurement': str(product[4]),
                'contactInfo': str(product[5]),
                'availableUnits': str(product[6]),
                'ownerId': str(product[7]),
                'basicDescription': str(product[8]),
                'imageUrl': str(product[9]),
            })

        return products_list

    except Exception as e:
        return internal_server_error_response