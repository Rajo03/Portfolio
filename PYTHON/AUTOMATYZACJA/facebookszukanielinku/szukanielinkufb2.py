import csv
import requests
from bs4 import BeautifulSoup

# Funkcja do przeszukiwania strony w poszukiwaniu linka do Facebooka
def find_facebook_link(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Szukamy elementu <a> z atrybutem class="facebook-link"
        facebook_link = soup.find('a', class_='facebook-link')
        if facebook_link:
            return facebook_link['href']
        else:
            return 'Brak linka do Facebooka'
    except Exception as e:
        print(f'Błąd podczas przeszukiwania strony {url}: {e}')
        return 'Błąd'

# Otwieramy plik CSV z linkami wejściowymi
input_file = 'C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\facebookszukanielinku\\input2.csv'
output_file = 'C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\facebookszukanielinku\\output2.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Otwieramy plik CSV do zapisu wyników
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    for row in rows:
        link = row[0]  # Zakładamy, że linki są w pierwszej kolumnie CSV
        facebook_link = find_facebook_link(link)
        writer.writerow([link, facebook_link])

print('Przeszukiwanie zakończone. Wyniki zapisane w pliku', output_file)