from Databases.mySQL import connectToDB
from responses import (
    internal_server_error_response, mysql_connection_error_response,
    no_search_results_response, missing_parameters_response
)

def searchProduct(eventMethod, eventBody):
    """
    Search for products based on a keyword.

    Args:
        eventMethod (str): The method of the event.
        eventBody (dict): The body of the event.

    Returns:
        list: A list of dictionaries containing the search results.
    """
    try:
        keyword = eventBody.get('queryStringParameters')

        if not keyword:
            return missing_parameters_response

        db = connectToDB()

        if not db:
            return mysql_connection_error_response

        cursor = db.cursor()

        query = """
            SELECT product_id, name, category_id, image_url, price_per_unit,
            unit_of_measurement, contact_info, available_units, owner_id,
            basic_description, created_at, updated_at
            FROM Product
            WHERE name LIKE ?
        """
        cursor.execute(query, ('%' + keyword + '%',))

        result = cursor.fetchall()

        if not result:
            return no_search_results_response

        response = []

        for product in result:
            productID, name, categoryID, image_url, pricePerUnit, unitOfMeasurement, \
            contactInfo, availableUnits, ownerID, basicDescription, createdAt, updatedAt = product

            response.append({
                "productID": str(productID),
                "name": str(name),
                "categoryID": str(categoryID),
                "image_url": str(image_url),
                "pricePerUnit": str(pricePerUnit),
                "unitOfMeasurement": str(unitOfMeasurement),
                "contactInfo": str(contactInfo),
                "availableUnits": str(availableUnits),
                "ownerID": str(ownerID),
                "basicDescription": str(basicDescription),
                "createdAt": str(createdAt),
                "updatedAt": str(updatedAt)
            })

        db.close()
        return response

    except Exception as e:
        print(e)
        return internal_server_error_response