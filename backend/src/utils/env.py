import os
from src.utils.enum import ENV

env = ENV(os.environ.get("ENV", ENV.LOCAL))

jwt_secret_key = os.getenv("JWT_SECRET_KEY")

dynamo_endpoint = os.getenv("DYNAMO_ENDPOINT", "http://store-db:8000")
aws_region = os.getenv("AWS_REGION", "us-east-1")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
