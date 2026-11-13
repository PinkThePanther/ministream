from flask import Flask
import boto3

app = Flask(__name__)
s3 = boto3.client("s3", region_name="us-east-1")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate-upload-url", methods=["POST"])
def generate_upload_url():
    return {"message": "Upload endpoint working"}
