
import json
import os
from util import ok, bad_request

# In a real deployment, these would call Amazon Personalize or a SageMaker endpoint.
# Here we mock with simple logic for a portfolio starter.

def handler(event, context=None):
    route_key = event.get('requestContext', {}).get('http', {}).get('path', '')
    query = event.get('queryStringParameters') or {}
    method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')

    if route_key.endswith('/recommendations/personalized') and method == 'GET':
        user_id = query.get('userId')
        k = int(query.get('k', 10))
        if not user_id:
            return bad_request("Missing userId")
        # mock: top-N by popularity in user's segment
        items = [f"ITEM_{i}" for i in range(1, k+1)]
        return ok({"userId": user_id, "items": items})

    if route_key.endswith('/recommendations/related') and method == 'GET':
        item_id = query.get('itemId')
        k = int(query.get('k', 10))
        if not item_id:
            return bad_request("Missing itemId")
        # mock: related items by same category (placeholder)
        items = [f"{item_id}_SIM_{i}" for i in range(1, k+1)]
        return ok({"itemId": item_id, "items": items})

    if route_key.endswith('/events') and method == 'POST':
        # accept an event payload and respond OK
        body = event.get('body') or "{}"
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            return bad_request("Invalid JSON body")
        # Normally send to Kinesis/SQS here.
        return ok({"status": "accepted", "received": payload})

    return bad_request("Unsupported route")
