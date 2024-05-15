# Variables for AWS

variable "aws_region" {
  description = "The AWS region where resources will be deployed"
  type        = string
}

variable "ami_id" {
  description = "The AMI ID for the EC2 instances"
  type        = string
}

variable "instance_type" {
  description = "The type of EC2 instance to deploy"
  type        = string
  default     = "t2.micro"
}

variable "autoscaling_group_name" {
  description = "The name of the Auto Scaling group"
  type        = string
}

variable "min_size" {
  description = "The minimum size of the Auto Scaling group"
  type        = number
  default     = 1
}

variable "max_size" {
  description = "The maximum size of the Auto Scaling group"
  type        = number
  default     = 3
}

variable "desired_capacity" {
  description = "The desired number of instances in the Auto Scaling group"
  type        = number
  default     = 2
}
