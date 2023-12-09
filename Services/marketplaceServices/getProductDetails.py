from Databases.mySQL import connectToDB
from responses import (
    internal_server_error_response, mysql_connection_error_response,
    no_search_results_response, missing_parameters_response
)

def getProductDetails(eventMethod, eventBody):
    """
    Retrieves product details based on the given product ID.

    Args:
        eventMethod (str): The HTTP method used for the request.
        eventBody (dict): The request body containing the product ID.

    Returns:
        dict: The response containing the product details.

    Raises:
        Exception: If any error occurs during the process.
    """

    try:
        # Extract product ID from the request body
        productID = eventBody.get('productId')

        if productID is None:
            return missing_parameters_response

        # Connect to the database
        db = connectToDB()

        if db is None:
            return mysql_connection_error_response

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to retrieve product details
        query = f"SELECT product_id, name, category_id, image_url, price_per_unit, unit_of_measurement, contact_info, available_units, owner_id, basic_description, created_at, updated_at FROM Product WHERE product_id = {productID}"
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        if result is None:
            return no_search_results_response

        # Extract the product details from the result
        (
            productID, name, categoryID, image_url, pricePerUnit, unitOfMeasurement,
            contactInfo, availableUnits, ownerID, basicDescription, createdAt, updatedAt
        ) = result

        # Create the response dictionary
        response = {
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
        }

        # Close the database connection
        db.close()

        return response

    except Exception as e:
        print(e)
        return internal_server_error_response