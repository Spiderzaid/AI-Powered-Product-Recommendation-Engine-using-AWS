import os, sys
# Make the Lambda code folder importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lambda_fn'))
from app import handler

def make_event(path, method="GET", qs=None, body=None):
    return {
        "requestContext": {"http": {"path": path, "method": method}},
        "queryStringParameters": qs or {},
        "body": body
    }

def test_personalized_requires_user():
    res = handler(make_event("/recommendations/personalized"))
    assert res["statusCode"] == 400

def test_personalized_ok():
    res = handler(make_event("/recommendations/personalized", qs={"userId":"U1","k":"3"}))
    assert res["statusCode"] == 200

def test_related_requires_item():
    res = handler(make_event("/recommendations/related"))
    assert res["statusCode"] == 400

def test_related_ok():
    res = handler(make_event("/recommendations/related", qs={"itemId":"I1","k":"2"}))
    assert res["statusCode"] == 200

def test_events_post():
    res = handler(make_event("/events", method="POST", body='{"userId":"U1"}'))
    assert res["statusCode"] == 200
