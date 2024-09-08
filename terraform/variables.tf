# Variable for User ARNs
variable "user_arns" {
  description = "List of IAM User ARNs allowed to assume the role"
  type        = list(string)
  default     = [
    "arn:aws:iam::637423483309:user/yehia",
    "arn:aws:iam::637423483309:user/yehia-2",
    "arn:aws:iam::637423483309:user/reem"
  ]
}

# Tags Variable
variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {
    Environment = "Production"
    Team        = "Team3-project"
  }
}