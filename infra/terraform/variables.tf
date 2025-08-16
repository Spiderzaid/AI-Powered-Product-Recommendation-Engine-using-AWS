
variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}

variable "data_lake_bucket" {
  type        = string
  description = "S3 bucket name for data lake"
}
