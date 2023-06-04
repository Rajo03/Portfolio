import random
import requests
import config

#GENERATORZDAN

przymiotnik = ["Seksi", "Seksowna", "Poznajcie",  "Poznajcie piękną", "Przepiękna", "Urocza", "Piękna", "Ładna", "Atrakcyjna", "Wyjątkowa", "Niegrzeczna"]
imie = ["Olimpia","Jola","Klara","Bogna","Magdalena","Lila","Nina","Matylda","Klementyna","Jola","Balbina","Paula","Maria","Eliza","Józefa","Maria","Róża","Oksana,""Kaja","Felicja","Justyna","Regina","Jagoda","Patrycja","Honorata","Daria","Florentyna","Bogna","Marzanna","Nina","Maja","Alice","Ada","Izyda","Franciszka","Danuta","Iga","Wanda","Judyta","Matylda","Arleta","Amalia","Jowita","Alana","Alice","Bianka","Bogna","Paulina","Dagmara",]

przedlink = ["Wpadnij na","Spotykaj takie dziewczyny na","Najlepszy portal randkowy","Najlepszy portal","Umów się na randke na","Najlepszy portal randkowy w polsce!","Czeka ona na was na stronie","Poznawajcie kobiety na","Zakładajcie darmowe konta i randkujcie! na","Wpadajcie i zakładajcie darmowe konto!","Zakładajcie konto za darmo 😀na","Założ darmowe konto i zacznij pisać na","Znajdź wymarzoną kobietę 😈 na","Załóż darmowe konto i zacznij spotkania na","Kontakt z panią przez","Znajdź kontakt do wymarzonej kobiety 🔥na","Zapraszam na","Zobacz mnie na żywo na"]
link = ["https://fap-world.live"]#/category/randkionline"]
reszta = ["i umów się ❤ To nic skomplikowanego 🥰", "nowy portal ❤ Znajdź kontakt do wymarzonej kobiety 🔥", "wejdź i działaj ❤ Nie pozwól żeby ktoś Cię wyprzedził 😎"," i działaj 😎🤩 To jest twój dzień! 🥰", "i poznaj się bliżej z tą śliczną kobietą ❤","Sprawdź jakiego faceta szuka ta piękna kobieta. ❤"," i umów się w kilka chwil 😎 Nie trać więcej czasu! 😈", "i poznaj prawdziwą kobiete marzeń ❤ Trzymamy za Was kciuki ❤", "  i umów się z kobietą marzeń 😈🍒 Na co jeszcze czekasz? Aż ktoś Cię wyprzedzi?..", " i działaj bo szkoda czasu 😲 Zajmuje to tylko kilka sekund a sprawi Ci wieeele radości ❤", "Chyba nie chcesz zmarnować kolejnego weekendu? ❤", "Nie masz nic do stracenia, możesz tylko zyskać ❤", "i baw się dobrze ❤  Zacznij żyć pełnią życia 😎💋"]





przy = random.sample(przymiotnik, 1)
imie2 = random.sample(imie, 1)
przedlink2 = random.sample(przedlink, 1)

msg = *przy,*imie2,*przedlink2,*link, sep=" "



#FACEBOOK_API


page_id = "111827098200870"

post_url = 'https://graph.facebook.com/111827098200870/{}/feed'.format(config.page_id_1)
                                                                     

payload = {
  'message':msg,
  'access_token': config.facebook_access_token_1
}

r = requests.post(post_url, data=payload)
print(r.text)


image_url = .format{page_id}
image_location = ""
img_payload = {
'url': image_location,
'access_token': config.facebook_access_token
  }

r = requests.post(image_url, data=img_payload)
print(r.text)





















#HARMONOGRAM

#schedule.every().day.at("17:00").do(upload)


#while True:
    #schedule.run_pending(upload)
    #time.sleep(5)