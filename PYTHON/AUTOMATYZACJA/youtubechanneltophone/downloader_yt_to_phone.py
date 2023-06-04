import os
import datetime
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.errors
from googleapiclient.discovery import build
from pytube import YouTube

# Enter your Google API credentials and channel id here
client_id = '148057720598-9tk0b87k7vpcr5cd4ra714kmu979ucs7.apps.googleusercontent.com'
client_secret = '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'
api_key = 'AIzaSyDjMTXu2a7Rbvf7FdOBcGjmdPl-Z8iO0Gc'
channel_id = 'UCNvSk-U6X9mOJHr7wz_xCWw'

# Set the date to check for new videos
check_date = datetime.datetime(2022, 4, 19, 0, 0, 0)  # format: YYYY, MM, DD, HH, MM, SS

# Set up the YouTube Data API client
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json", scopes)
creds = flow.run_local_server(port=0)

# Build the YouTube Data API client
youtube = build("youtube", "v3", credentials=creds)

# Get the latest video from the channel
request = youtube.search().list(
    part="id",
    channelId=channel_id,
    order="date",
    type="video",
    maxResults=1,
    key=api_key
)
response = request.execute()
video_id = response['items'][0]['id']['videoId']

# Get the upload date of the latest video
request = youtube.videos().list(
    part="snippet",
    id=video_id,
    key=api_key
)
response = request.execute()
upload_date_str = response['items'][0]['snippet']['publishedAt'][:-5]
upload_date = datetime.datetime.strptime(upload_date_str, '%Y-%m-%dT%H:%M:%S')

# Compare the upload date of the latest video to the check date
if upload_date > check_date:
    # Download the video to a file
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path='.', filename=f"{video_id}.mp4")
    print("Video downloaded.")
else:
    print("No new video found.")