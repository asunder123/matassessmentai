provider "aws" {
  region = "us-west-2"
}

resource "aws_launch_configuration" "example" {
  name          = "terraform-example-config"
  image_id      = "ami-0c55b159cbfafe1f0" # Update this to your desired AMI ID
  instance_type = "t2.micro"

  # Other launch configuration settings
}

resource "aws_autoscaling_group" "example" {
  launch_configuration = aws_launch_configuration.example.id
  min_size             = 3
  max_size             = 6

  # Other Auto Scaling group configuration

  tags = {
    environment = "dev"
  }
}
