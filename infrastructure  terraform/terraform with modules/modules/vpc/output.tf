output "vpc_id" {
  value = aws_default_vpc.default_vpc.id
}

output "default_az1_id" {
  value = aws_default_subnet.default_az1.id
}
output "default_az2_id" {
  value = aws_default_subnet.default_az2.id
}

output "default_az3_id" {
  value = aws_default_subnet.default_az3.id
}