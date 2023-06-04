from datetime import datetime
import sqlite3
import time
import sys
from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule

# send a request to fetch HTML of the page
response = requests.get('https://bitcoin.pl/wiadomosci')

# create the soup object
soup = BeautifulSoup(response.text, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')


def check_head():
  global naglowki
  naglowki = soup.find_all('h2')[0].get_text()
  print (naglowki)
    
  b = 3
  if (b >1):
    send_mail()
  else:
    print("puste")



  

# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('faptribute987@gmail.com', 'tyhuju03')


  body = "Dzisiejsze newsy https://bitcoin.pl/wiadomosci"

  
  msg = MIMEMultipart()
  msg['From'] = 'Paliwo'
  msg['To'] = 'faptribute987@gmail.com'
  msg['Subject']= "Dzisiejsze newsy"
  msg.attach(MIMEText(body, 'plain'))
  
  server.sendmail(
    'sender@gmail.com',
    'faptribute987@gmail.com',
    msg.as_string()
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices

check_head()