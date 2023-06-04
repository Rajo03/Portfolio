import tiktok_scraper

# Set the hashtag to search for
hashtag = 'popular'

# Set the maximum number of videos to download
max_videos = 60

# Set the output folder
output_folder = 'videos'

# Search for TikTok videos by hashtag
videos = tiktok_scraper.hashtag(hashtag)

# Iterate through the videos
for video in videos:
    # Download the TikTok video
    video_data = tiktok_scraper.download(video['url'])
    
    # Check if the download was successful
    if video_data is not None:
        # Get the video's file name
        file_name = video['url'].split('/')[-1] + '.mp4'
        
        # Save the video to the folder
        with open(output_folder + '/' + file_name, 'wb') as video_file:
            video_file.write(video_data)
            
        # Decrement the counter
        max_videos -= 1
        
        # Break if the maximum number of videos has been reached
        if max_videos == 0:
            break
