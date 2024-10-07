import boto3

#note: this line will work only if we have AWS CLI set up on our remote runner. We can configure that with a Dockerfile
class S3Uploader:
    def __init__(self):
        self.client = boto3.client('s3')

    def put_s3_image(self, image):
        print("uploading ", image.filename, " to s3")
        response = self.client.put_object(Bucket='img-similarity', Key=image.filename, Body=image)
    def get_s3_image(self, path):
        img = self.client.get_object(Bucket='img-similarity', Key=path)
        return img