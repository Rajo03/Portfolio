import csv

input_file = 'C:\\PROGRAMOWANIE\\PYTHON\\PROjekty\\input.csv'
output_file = 'C:\\PROGRAMOWANIE\\PYTHON\\PROjekty\\output.csv'

# Open the input CSV file and read the links
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    links = [row[0] for row in reader]

# Add 'https://' to any links that don't already have it
for i in range(len(links)):
    if not links[i].startswith('https://'):
        links[i] = 'https://' + links[i]

# Write the updated links to the output CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for link in links:
        writer.writerow([link])
print("gotowe")