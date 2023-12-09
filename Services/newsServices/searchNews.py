from Databases.mySQL import connectToDB
from responses import (
    internal_server_error_response, mysql_connection_error_response,
    no_search_results_response, missing_parameters_response
)

def searchNews(evenMethod, eventBody):
    """
    Search news based on a keyword.

    Args:
        eventBody (dict): The request body containing the keyword.
        eventMethod (str): The HTTP method used for the request.

    Returns:
        list: A list of dictionaries representing the search results.
    """
    try:
        # Get the keyword from the request body
        keyword = eventBody.get('queryStringParameters')

        # Check if the keyword is missing
        if not keyword:
            return missing_parameters_response

        # Connect to the database
        conn = connectToDB()

        # Check if the database connection is successful
        if not conn:
            return mysql_connection_error_response

        # Create a cursor object
        cursor = conn.cursor()

        # Construct the SQL query
        query = "SELECT news_id, title, picture, link, date, language FROM news WHERE title LIKE ? ORDER BY date DESC"

        # Execute the query with the keyword as a parameter
        cursor.execute(query, ('%' + keyword + '%',))

        # Fetch all the search results
        newsList = cursor.fetchall()

        # Check if there are no search results
        if not newsList:
            return no_search_results_response

        # Prepare the search results as a list of dictionaries
        newsListDict = []
        for news in newsList:
            newsDict = {
                "id": news[0],
                "title": news[1],
                "picture": news[2],  # "https://www.abc.com/xyz.jpg"
                "link": news[3],
                "date": news[4],
                "language": news[5]
            }
            newsListDict.append(newsDict)

        # Close the database connection
        conn.close()

        return newsListDict

    except Exception as e:
        # Handle any exceptions and return an internal server error response
        print(e)
        return internal_server_error_response
