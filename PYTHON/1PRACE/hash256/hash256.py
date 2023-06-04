import hashlib

# Open the file in binary mode
with open('file.txt', 'rb') as file:
    # Read the contents of the file
    data = file.read()
    
    # Calculate the hash of the data
    hash = hashlib.sha256(data).hexdigest()
    
    # Print the hash
    print(hash)
