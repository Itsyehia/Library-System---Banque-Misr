# Variable for User ARNs
variable "user_arns" {
  description = "List of IAM User ARNs allowed to assume the role"  # Description of what this variable is used for
  type        = list(string)  # Type of the variable: a list of strings
  default     = [
    "arn:aws:iam::637423483309:user/yehia",    # ARN for user 'yehia'
    "arn:aws:iam::637423483309:user/yehia-2",  # ARN for user 'yehia-2'
    "arn:aws:iam::637423483309:user/reem"      # ARN for user 'reem'
  ]
}

# Tags Variable
variable "tags" {
  description = "Tags to apply to resources"  # Description of what this variable is used for
  type        = map(string)  # Type of the variable: a map of strings
  default     = {
    Environment = "Production"  # Tag for environment, e.g., Production, Development
    Team        = "Team3-project"  # Tag for the team or project name
  }
}
