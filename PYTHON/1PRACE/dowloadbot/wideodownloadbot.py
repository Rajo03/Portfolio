import csv
import requests

# Open the CSV file
with open('D:\\PROGRAMOWANIE\PYTHON\\1PRACE\dowloadbot\\links2.csv', 'r') as csv_file:
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
            # Get the video's data
            video_data = response.content
            
            # Get the video's file name
            file_name = link.split('/')[-1]
            
            # Save the video to the folder
            with open('videos/' + file_name, 'wb') as video_file:
                video_file.write(video_data)