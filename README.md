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

What’s implemented now

Serverless API: API Gateway (HTTP API) → Lambda (Python 3.11)

Handlers:

personalized (mock top-N for a user)

related (mock similar items)

events (accepts JSON event payload)

Unit tests: pytest (all tests passing)

Repo layout: ready for CI/CD, infra, and data utilities
🧭 Roadmap (next)

Amazon Personalize integration (real recs)

Batch & retraining (Step Functions/EventBridge)

DynamoDB (catalog + event storage)

React frontend on S3 + CloudFront

Observability (CloudWatch dashboards, alarms)

IaC expansion (Terraform for API/Lambda/roles)

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

# create venv
python -m venv .venv             # if 'python' not found, use: py -3 -m venv .venv
source .venv/Scripts/activate    # Windows Git Bash

# install & test
python -m pip install --upgrade pip
python -m pip install -r services/api/requirements.txt
python -m pytest -q

# optional sample data
python data/generators/generate_synthetic.py

flowchart LR
  A[Client / curl] --> B[API Gateway (HTTP API)]
  B --> C[Lambda (Python)]
  C -->|mock today| D[(Mock data)]
  C -.future .-> E[(Amazon Personalize)]
  C -.future .-> F[(DynamoDB)]




