
# AI-Powered Product Recommendation Engine (AWS)

An end-to-end, **production-style** recommendation engine that delivers personalized and related-item recommendations using **AWS** services. It includes **data ingestion**, **ETL**, **modeling** (Amazon Personalize by default), **real-time APIs** (API Gateway + Lambda), **batch inference**, **IaC**, **CI/CD**, and **observability**.

> Portfolio-ready project you can deploy and demo. Use this repo to showcase cloud, ML, and systems design skills.

## Architecture

```mermaid
flowchart LR
  A[Web/App Events] -->|Kinesis| B[Firehose]
  B --> C[S3 Data Lake]
  D[Catalog Dump] --> C
  C --> E[Glue ETL/Curated]
  E --> F[(Amazon Personalize)]
  F --> G{Serving}
  G -->|Real-time| H[API Gateway → Lambda → Campaign/Endpoint]
  G -->|Batch| I[Batch Recommendations in S3]
  H --> J[Frontend (S3 + CloudFront)]

  subgraph Ops
  K[Step Functions: nightly import/retrain/deploy]
  L[CloudWatch + Model Monitor + QuickSight]
  end
```

### Key AWS components
- **Kinesis / Firehose → S3** for clickstream ingestion
- **AWS Glue / PySpark** for ETL & curation (parquet)
- **Amazon Personalize** for fast-to-prod recommendations (switchable to SageMaker)
- **API Gateway + Lambda** for real-time APIs
- **Step Functions** for orchestration (import/retrain/batch)
- **CloudWatch** for logs/alarms; **QuickSight** dashboards
- **S3 + CloudFront** for optional SPA frontend hosting
- **Terraform** for Infrastructure-as-Code
- **GitHub Actions** for CI/CD

---

## Getting started (local)

### 1) Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r services/api/requirements.txt
```

### 2) Generate sample data
```bash
python data/generators/generate_synthetic.py
```
This writes `data/sample_catalog.csv` and small interaction files to `data/`.

### 3) Run unit tests (API layer)
```bash
pytest -q
```

---

## AWS Deploy (high level)

> You need an AWS account and AWS CLI configured (`aws configure`).

1. **Provision core infra** (VPC optional for this starter):  
   - Edit `infra/terraform/variables.tf` and `terraform.tfvars` (create one) with your values.  
   - Initialize & apply:
     ```bash
     cd infra/terraform
     terraform init
     terraform apply
     ```

2. **Create a Personalize dataset group** and import data (manual or CLI). See `model/personalize/README.md` (to be added) for detailed commands.

3. **Deploy API** (Lambda + API Gateway):  
   - Package Lambda:
     ```bash
     cd services/api
     pip install -r requirements.txt -t lambda/
     cd lambda && zip -r ../lambda.zip . && cd ..
     ```
   - Use Terraform modules or AWS SAM/Serverless Framework (future enhancement). As a simple start, upload `lambda.zip` to a Lambda function in the console and connect it to API Gateway.

4. **(Optional) Frontend**: host a SPA on S3 + CloudFront and point it to your API endpoints.

---

## API (OpenAPI excerpt)

- `GET /recommendations/personalized?userId=U123&k=10`
- `GET /recommendations/related?itemId=I456&k=10`
- `POST /events` (records user events; mock in this starter)

Full spec: `services/api/openapi.yaml`

---

## Repo structure

```
ai-reco-engine-aws/
├─ infra/
│  └─ terraform/
│     ├─ main.tf
│     ├─ variables.tf
│     └─ outputs.tf
├─ services/
│  └─ api/
│     ├─ lambda/
│     │  ├─ app.py
│     │  └─ util.py
│     ├─ requirements.txt
│     ├─ openapi.yaml
│     └─ tests/
│        └─ test_api.py
├─ pipelines/
│  └─ glue_jobs/
│     └─ README.md
├─ data/
│  ├─ sample_catalog.csv
│  └─ generators/
│     └─ generate_synthetic.py
├─ .github/
│  └─ workflows/
│     └─ cicd.yml
├─ .gitignore
└─ README.md
```

---

## Resume bullets (paste-ready)

- Built an **AI-powered product recommendation engine** on AWS delivering **low-latency** results via **API Gateway + Lambda + Amazon Personalize**, with automated nightly refresh using **Step Functions**.
- Designed a **streaming data pipeline** (Kinesis → Firehose → S3 → Glue) and **batch top‑N** generation stored in S3 for downstream consumption.
- Implemented **IaC** with Terraform and **CI/CD** with GitHub Actions; added **CloudWatch** dashboards and alarms for **SLOs** (latency, error rate).

> Replace numbers with your actual test results (e.g., p95 latency, CTR uplift from an A/B demo).

---

## License
MIT
