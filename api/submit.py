import json

def handler(request):
    if request.method == "POST":
        body = request.json()
        name = body.get("name", "Unknown")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({ "message": f"Hello, {name}!" })
        }
    else:
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }
