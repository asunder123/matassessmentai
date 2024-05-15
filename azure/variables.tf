# Variables for Azure

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure region to deploy the resources"
  type        = string
}

variable "vm_size" {
  description = "The size of the Azure VM instances"
  type        = string
  default     = "Standard_DS1_v2"
}

variable "vmss_name" {
  description = "The name of the VM Scale Set"
  type        = string
}

variable "instance_count" {
  description = "The number of instances to be deployed in the VM Scale Set"
  type        = number
  default     = 2
}