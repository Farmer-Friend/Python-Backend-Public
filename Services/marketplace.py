from responses import path_not_found_response, internal_server_error_response
from Services.marketplaceServices import (
    addProduct,
    editProduct,
    deleteProduct,
    getProductDetails,
    getTrendingProducts,
    searchProduct,
    getUserProducts
)

method_mapping = {
    'addProduct':addProduct.addProduct,
    'editProduct':editProduct.editProduct,
    'deleteProduct':deleteProduct.deleteProduct,
    'getProductDetails':getProductDetails.getProductDetails,
    'getTrendingProducts':getTrendingProducts.get_trending_products,
    'searchProduct':searchProduct.searchProduct,
    'getUserProducts':getUserProducts.getUserProducts,
}


# -- Products
# CREATE TABLE Products (
#     product_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     category_id INT,
#     price_per_unit DECIMAL(10, 2),
#     unit_of_measurement VARCHAR(50),
#     contact_info VARCHAR(255),
#     available_units INT,
#     owner_id INT,
#     basic_description TEXT,
#     image_url TEXT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#     FOREIGN KEY (category_id) REFERENCES Category(category_id),
#     FOREIGN KEY (owner_id) REFERENCES Users(user_id)
# );



# Marketplace services handler

# Request and Response format

# 1. Add Product
# Request
# {
#     'sessionId': '1234567890',
#     'name': 'Rice',
#     'categoryId': '1',
#     'pricePerUnit': '100',
#     'unitOfMeasurement': 'kg',
#     'contactInfo': '1234567890',
#     'availableUnits': '100',
#     'ownerId': '1',
#     'basicDescription': 'Rice',
#     'imageUrl': 'https://www.google.com',
# }

# Response body
# {
#     'productId': '1',
#     'message': 'Product added successfully'
# }


# 2. Edit Product

# Request
# {
#     'sessionId': '1234567890',
#     'productId': '1',
#     'name': 'Rice',
#     'categoryId': '1',
#     'pricePerUnit': '100',
#     'unitOfMeasurement': 'kg',
#     'contactInfo': '1234567890',
#     'availableUnits': '100',
#     'basicDescription': 'Rice'
# }

# Response body
# {
#     'productId': '1',
#     'message': 'Product edited successfully'
# }


# 3. Delete Product

# Request
# {
#     'sessionId': '1234567890',
#     'productId': '1'
# }

# Response body
# {
#    'message': 'Product deleted successfully'
# }


# 4. Get Product Details

# Request
# {
#    'productId': '1'
# }

# Response body
# {
#     'productId': '1',
#     'name': 'Rice',
#     'categoryId': '1',
#     'pricePerUnit': '100',
#     'unitOfMeasurement': 'kg',
#     'contactInfo': '1234567890',
#     'availableUnits': '100',
#     'ownerId': '1',
#     'basicDescription': 'Rice',
#     'imageUrl': 'https://www.google.com',
# }


# 5. Get Trending Products

# Request
# {
# }

# Response body
# {
#     'products':[{
#         'productId': '1',
#         'name': 'Rice',
#         'categoryId': '1',
#         'pricePerUnit': '100',
#         'unitOfMeasurement': 'kg',
#         'contactInfo': '1234567890',
#         'availableUnits': '100',
#         'ownerId': '1',
#         'basicDescription': 'Rice',
#         'imageUrl': 'https://www.google.com',
#     }]
# }


# 6. Search Product

# Request
# {
#     'queryStringParameters': 'rice'
# }

# Response body
# {
#     'products':[{
#         'productId': '1',
#         'name': 'Rice',
#         'categoryId': '1',
#         'pricePerUnit': '100',
#         'unitOfMeasurement': 'kg',
#         'contactInfo': '1234567890',
#         'availableUnits': '100',
#         'ownerId': '1',
#         'basicDescription': 'Rice',
#         'imageUrl': 'https://www.google.com',
#     }]
# }


# 7. Get User's Products

# Request
# {
#   'sessionId': '1234567890'
# }

# Response body
# {
#     'products':[{
#         'productId': '1',
#         'name': 'Rice',
#         'categoryId': '1',
#         'pricePerUnit': '100',
#         'unitOfMeasurement': 'kg',
#         'contactInfo': '1234567890',
#         'availableUnits': '100',
#         'ownerId': '1',
#         'basicDescription': 'Rice',
#         'imageUrl': 'https://www.google.com',
#     }]
# }








def handle_marketplace_services(function_path, method, body):
    """
    Handle various marketplace services based on the provided path.

    Args:
        path (str): The path of the event.
        method (str): The HTTP method of the event.
        body (dict): The body of the event.

    Returns:
        dict: The response of the marketplace service.

    Raises:
        ValueError: If the path is not valid.
        Exception: If any other error occurs.
    """
    
    try:

        if function_path not in method_mapping:
            return path_not_found_response

        return method_mapping[function_path](method, body)
    
    except Exception as e:
        return internal_server_error_response
    
