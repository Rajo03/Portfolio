import tiktok_downloader
import csv

# Open the CSV file
with open('D:\\PROGRAMOWANIE\PYTHON\\1PRACE\dowloadbot\\links2.csv', 'r') as csv_file:
    # Read the CSV file
    reader = csv.reader(csv_file)
    
    # Iterate through the rows of the CSV file
    for row in reader:
        # Get the TikTok link from the row
        link = row[0]
        
        # Download the TikTok video
        video_data = tiktok_downloader.download(link)
        
        # Check if the download was successful
        if video_data is not None:
            # Get the video's file name
            file_name = link.split('/')[-1] + '.mp4'
            
            # Save the video to the folder
            with open('videos/' + file_name, 'wb') as video_file:
                video_file.write(video_data)
