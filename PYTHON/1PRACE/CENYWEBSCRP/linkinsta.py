from bs4 import BeautifulSoup

import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule

# send a request to fetch HTML of the page
response = requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/slaskie/')

# create the soup object
soup = BeautifulSoup(response.text, 'html.parser')