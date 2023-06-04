import cv2
import os
import random

# Set the output video's width and height
output_width = 1920
output_height = 1080

# Set the length of the output video in seconds
output_length = 60

# Set the frame rate of the output video
frame_rate = 30.0

# Set the input folder
input_folder = 'videos'

# Get the list of video files in the input folder
video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

# Shuffle the list of video files
random.shuffle(video_files)

# Open a writer for the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output.mp4', fourcc, frame_rate, (output_width, output_height))

# Set the counter for the number of frames written
frame_count = 0

# Iterate through the input videos
for input_video in video_files:
    # Open the input video
    video = cv2.VideoCapture(input_folder + '/' + input_video)
    
    # Iterate through the frames of the input video
    while video.isOpened():
        # Read the next frame
        success, frame = video.read()
        if not success:
            break
            
        # Write the frame to the output video
        output_video.write(frame)
        
        # Increment the counter
        frame_count += 1
        
        # Break if the maximum number of frames has been reached
        if frame_count == output_length * frame_rate:
            break
    
    # Release the video object
    video.release()

# Release the video writer object
output_video.release()
