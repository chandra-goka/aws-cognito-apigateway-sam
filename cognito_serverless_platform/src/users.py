import json


def handle(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"statusCode": 200, "data": "I am a users function"}),
        "isBase64Encoded": False,
    }
