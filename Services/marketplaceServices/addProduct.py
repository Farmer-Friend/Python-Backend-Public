from Databases.mySQL import connectToDB, checkSession
from responses import (
    method_not_allowed_response,
    internal_server_error_response,
    missing_parameters_response,
    unauthorized_response,
    mysql_connection_error_response,
)


def addProduct(eventMethod, eventBody):
    """
    Add a product to the marketplace.

    Args:
        eventMethod (str): The HTTP method of the request.
        eventBody (dict): The request body containing the product details.

    Returns:
        dict: The response containing the product ID, message, and image URL.
    """
    if eventMethod != 'POST':
        return method_not_allowed_response

    try:
        sessionToken = eventBody.get('sessionId')

        # Connect to the database
        conn = connectToDB()

        if conn is None:
            return mysql_connection_error_response

        user_id = checkSession(sessionToken)

        if not user_id:
            return unauthorized_response

        # Get the product details from the request body
        name = eventBody.get('name')
        category_id = eventBody.get('categoryId')
        price_per_unit = eventBody.get('pricePerUnit')
        unit_of_measurement = eventBody.get('unitOfMeasurement')
        contact_info = eventBody.get('contactInfo')
        available_units = eventBody.get('availableUnits')
        owner_id = user_id
        basic_description = eventBody.get('basicDescription')
        image_url = eventBody.get('imageUrl')

        # Check if any required parameter is missing
        if not all([name, category_id, price_per_unit, unit_of_measurement, contact_info, available_units, basic_description, image_url]):
            return missing_parameters_response

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        import hashlib
        # generate the random product ID int
        product_id = int(hashlib.sha1(str.encode(name)).hexdigest(), 16) % (10 ** 8)


        # Construct the SQL query
        query = """
            INSERT INTO Product (
                product_id,
                name, category_id, price_per_unit, unit_of_measurement,
                contact_info, available_units, owner_id, basic_description, image_url
            ) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # Execute the query with the keyword as a parameter
        cursor.execute(
            query,
            (
                product_id,
                name, category_id, price_per_unit, unit_of_measurement,
                contact_info, available_units, owner_id, basic_description, image_url
            ),
        )

        # Insert into transaction
        cursor.execute(
            "INSERT INTO transactions (user_id,action) VALUES (?, 'addproduct')",
            (user_id)
        )

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()

        # Return the response
        return {
            'productId': product_id,
            'message': 'Product added successfully',
            'imageUrl': image_url
        }

    except Exception as e:
        print(e)
        return internal_server_error_response