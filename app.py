from flask import Flask
import boto3
import uuid
from botocore.config import Config

app = Flask(__name__)

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 's3v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

s3 = boto3.client("s3", region_name="us-east-1",config=my_config)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate-upload-url", methods=["POST"])
def generate_upload_url():
    object_key = f"videos/{uuid.uuid4()}.mp4"
    upload_url = s3.generate_presigned_url(
    ClientMethod="put_object",
    Params={
        "Bucket": "ministream-videos-uniqueidentifier",
        "Key":object_key
    }
)
    return {"upload_url": upload_url}
