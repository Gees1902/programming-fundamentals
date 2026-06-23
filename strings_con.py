# Define the AWS account ID
account_id = "123456789012"

# Define the project name
project_name = "cloud_project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + '_' + project_name +"-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")



# Excercise EC2 String Concatenation

# Environment name prod, dev, staging
environment =  'dev'

# Application name
application = 'appserver'

# Instance number
instance_number = "02"
# Concatenate
instance_name = environment + "_" + application  + "-instance-" + instance_number
# Print
print("EC2 instance_name: " + instance_name)



