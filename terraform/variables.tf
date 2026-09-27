variable "aws_region" {
  description = "AWS region for the infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "ultimate-devops-local"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "ultimate-devops-cluster"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet"
  type        = string
  default     = "10.0.2.0/24"
}

variable "availability_zone" {
  description = "Availability zone for the subnets"
  type        = string
  default     = "ap-south-1a"
}

variable "eks_role_arn" {
  description = "IAM role ARN used by the EKS cluster"
  type        = string
  default     = "arn:aws:iam::123456789012:role/ultimate-devops-eks-role"
}