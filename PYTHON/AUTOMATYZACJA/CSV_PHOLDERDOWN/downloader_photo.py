import csv
import requests
import os
from bs4 import BeautifulSoup

# Open the CSV file and read the links
with open('C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_PHOLDERDOWN\\links.csv', 'r') as file:
    reader = csv.reader(file)
    links = [row[0] for row in reader]

# Create a folder to store the images
if not os.path.exists('C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_PHOLDERDOWN\\export'):
    os.makedirs('export')

# Iterate through the links
for link in links:
    # Open the link and parse the HTML
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

images = soup.find_all('img')
    # Iterate through the images
for image in images:
    # Download the image and save it to the folder
    response = requests.get(image['src'], stream=True)
    filename = image['src'].split('/')[-1]
    with open(f'C://PROGRAMOWANIE\PYTHON//AUTOMATYZACJA//CSV_PHOLDERDOWN//export/{filename}', 'wb') as out_file:
        out_file.write(response.content)
