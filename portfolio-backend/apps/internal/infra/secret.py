# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/
import json
import os

import boto3
from botocore.exceptions import ClientError


def get_open_ai_key():
    secret_name = os.environ['OPEN_AI_KEY_SECRET_PATH']
    region_name = "ap-northeast-1"
    if secret_name is None:
        raise Exception("Secret name cannot be empty")
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e
    data = json.loads(get_secret_value_response['SecretString'])
    _openai_api_key = data["OPENAI_API_KEY"]
    return _openai_api_key
