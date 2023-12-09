from responses import external_server_error_response
from helper import helperFunction
from Databases.s3Bucket import uploadImage
import os
import json

s3_bucket_link = os.getenv('AWS_BUCKET_LINK')

def lambda_handler(event,context):

    try:
        method = event.get('httpMethod')
        path=event.get('path')

        body={}
        for key in event.get('queryStringParameters',{}):
            body[key]=event['queryStringParameters'][key]

        # extract from body json
        if event.get('body') is not None:
            body.update(json.loads(event['body']))

        # Check for photo

        if 'photo' in event.get('multiValueHeaders',{}):
            photo = event['multiValueHeaders']['photo']
            if photo[0] != '':
                filename = photo[0]
                body['imageUrl'] = s3_bucket_link + filename

                try:
                    uploadImage(filename, filename)
                except Exception as e:
                    # Handle file upload or deletion errors
                    return external_server_error_response(str(e))

        p1,p2=path.split('/')[1],path.split('/')[2]

        response=helperFunction(p1,p2, method, body)

        # if response is flask response return it
        if 'statusCode' in response:
            return response
        
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }


    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
