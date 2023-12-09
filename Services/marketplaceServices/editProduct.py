from Databases.mySQL import connectToDB, checkSession
from Databases.s3Bucket import uploadImage
from responses import (
    internal_server_error_response,
    method_not_allowed_response,
    missing_parameters_response,
    unauthorized_response,
    mysql_connection_error_response,
)


def editProduct(eventMethod, eventBody):
    """
    Edit a product in the marketplace.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing the updated product details.

    Returns:
        dict: The response containing the product ID and message.
    """
    if eventMethod != 'POST':
        return method_not_allowed_response

    try:
        session = eventBody.get('sessionId')

        if session is None:
            return missing_parameters_response

        user_id = checkSession(session)
        if user_id is None:
            return unauthorized_response

        product_id = eventBody.get('productId')
        name = eventBody.get('name')
        category_id = eventBody.get('categoryId')
        price_per_unit = eventBody.get('pricePerUnit')
        unit_of_measurement = eventBody.get('unitOfMeasurement')
        contact_info = eventBody.get('contactInfo')
        available_units = eventBody.get('availableUnits')
        basic_description = eventBody.get('basicDescription')

        if not all([product_id, name, category_id, price_per_unit, unit_of_measurement, contact_info, available_units, basic_description]):
            return missing_parameters_response

        db = connectToDB()
        if db is None:
            return mysql_connection_error_response

        cursor = db.cursor()
        query = "UPDATE Product SET name=?, category_id=?, price_per_unit=?, unit_of_measurement=?, contact_info=?, available_units=?, basic_description=? WHERE product_id=? AND owner_id=?"
        cursor.execute(query, (name, category_id, price_per_unit, unit_of_measurement, contact_info, available_units, basic_description, product_id, user_id))

        # Insert into transactions table
        cursor.execute(
            "INSERT INTO transactions (user_id,action) VALUES (?, 'editProduct')",
            (user_id)
        )

        
        db.commit()
        cursor.close()
        db.close()

        return {
            'productId': product_id,
            'message': 'Product edited successfully'
        }

    except Exception as e:
        return internal_server_error_response
