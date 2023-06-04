from types import NoneType
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule

# send a request to fetch HTML of the page
response = requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/slaskie/')

# create the soup object
soup = BeautifulSoup(response.text, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')



def check_price():
  benzyna_95 = "benzyna"
  price = soup.find('div',attrs={'class':'price'})
  cena_paliwa = "6,89"
  converted_price = price.text
  usuwanie = converted_price.strip()
  usuwanie2 =  usuwanie.replace("zł", "")
  print (usuwanie2)
  if usuwanie2 <= cena_paliwa:
    print("True")
    send_mail()
  else:
    print("False")
  

  #using strip to remove extra spaces in the title
  print(benzyna_95.strip())





# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('faptribute987@gmail.com', 'tyhuju03')


  body = "Cena paliwa spadła na   https://www.autocentrum.pl/paliwa/ceny-paliw/slaskie/ "

  
  msg = MIMEMultipart()
  msg['From'] = 'Paliwo'
  msg['To'] = 'faptribute987@gmail.com'
  msg['Subject']= "Cena paliwa spadła"
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

#schedule.every().day.at("15:23").do(check_price)
check_price()
