# AI-Powered Product Recommendation Engine (AWS)

Serverless recommendation API running on **AWS Lambda + API Gateway (HTTP API)** with a clean, testable Python codebase. Easy to extend with Amazon Personalize, DynamoDB, and a React frontend.

---

## 🚀 Live API (Demo)

**Base URL:** https://hcqne2tob5.execute-api.us-east-2.amazonaws.com/prod

### Endpoints
- `GET /recommendations/personalized?userId=U1&k=3`
- `GET /recommendations/related?itemId=I100&k=3`
- `POST /events`  _(JSON body: `{"userId":"U1","itemId":"I100","event_type":"view"}`)_

### Try in your browser
- Personalized: https://hcqne2tob5.execute-api.us-east-2.amazonaws.com/prod/recommendations/personalized?userId=U1&k=3  
- Related: https://hcqne2tob5.execute-api.us-east-2.amazonaws.com/prod/recommendations/related?itemId=I100&k=3

### curl examples
```bash
BASE="https://hcqne2tob5.execute-api.us-east-2.amazonaws.com/prod"
curl "$BASE/recommendations/personalized?userId=U1&k=3"
curl "$BASE/recommendations/related?itemId=I100&k=3"
curl -X POST "$BASE/events" -H "content-type: application/json" -d '{"userId":"U1","itemId":"I100","event_type":"view"}'

## implemented

Serverless API: API Gateway (HTTP API) → Lambda (Python 3.11)

Handlers:

personalized (mock top-N for a user)

related (mock similar items)

events (accepts JSON event payload)

Unit tests: pytest (all tests passing)

Repo layout: ready for CI/CD, infra, and data utilities

🧭 Roadmap 

Amazon Personalize integration (real recs)

Batch & retraining (Step Functions/EventBridge)

DynamoDB (catalog + event storage)

React frontend on S3 + CloudFront

Observability (CloudWatch dashboards, alarms)

IaC expansion (Terraform for API/Lambda/roles)


🗂 Project structure

services/
  api/
    lambda_fn/
      app.py
      util.py
    openapi.yaml
    tests/
      test_api.py
data/
  generators/
    generate_synthetic.py
infra/
  terraform/
    main.tf  variables.tf  outputs.tf
.github/
  workflows/
    cicd.yml
README.md

## 🛠 Run locally

**Requirements:** Python 3.11+, pip

```bash
# create & activate venv (Windows Git Bash)
python -m venv .venv             
source .venv/Scripts/activate

# install deps & run tests
python -m pip install --upgrade pip
python -m pip install -r services/api/requirements.txt
python -m pytest -q

## 🚢 Manual deploy (quick path)

1) Zip the Lambda code (run from `services/api/lambda_fn` on Windows PowerShell):
```powershell
Compress-Archive -Path * -DestinationPath ../lambda.zip -Force
Upload to AWS Lambda (Console):

Runtime: Python 3.11

Handler: app.handler

Code: upload services/api/lambda.zip

Create an HTTP API (API Gateway) and attach the Lambda to these routes:

GET /recommendations/personalized

GET /recommendations/related

POST /events

Create stage prod with Auto-deploy ON and use the Invoke URL shown on the stage page.




