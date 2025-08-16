
import json

def ok(payload, status_code=200):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(payload)
    }

def bad_request(message, status_code=400):
    return ok({"error": message}, status_code=status_code)
