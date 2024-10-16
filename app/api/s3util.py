import boto3
import dotenv

bucket_name='img-similarity'

class S3Uploader:
    def __init__(self):
        #note: this line will work in a deployment environment only if we have AWS CLI set up on our remote runner. We can configure that with a Dockerfile
        # the following line will handle config. If you have AWS CLI configured on your computer, comment it out and see if it works!
        # insert config here
        # config = {'region': 'us-east-2'}
        dotenv.load_dotenv()
        self.client = boto3.client('s3')

    def put_s3_image(self, image):
        print("uploading ", image.filename, " to s3")
        response = self.client.put_object(Bucket=bucket_name, Key=image.filename, Body=image)
    def get_s3_image(self, path):
        img = self.client.get_object(Bucket=bucket_name, Key=path)
        return img