import os
from pymongo import MongoClient

# Get environment variables or set default values
_MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
_MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
_MONGO_USER = os.getenv('MONGO_USER', '')
_MONGO_PASS = os.getenv('MONGO_PASS', '')
_MONGO_AUTH = os.getenv('MONGO_AUTH', 'admin')
_MONGO_DB = os.getenv('MONGO_DB', 'mydatabase')
_MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'mycollection')

# Create a new client and connect to the server
client = MongoClient(
    host=_MONGO_HOST,
    port=_MONGO_PORT,
    username=_MONGO_USER,
    password=_MONGO_PASS,
    authSource=_MONGO_AUTH,
    maxPoolSize=10  # Set the maximum number of connections in the connection pool
)

# Check if the connection is successful
def ping():
    try:
        client.admin.command('ping')
        return True
    except Exception as e:
        return False
