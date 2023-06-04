import requests
from bs4 import BeautifulSoup

url = 'https://adsyourself.online/'  # wpisz adres strony

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# znajdź wszystkie linki
links = soup.find_all('a')

# przeszukaj wszystkie linki i wybierz tylko te, które prowadzą do podstron
subpages = []
for link in links:
    href = link.get('href')
    if href and not href.startswith('#') and not href.startswith('http'):
        subpages.append(url + href)

# wydrukuj znalezione podstrony
for subpage in subpages:
    print(subpage)