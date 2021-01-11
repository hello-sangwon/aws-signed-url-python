import boto3
from botocore.config import Config
import time

s3_client = boto3.client('s3')

upload_bucket = 'test-bucket'
action_id = int(time.time())
expiration = 3600

upload_s3_params = {
    'Bucket': upload_bucket,
    'Key': f"{action_id}.jpg",
    'ContentType': 'image/jpeg',
    'CacheControl': 'max-age=31104000'
}
upload_url = s3_client.generate_presigned_url('put_object', upload_s3_params, ExpiresIn=expiration)
print(upload_url)

download_s3_params = {
    'Bucket': upload_bucket,
    'Key': f"{action_id}.jpg"
}
download_url = s3_client.generate_presigned_url('get_object', download_s3_params, ExpiresIn=expiration)
print(download_url)
