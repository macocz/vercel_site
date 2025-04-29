import json

def handler(request):
    data = {
        "message": "Hello from Python!",
        "success": True
    }
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data)
    }