from Databases.mySQL import connectToDB
from responses import (
    internal_server_error_response, mysql_connection_error_response,
    no_search_results_response, missing_parameters_response
)

def get_trending_products(event_method, event_body):
    """
    Retrieves the trending products from the database.

    Args:
        event_method (str): The event method.
        event_body (dict): The event body.

    Returns:
        list: A list of dictionaries representing the trending products.
    """
    try:
        # Connect to the database
        db = connectToDB()

        if db is None:
            return mysql_connection_error_response
        
        cursor = db.cursor()

        # Columns: product_id, name, category_id, image_url, price_per_unit, unit_of_measurement, contact_info, available_units, owner_id, basic_description, created_at, updated_at
        query = "SELECT product_id, name, category_id, image_url, price_per_unit, unit_of_measurement, contact_info, available_units, owner_id, basic_description, created_at, updated_at FROM Product ORDER BY created_at DESC LIMIT 10"
        cursor.execute(query)

        result = cursor.fetchall()

        if not result:
            return no_search_results_response
        
        response = []

        for product in result:
            product_id, name, category_id, image_url, price_per_unit, unit_of_measurement, contact_info, available_units, owner_id, basic_description, created_at, updated_at = product

            response.append({
                "productID": str(product_id),
                "name": str(name),
                "categoryID": str(category_id),
                "image_url": str(image_url),
                "pricePerUnit": str(price_per_unit),
                "unitOfMeasurement": str(unit_of_measurement),
                "contactInfo": str(contact_info),
                "availableUnits": str(available_units),
                "ownerID": str(owner_id),
                "basicDescription": str(basic_description),
                "createdAt": str(created_at),
                "updatedAt": str(updated_at)
            })

        db.close()
        return response

    except Exception as e:
        print(e)
        return internal_server_error_response
