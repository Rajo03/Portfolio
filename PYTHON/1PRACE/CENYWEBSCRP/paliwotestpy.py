from datetime import datetime
import sqlite3
import time
import sys
from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart

try:
    page = requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/slaskie/') #ceny
    page2 = requests.get('https://www.e-petrol.pl/notowania/rynek-krajowy/hurt') #hurt_ceny
    page3 = requests.get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ROPA')
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('error')
    print (error_type, 'line', error_info.tb_lineo)
    
time.sleep(1)

soup = BeautifulSoup(page.text,'html.parser')
soup2 = BeautifulSoup(page2.text,'html.parser')
soup3 = BeautifulSoup(page3.text,'html.parser')

#cena w zł na śląsku
benzyna_95 = soup.find('div',attrs={'class':'price'})
diesiel = soup.find('a',attrs={'href':'/paliwa/ceny-paliw/slaskie/on/'})

#hurtowe ceny benzyny95
hurt_95 = soup2.find("div",  text=" Pb 95")
hurt_95_cena = soup2.find('div',attrs={'class':'col pb95'})

#hurtowe ceny diesiel
hurt_ON = soup2.find("div",  text=" ON")
hurt_ON_cena = soup2.find('div',attrs={'class':'col one'})

#ceny ropy
Ropa = soup3.find('div',attrs={'class':'profilLast'})

#CENY PALIWA I CENY HURTOWE
print("Benzyna95\n",benzyna_95.text)
print("Diesiel\n",diesiel.text)
print("HurtoweCeny\n",  hurt_95.text, hurt_95_cena.text,  "zł/m3")

print(hurt_ON.text,"-", hurt_ON_cena.text, "zł/m3")

print(Ropa.text)


#BAZA DANYCH

conn = sqlite3.connect('cenypaliwo.db')

c = conn.cursor()

#c.execute(' ' ' CREATE TABLE paliwodiesel (rodzaj TEXT, cena TEXT, data TEXT) ' ' ')

#TABELA DIESEL
rodzaj = 'Diesel'
cena = diesiel.text
data = datetime.now()
#c.execute(' ' ' INSERT INTO  paliwodiesel VALUES (?, ?,?) ' ' ',  (rodzaj, cena, data))

#TABELA BENZYNA
rodzaj2 = 'Benzyna95'
cena2 = benzyna_95.text
data2 = datetime.now()
#c.execute(' ' ' INSERT INTO  paliwo95 VALUES (?, ?,?) ' ' ',  (rodzaj2, cena2, data2))






#c.execute(' ' ' DELETE FROM paliwo95 WHERE rodzaj=Diesel ;' ' ')
conn.commit()

tytul = 'Benzyna'
price = benzyna_95.text
print(price)

print(tytul.strip())

s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()
s.starttls()
s.ehlo()
s.login('faptribute987@gmail.com', 'tyhuju03')

subject = 'Cena benzyny spadla!'
body = "Sprawdz cene https://www.autocentrum.pl/paliwa/ceny-paliw/slaskie/ "



msg = MIMEMultipart()
msg['From'] = 'Paliwo'
msg['To'] = 'faptribute987@gmail.com'
msg['Subject']= subject

s.sendmail("example@gmail.com",
           "faptribute987@gmail.com",
           body)
s.quit()