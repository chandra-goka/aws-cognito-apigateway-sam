import json


def handle(event, context):
    categories = ["Books", "Python", "AWS", "Java"]
    return {
        "statusCode": 200,
        "body": json.dumps({"statusCode": 200, "data": categories}),
        "isBase64Encoded": False,
    }
