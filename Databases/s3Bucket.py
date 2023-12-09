import boto3
import os

# Uploads an image to the S3 bucket
def uploadImage(photo_path, image):
    """
    Uploads an image to the S3 bucket.

    Args:
        photo_path (str): The local path of the photo to upload.
        image (str): The name of the image file in the S3 bucket.

    Returns:
        bool: True if the upload is successful, False otherwise.
    """
    try:
        access_key = os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        region = os.getenv('AWS_REGION')
        bucket_name = os.getenv('AWS_BUCKET_NAME')

        if not access_key or not secret_key or not region or not bucket_name:
            raise ValueError("Missing required environment variables.")

        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        s3.upload_file(photo_path, bucket_name, image)
        
    except ValueError as ve:
        print(ve)
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    return True