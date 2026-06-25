# List of EC2 instance
instance_ids = ["i-1234", "i-5678", "i-9012"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
                
# List of availability zones in a region
availbility_zones = ["us-west-1a", "us-west-2a", "us-west-2c"]

# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"First IP addresses: {ip_addresses}")
print(f"Number of AZs: {availbility_zones}")


# #Add new EC2 instance ID
instance_ids.append("i-3456")
print("After adding a new instance ID")
print("EC2 Instance:", instance_ids)


# # Remove EC instance ID
instance_ids.remove('i-1234')
print("After removing and instance")
print("EC2 instances:", instance_ids)


# Check if an item is in a list
if "10.0.0.4" in ip_addresses:
  print("Yes 10.0.0.4 is in and allowed")
else:
  print("No 10.0.0.4 is not in the allowed list")
print("IP addresses:", ip_addresses)


# Slicing a List
# # First two AZ 
first_two_azs = availbility_zones [:4]
print("First tow Azs:", first_two_azs)

 
# Sorting
instance_ids.sort()
print("Storted EC2 Instances", instance_ids)

# Finding length of a list
number_of_ips = len(ip_addresses)
print(f"Number of IP addresses: {number_of_ips}")


# Acessing list of Items by Index
first_az =availbility_zones[0]
last_az = availbility_zones[1]
print(f"First Az:", first_az)
print(f"Last Az:", last_az)



