import csv
import requests
from bs4 import BeautifulSoup

# Open the CSV file
with open('D:\\PROGRAMOWANIE\\PYTHON\\1PRACE\\AFFILIACJA\\photodownload\\zdjecia.csv', 'r') as csv_file:
    # Read the CSV file
    reader = csv.reader(csv_file)
    
    # Iterate through the rows of the CSV file
    for row in reader:
        # Get the page link from the row
        link = row[0]
        
        # Send a request to the page
        response = requests.get(link)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page's HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all the img tags on the page
            img_tags = soup.find_all('img')
            
            # Iterate through the img tags
            for img_tag in img_tags:
                # Get the src attribute of the img tag
                img_src = img_tag['src']
                
                # Send a request to download the image
                img_response = requests.get(img_src)
                
                # Check if the request was successful
                if img_response.status_code == 200:
                    # Get the image's data
                    img_data = img_response.content
                    
                    # Get the image's file name
                    file_name = img_src.split('/')[-1]
                    
                    # Save the image to the folder
                    with open('photos/' + file_name, 'wb') as img_file:
                        img_file.write(img_data)
