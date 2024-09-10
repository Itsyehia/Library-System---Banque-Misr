# Create a VPC
resource "aws_vpc" "Team3" {
  cidr_block           = "10.0.0.0/16"   # IP address range for the VPC
  enable_dns_support   = true            # Enable DNS resolution
  enable_dns_hostnames = true            # Enable DNS hostnames for instances

  tags = {
    Name = "Team3-vpc"  # Tag for identifying the VPC
  }
}

# Create a public subnet
resource "aws_subnet" "team3_first_subnet" {
  vpc_id                  = aws_vpc.Team3.id  # VPC ID to associate the subnet with
  cidr_block              = "10.0.1.0/24"     # IP address range for the subnet
  availability_zone       = "us-west-2a"      # Availability zone for the subnet
  map_public_ip_on_launch = true              # Automatically assign public IPs to instances in this subnet

  tags = {
    Name = "team3-subnet"  # Tag for identifying the subnet
  }
}

# Create a private subnet
resource "aws_subnet" "team3_second_subnet" {
  vpc_id                  = aws_vpc.Team3.id  # VPC ID to associate the subnet with
  cidr_block              = "10.0.2.0/24"     # IP address range for the subnet
  availability_zone       = "us-west-2b"      # Availability zone for the subnet
  map_public_ip_on_launch = true              # Automatically assign public IPs to instances in this subnet

  tags = {
    Name = "team3-subnet"  # Tag for identifying the subnet
  }
}

# Create an internet gateway
resource "aws_internet_gateway" "Team3" {
  vpc_id = aws_vpc.Team3.id  # VPC ID to attach the internet gateway to

  tags = {
    Name = "team3-gateway"  # Tag for identifying the internet gateway
  }
}

# Create a route table for the public subnet
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.Team3.id  # VPC ID to associate the route table with

  route {
    cidr_block = "0.0.0.0/0"  # Route all traffic to the internet
    gateway_id = aws_internet_gateway.Team3.id  # Internet gateway ID
  }

  tags = {
    Name = "public-route-table"  # Tag for identifying the route table
  }
}

# Associate the route table with the public subnet
resource "aws_route_table_association" "public_subnet" {
  subnet_id      = aws_subnet.team3_first_subnet.id  # Subnet ID to associate with the route table
  route_table_id = aws_route_table.public.id          # Route table ID
}

# Create an Elastic IP for the NAT Gateway
resource "aws_eip" "nat" {
  domain = "vpc"  # Indicates that the Elastic IP is for use with a VPC
}

# Create a NAT Gateway
resource "aws_nat_gateway" "Team3" {
  allocation_id = aws_eip.nat.id  # Elastic IP allocation ID
  subnet_id     = aws_subnet.team3_first_subnet.id  # Subnet ID to place the NAT gateway in

  tags = {
    Name = "team3-nat-gateway"  # Tag for identifying the NAT gateway
  }
}

# Create a route table for the private subnet
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.Team3.id  # VPC ID to associate the route table with

  route {
    cidr_block     = "0.0.0.0/0"  # Route all traffic to the NAT gateway
    nat_gateway_id = aws_nat_gateway.Team3.id  # NAT gateway ID
  }

  tags = {
    Name = "private-route-table"  # Tag for identifying the route table
  }
}

# Associate the route table with the private subnet
resource "aws_route_table_association" "private_subnet" {
  subnet_id      = aws_subnet.team3_second_subnet.id  # Subnet ID to associate with the route table
  route_table_id = aws_route_table.private.id          # Route table ID
}
