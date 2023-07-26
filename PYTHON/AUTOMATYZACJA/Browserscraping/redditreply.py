import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID", 
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

subreddit = reddit.subreddit("glassblowing")


for post in subreddit.new():
  current_time = datetime.utcnow()
  post_time = datetime.utcfromtimestamp(post.created)
  delta_time = current_time - post_time
  if delta_time <= timedelta(hours=48):
    if "christmas" in post.title.lower():
      # print(post.title)
      # post.reply('Hey, Christmas is coming!')
      for comment in post.comments:
        if "is coming" in comment.body.lower():
          comment.reply("Yeah, it's coming")