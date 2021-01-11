# AWS S3 Presigned URL Sample

### Set Up Environment Variables
```
export AWS_ACCESS_KEY_ID='AKIASCHPJFR12345678'
export AWS_SECRET_ACCESS_KEY='abcd......................'
export AWS_REGION='us-west-2'
```

### Run
```
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install boto3
(venv) $ python app.py
https://test-bucket.s3.amazonaws.com/1610363392.jpg?AWSAccessKeyId=AKIASCHPJFR12345678&Signature=I5QhzCQsL4W5UDD2vRTj%2B0qBo2A%3D&content-type=image%2Fjpeg&Expires=1610366992
https://test-bucket.s3.amazonaws.com/1610363392.jpg?AWSAccessKeyId=AKIASCHPJFR12345678&Signature=nZ7yDgaznfXF137%2BMgQ1mszKmlQ%3D&Expires=1610366992
(venv) $
```
