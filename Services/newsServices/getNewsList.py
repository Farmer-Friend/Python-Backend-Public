from Databases.mySQL import connectToDB
from responses import (
    internal_server_error_response, mysql_connection_error_response,
    no_search_results_response
)


def getNewsList(eventMethod, eventBody):
    """
    Retrieves the latest news list from the database.

    Args:
        eventMethod (str): The HTTP method used for the request.
        eventBody (dict): The request body.

    Returns:
        list: The list of latest news items.

    Raises:
        Exception: If an error occurs during the process.
    """
    try:
        # Connect to the database
        conn = connectToDB()

        if not conn:
            return mysql_connection_error_response

        cursor = conn.cursor()

        # Get Latest News top 5
        query = "SELECT news_id, title, picture, link, date, language FROM news ORDER BY date DESC LIMIT 5"

        cursor.execute(query)
        newsList = cursor.fetchall()

        if not newsList:
            return no_search_results_response

        newsListDict = []
        for news in newsList:
            newsDict = {
                "id": str(news[0]),
                "title": news[1],
                "picture": news[2],
                "link": news[3],
                "date": str(news[4]),
                "language": news[5]
            }
            newsListDict.append(newsDict)

        conn.close()

        return newsListDict

    except Exception as e:
        return internal_server_error_response
