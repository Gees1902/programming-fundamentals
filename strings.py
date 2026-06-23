# Single quotes
single_quoted_string = 'This is an EC2'

# Double quotes
double_quoted_string = "This is also an S3 bucket"

#Triple quotes for multi-line strings
multi_line_string = """
This is a CloudFormation template.
Which has multiple lines


"""


print(single_quoted_string)
print(double_quoted_string)
print(multi_line_string)

# Exercise
# Create a single-line string for an AWS region
aws_region = "us-west-2"

# double quoted string for an ec2 instance type
ec2_instance_type = "t2.micro"

# Triple quotes for multi-line strings
iam_policy = """
{
    "Version": "2012-10-17"
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3::wxample-bucket"
        {    
    ]
}   
"""
#Print all three strings    
print(aws_region)
print(ec2_instance_type)
print(iam_policy)

# Create a multi-line string that contains the following text: