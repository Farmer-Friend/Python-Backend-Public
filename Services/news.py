from responses import path_not_found_response, internal_server_error_response
from Services.newsServices import getNewsList, searchNews

method_mapping = {
    'getNewsList': getNewsList.getNewsList,
    'searchNews': searchNews.searchNews
}


# -- News
# CREATE TABLE News (
#     news_id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255),
#     description TEXT,
#     link VARCHAR(255),
#     picture TEXT,
#     language VARCHAR(50),    
#     date TIMESTAMP
# );

# Handle news services

# 1. Get news list
# Request:
# {
#   }


# Response Body:
# {
#     "id": "1",
#     "title": "title",
#     "picture": "picture",
#     "link": "link",
#     "date": "date",
#     "language": "language"
# }

# 2. Search news
# Request:
# {
#     "queryStringParameters": "title"
# }

# Response Body:
# {
#    "news": [{
#         "id": "1",
#         "title": "title",
#         "picture": "picture",
#         "link": "link",
#         "date": "date",
#         "language": "language"
#     }]
# }



def handle_news_services(functionPath, eventMethod, eventBody):
    """
    Handles the news services based on the function path, event method, and event body.

    Args:
        functionPath (str): The path of the function.
        eventMethod (str): The method of the event.
        eventBody (dict): The body of the event.

    Returns:
        dict: The response based on the function path, or an error response if an exception occurs.
    """
    try:
        if functionPath not in method_mapping:
            return path_not_found_response
        
        return method_mapping[functionPath](eventMethod, eventBody)

    except Exception as e:
        return internal_server_error_response