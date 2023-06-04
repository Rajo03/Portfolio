import csv
import os
import requests
import uuid

# specify the folder to save the images
save_folder = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_PHOLDERDOWN\\export"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# open the CSV file
with open("C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_PHOLDERDOWN\\links.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        url = row[0]
        response = requests.get(url)
        filename = os.path.join(save_folder, str(uuid.uuid4()) + ".jpg")
        open(filename, "wb").write(response.content)
        print("{} downloaded!".format(filename))
