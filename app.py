import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from Databases.s3Bucket import uploadImage
from helper import helperFunction
from Databases.mySQL import connectToDB, checkSession
from Databases.mongoDB import ping,client
from responses import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
s3_bucket_link = os.getenv('AWS_BUCKET_LINK')

@app.route('/', methods=['GET'])
def root():
    """
    Returns the response message with basic description of the API.
    """
    return 'Hello World! This is a simple API for the Backend of the Project.'

@app.route('/<path1>/<path2>', methods=['POST', 'GET'])
def python_server(path1, path2):
    """
    Handles requests to the custom path /<path1>/<path2>.

    Args:
        path1 (str): The first path parameter.
        path2 (str): The second path parameter.

    Returns:
        str: The response message.

    Raises:
        ValueError: If the request is missing required parameters.
    """
    method = request.method
    body = dict(request.args)

    for key in request.form:
        body[key] = str(request.form.getlist(key)[0])

    body['ipAddress'] = request.remote_addr

    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            filename = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)
            
            body['imageUrl'] = s3_bucket_link + filename

            try:
                uploadImage(photo_path, filename)
                os.remove(photo_path)
            except Exception as e:
                # Handle file upload or deletion errors
                return jsonify({'error': str(e)}), 500
    
    return helperFunction(path1,path2, method, body)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
