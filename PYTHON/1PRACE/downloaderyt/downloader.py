from pytube import YouTube
import sys

yt = YouTube("https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=PLHAfo0kzPsgpicia6C8cqtTBoN9WfNWyg&index=76&t=598s")

print(yt.title)
print(yt.views)
 
yd = yt.streams.get_highest_resolution()

yd.download("D:/PYTHON/1PRACE/downloaderyt")