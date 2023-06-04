import cv2
import os

# Define the input and output folders
input_folder = 'C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\FOLDER_RESIZE_TO_1080X1920\\import'
output_folder = 'C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\FOLDER_RESIZE_TO_1080X1920\\export'

# Define the target aspect ratio
target_aspect_ratio = 9/16

# Loop through all files in the input folder
for file in os.listdir(input_folder):
    # Check if the file is a video file
    if file.endswith(".mp4"):
        # Open the video file
        video = cv2.VideoCapture(input_folder + '/' + file)

        # Get the frames per second (fps) of the video
        fps = video.get(cv2.CAP_PROP_FPS)

        # Get the width and height of the frames
        frame_width = int(video.get(3))
        frame_height = int(video.get(4))

        # Calculate the aspect ratio
        aspect_ratio = frame_width / frame_height
        if aspect_ratio > target_aspect_ratio:
            new_width = 1080
            new_height = int(new_width / target_aspect_ratio)
        else:
            new_height = 1920
            new_width = int(new_height * target_aspect_ratio)
        
        # Define the codec and create a video writer object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_folder + '/' + file, fourcc, fps, (new_width, new_height))

        # Loop through the frames of the video
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                # Resize the frame
                frame = cv2.resize(frame, (new_width, new_height))

                # Write the frame to the output video
                out.write(frame)

                # Display the frame
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release the video and writer objects
        video.release()
        out.release()

# Close all windows
cv2.destroyAllWindows()