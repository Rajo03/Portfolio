import os
import pytube
from moviepy.video.io.VideoFileClip import VideoFileClip

# define the playlist url and output folder
playlist_link = 'https://www.youtube.com/playlist?list=PL2ywZDa0wHjS6uwsAvTFvn8cX-wXOF-Bi'
download_dir = 'C:\\Users\\kubak\\Music'


# create directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# initialize PyTube object with playlist link
playlist = pytube.Playlist(playlist_link)

# iterate through videos in playlist
for video in playlist.videos:
    # download video to download directory
    video.streams.get_audio_only().download(output_path=download_dir)

# iterate through downloaded videos in download directory
for file in os.listdir(download_dir):
    # check if file is a video file
    if file.endswith(".mp4"):
        # get video file path
        video_path = os.path.join(download_dir, file)
        
        # get mp3 file path
        mp3_path = os.path.join(download_dir, os.path.splitext(file)[0] + ".mp3")
        
        # convert video to mp3
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(mp3_path)
        
        # delete video file
        os.remove(video_path)
