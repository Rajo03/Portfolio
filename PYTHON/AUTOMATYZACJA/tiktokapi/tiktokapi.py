from TikTokApi import TikTokApi

verifyFp = "verify_l56hp6pe_l7fkxRJj_mWVa_4igS_9AQZ_31fZYpQURzHS"

api = TikTokApi()


count = 5


viral = api.hashtag(name="viral")

print(viral.info_full)






#pobieranie
"""
def pobieranie():
 for video in api.hashtag(name='viral').videos():
  video_bytes = video.bytes()
  

 with open("viral.mp4", "wb") as out:
  out.write(video_bytes)

  
while True:
  pobieranie()
"""