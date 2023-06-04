import random
import schedule
import time
from instabot import Bot

my_bot = Bot()
#login
my_bot.login(username="ladne.laskiz",  password="tyHuju03")

hashstags = ["#nastolatki", "#polishgirl" , "#polskadziewczyna", "#lady", "#polishmua", "#makeupmafia", "#kalisz", "#muaarmy", "#ladyluck", "#muapl", "#luck", "#kaliszmakeup", "#teen", "#instagood", "#fashion" "#l4l", "#polskiedziewczyny", "#lovemakeup", "#portrait", "#nastolatek", "#like", "#teenager", "#portret", "#polishgirls", "#szkoła", "#poland", "#maciek", "#tiul", "#inspiracja", "poland", "polska","dziewczyna", "kobieta"]


hashstagsrand = random.sample(hashstags, 10)

#zdjecie
def  upload():
    my_bot.upload_photo("1T9CWqN.jpg", caption= "#nastolatki #polishgirl #polskadziewczyna")
    time.sleep(retry)









#schedule.every().day.at("17:00").do(upload)


#while True:
    #schedule.run_pending(upload)
    #time.sleep(5)