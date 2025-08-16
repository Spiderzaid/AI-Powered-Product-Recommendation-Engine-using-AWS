
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Example: S3 bucket for data lake
resource "aws_s3_bucket" "datalake" {
  bucket = var.data_lake_bucket
  force_destroy = true
}

output "data_lake_bucket" {
  value = aws_s3_bucket.datalake.bucket
}
