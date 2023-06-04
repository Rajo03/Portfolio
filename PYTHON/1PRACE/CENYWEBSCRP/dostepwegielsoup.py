from bs4 import BeautifulSoup
import requests


# send a request to fetch HTML of the page
response = requests.get('https://sklep.tauron.pl')

# create the soup object
soup = BeautifulSoup(response.text, 'html.parser')




dostepnosc = soup.find('a',attrs={'href':'https://sklep.tauron.pl'})
print(soup)