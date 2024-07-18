terraform {
  backend "s3" {
    bucket = "sumonaust-restapi"
    key    = "EKS/terraform.tfstate"
    region = "us-east-1"
  }
}