import csv
import os
from pytube import YouTube

# Example usage
csv_file = "C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\ytdownload\\link.csv"
output_folder = "C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\ytdownload\\filmyyt"

# Function to download a YouTube video
def download_video(url, output_folder, filename):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video
        video = yt.streams.get_highest_resolution()

        # Set the output path
        output_path = os.path.join(output_folder, filename)

        # Download the video
        video.download(output_path)
        print(f"Video downloaded successfully: {filename}")

    except Exception as e:
        print("An error occurred while downloading the video:", str(e))

# Function to process the CSV file and download videos
def download_videos_from_csv(csv_file, output_folder):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for index, row in enumerate(reader, start=1):
            video_url = row[0]  # Assuming the URL is in the first column of the CSV
            filename = f"video_{index}.mp4"  # Generate sequential filenames

            # Download the video to the output folder
            download_video(video_url, output_folder, filename)

download_videos_from_csv(csv_file, output_folder)