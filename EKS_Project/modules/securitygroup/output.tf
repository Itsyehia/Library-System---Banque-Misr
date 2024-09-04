output "ec2_security_group_id" {
 value = aws_security_group.ec2_security_group.id
}

output "ec2_security_group_arn" {
 value = aws_security_group.ec2_security_group.arn
}