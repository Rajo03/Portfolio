import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
download_folder = 'C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\CSV_YOUTUBEDOWN\\export'

playlist = Playlist('https://www.youtube.com/playlist?list=PL2ywZDa0wHjS6uwsAvTFvn8cX-wXOF-Bi')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)




# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    out_file = audioStream.download(output_path=download_folder)
