from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
#strona z której chcemy sciągnac zdjęcia
page = requests.get('https://theviraler.com/24-year-old-actress-and-model-madelyn-cline-in-sexy-swimsuits-40-photos/')



soup = BeautifulSoup(page.content,'html.parser')
search = soup.find_all("img")
search = search[3:-1]

#pobieranie zdjec
for img in tqdm(search):
    imglinks = img.attrs.get("src")
    image = requests.get(imglinks).content
    #FIXME: sciezka zapisu
    filename = r"S:\wykop\FapWorld" + imglinks[imglinks.rfind("/"):] #katalog do którego maja trafic zdjecia
    with open(filename, "w") as file:
         file.write(image)