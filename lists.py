# List of EC2 instance
instance_ids = ["i-1234", "i-5678", "i-9012"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
                
# List of availability zones in a region
availbility_zones = ["us-west-1a", "us-west-2a", "us-west-2c"]

# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"First IP addresses: {ip_addresses}")
print(f"Number of AZs: {availbility_zones}")


#Add new EC2 instance ID
instance_ids.append("i-3456")
print("After adding a new instance ID")
print("EC2 Instance:", instance_ids)