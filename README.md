# AI-Powered Product Recommendation Engine (AWS)

An **AI-powered product recommendation system** built using **Amazon Personalize**, AWS Lambda, API Gateway, DynamoDB, and CloudFront.  
This project demonstrates how to build a **serverless, scalable, and low-latency** recommendation engine capable of delivering **personalized product suggestions in real time**.

---

## 🚀 Features
- **Personalized Recommendations** using Amazon Personalize
- **Serverless APIs** with AWS Lambda & API Gateway
- **Low Latency (<150ms p95)** responses
- **Product Catalog Management** via DynamoDB
- **Event Tracking** for user clicks, views, and purchases
- **Weekly Model Retraining** via AWS EventBridge
- **React Frontend** hosted on S3 + CloudFront

---

## 🛠 Tech Stack
**AWS Services**
- Amazon Personalize (ML Model Training & Inference)
- Lambda (Backend Functions)
- API Gateway (REST API)
- DynamoDB (Product & Event Storage)
- S3 (Data Storage & Static Website Hosting)
- EventBridge (Automated Retraining Schedule)
- CloudFront (Content Delivery)
- IAM (Secure Access Management)
- CloudWatch (Monitoring & Logging)

**Languages & Tools**
- Python (Lambda Functions)
- React (Frontend UI)
- Terraform (Infrastructure as Code)
- Draw.io (Architecture Diagrams)
## 🗺 Architecture Diagram
![Architecture Diagram](Architecture.png)

## 🛠 Tech Stack
- **AWS Personalize** – Machine learning for personalized recommendations
- **AWS Lambda** – Backend serverless functions
- **API Gateway** – REST API for client-server communication
- **DynamoDB** – NoSQL database for products and user events
- **S3 + CloudFront** – Static hosting & CDN for React frontend
- **React** – Frontend application
- **EventBridge** – Model retraining scheduler

---

## 🚀 How It Works
1. User opens the frontend (S3 + CloudFront).
2. API Gateway sends requests to AWS Lambda.
3. Lambda retrieves data from DynamoDB and AWS Personalize.
4. Recommendations are returned to the frontend.
5. User activity events are stored in DynamoDB for future model retraining.

---

## 📦 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AnuhyaPachika/AI-Powered-Product-Recommendation-Engine-using-AWS.git



---

## 📂 Project Structure
## 📂 Project Structure
.
├── README.md                # Documentation
├── architecture.png         # Architecture diagram
├── Welcome file.md          # Detailed project intro
├── LICENSE                  # License info
├── architecture.drawio.png  # Source diagram file


 


