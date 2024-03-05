 
# Open the file that contains the allow list
import_file = "allow_list.txt"
with open(import_file, "r") as file:
    # Read the file contents
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Iterate through the remove list
remove_list = ["192.168.1.1", "192.168.1.91"]  # Example remove list
for element in remove_list:
    # Remove IP addresses that are on the remove list
    if element in ip_addresses:
        ip_addresses.remove(element)

# Update the file with the revised list of IP addresses
updated_ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(updated_ip_addresses)
