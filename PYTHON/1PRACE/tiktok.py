import csv
import requests
from bs4 import BeautifulSoup

# Open the CSV file containing website links
with open('C:\\PROGRAMOWANIE\\PYTHON\\PROjekty\\nowiklienci.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Open a new CSV file to write the results
    with open('C:\\PROGRAMOWANIE\\PYTHON\\PROjekty\\social_media_links.csv', 'w', newline='') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(['Website Link', 'TikTok Link', 'Instagram Link'])
        # Iterate over each row in the CSV file
        for row in csvreader:
            website_link = row[0]
            # Make a GET request to the website
            response = requests.get(website_link)
            # Parse the HTML content of the website using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all <a> tags on the website
            links = soup.find_all('a')
            tiktok_link = None
            instagram_link = None
            # Iterate over each <a> tag to find TikTok and Instagram links
            for link in links:
                href = link.get('href')
                if href is not None:
                    # Check if the <a> tag contains a TikTok link
                    if 'tiktok.com' in href:
                        tiktok_link = href
                    # Check if the <a> tag contains an Instagram link
                    elif 'instagram.com' in href:
                        instagram_link = href
            # Write the results to the output CSV file
            csvwriter.writerow([website_link, tiktok_link, instagram_link])
            
print("gotowe")