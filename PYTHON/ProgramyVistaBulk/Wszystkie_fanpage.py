import xlsxwriter
import datetime
import pandas as pd
import os
import requests
import random
from PIL import Image

#TODO:przerobić wszystkie funkcje na wspólne


#tablice do tworzenia zdań,opisu posta
imiona = ["Maria", "Anna", "Katarzyna", "Małgorzata", "Agnieszka", "Barbara", "Krystyna", "Ewa", "Teresa""Joanna",
                "Magdalena", "Zofia", "Jadwiga", "Danuta", "Monika", "Elżbieta", "Halina", "Beata", "Irena", "Dorota",
                "Bożena", "Renata", "Aleksandra", "Marta", "Janina", "Kamila", "Kinga", "Wanda", "Natalia", "Karolina",
                "Patrycja", "Mariola", "Klaudia", "Julia", "Grażyna", "Paulina", "Helena", "Aneta", "Agata", "Dominika",
                "Iwona", "Weronika", "Jolanta", "Kornelia", "Katarzyna", "Sabina", "Milena", "Anita", "Blanka", "Alicja",
                "Adriana", "Ewelina", "Marlena", "Katarzyna", "Agata", "Oliwia", "Maja", "Róża", "Marta", "Katarzyna",
                "Aleksandra", "Marzanna", "Patrycja", "Renata", "Sylwia", "Agnieszka", "Elżbieta", "Joanna", "Aniela",
                "Wioletta", "Kamila", "Katarzyna", "Dagmara", "Nina", "Paula", "Martyna", "Łucja", "Dominika", "Justyna",
                "Adrianna", "Izabela", "Klaudia", "Joanna", "Ewelina", "Olga", "Aleksandra", "Karina", "Katarzyna", "Inga",
                "Alicja", "Karolina", "Katarzyna", "Marta", "Anita", "Katarzyna", "Angelika", "Natasza", "Ilona", "Natalia",
                "Martyna", "Jagoda", "Karolina", "Daria", "Katarzyna", "Anita", "Natalia", "Katarzyna", "Katarzyna", "Marta",
                "Adrianna", "Barbara", "Paula", "Patrycja", "Magdalena", "Kamila", "Monika", "Magdalena", "Marta", "Katarzyna",
                "Klaudia", "Ewa", "Weronika", "Iwona", "Ewelina", "Aleksandra", "Agnieszka", "Kamila", "Joanna", "Sandra",
                "Natalia", "Martyna", "Katarzyna", "Monika", "Ewa", "Patrycja", "Anita", "Aleksandra", "Beata", "Małgorzata",
                "Aleksandra", "Monika", "Jolanta", "Karolina", "Katarzyna", "Zuzanna", "Monika", "Marta", "Weronika",
                "Aleksandra", "Katarzyna","Alicja", "Oliwia", "Emilia", "Natalia", "Nikola", "Antonina", "Lena", "Nina", "Iwona", "Adrianna","Anastazja", "Wanda", "Lilia", "Liwia", "Gabriela", "Julita", "Martyna", "Miriam", "Lidia", "Daria",
                "Ewelina", "Maja", "Agnieszka", "Aurelia", "Iga", "Jagna", "Sara", "Sonia", "Ludmiła", "Kamila",
                "Roksana", "Róża", "Aurelia", "Czesława", "Elena", "Lila", "Maryla", "Nadia", "Renata", "Wioletta",
                "Amanda", "Apolonia", "Celina", "Izabela", "Lea", "Leila", "Ligia", "Lilia", "Marlena", "Mia"]

wiek = [25,26,27,28,29,30,31,32,33,34]
miasta = ['Warszawy', 'Krakowa', 'Łodzi', 'Wrocławia', 'Poznania', 'Gdańska', 'Szczecina', 'Bydgoszczy', 'Lublina', 'Białegostoku', 'Katowic', 'Gdyni', 'Częstochowy', 'Radomia', 'Sosnowca', 'Torunia', 'Kielc', 'Rzeszowa', 'Gliwic', 'Zabrze', 'Olsztyna', 'Bielska-Białej', 'Bytomia', 'Zielonej Góry', 'Rybnika', 'Ruda Śląska', 'Tychów', 'Gorzowa Wielkopolskiego', 'Dąbrowy Górniczej', 'Płocka', 'Elbląga', 'Opola', 'Wałbrzycha', 'Tarnowa', 'Chorzowa', 'Kalisza', 'Koszalina', 'Legnicy', 'Grudziądza']
opis = ["Szukam kogoś, kto potrafi mnie rozbawić i robić ze nmną różne rzeczy, o których zawsze marzyłam.","Jestem pozytywnie nastawiona na życie i chętnie poznam kogoś, kto podziela moje wartości.","Lubię spontaniczne wypady i przygody. Szukam osoby, która jest gotowa zrobić coś niespodziewanego i niekoniecznie zaplanowanego.","Kocham muzykę i podróże. Chętnie poznam kogoś, kto podziela moje zainteresowania i jest gotowy na nowe przygody namiętności.","Szukam kogoś, kto potrafi mnie zaskoczyć i rozbudzić moje zmysły.","Lubię zmysłowe tańce i gorące nocne kluby. Chętnie poznam kogoś, kto chce ze mną zatańczyć i poczuć namiętność.","Jestem romantyczką i chciałabym poznać kogoś, kto potrafi mnie uwieść i zrobić coś wyjątkowego dla mnie.","Lubię masaż i wszystko, co związane z relaksacją. Chętnie poznam kogoś, kto chce ze mną zrelaksować się w zmysłowym otoczeniu.","Jestem osobą uwodzicielską i chciałabym poznać kogoś, kto podziela mój styl życia i podejście do związków.","Lubię fantazjować i chciałabym znaleźć kogoś, kto potrafi zrozumieć moje marzenia i chce pomóc mi je spełnić","Uwielbiam dobre wino i zmysłową atmosferę. Chętnie poznam kogoś, kto chce ze mną podzielić się tą pasją.","Lubię ostre emocje i intensywne przeżycia. chciałabym poznać kogoś, kto jest gotowy na wspólne przeżywanie niezapomnianych chwil.","Jestem miłośniczką dobrej muzyki i zmysłowego tańca. Chętnie poznam kogoś, kto chce ze mną zatańczyć i poczuć namiętność.","Szukam kogoś, kto jest gotowy na wspólne eksplorowanie swojego ciała i odkrywanie nowych sposobów na przyjemność.","Jestem bardzo otwarta na nowe doświadczenia i chętnie przetestuję różne pozycje i techniki. Szukam kogoś, kto będzie chciał to robić ze mną i eksperymentować.","Szukam starszego doświadczonego pana który lubi eksperymentować w łóżku","Co myślisz o moim wyglądzie?","Masz ochotę na mnie?","Chcesz się namiętnie porozciągać?","Co mnie myślisz?","Może się spotkamy?","Co byś zrobił ze mną sam na sam?","Chcesz spalić ze mną kalorie?","Czy byłbyś w stanie się skupić, gdybyś mnie zobaczył?","Czy znalazłby się ktoś, kto mógłby mi pomóc trenować w łózku?","Czy jest któs kto mógłby mnie trenować w łóżku?","Jak spędził byś ze mną wolny czas?","Napijemy się razem kawy?","Spędzimy razem wieczór?","Jestem ładna dla ciebie?","Chcę, żebyś zawsze otaczał mnie ramionami","Uczyń mnie swoją księżniczką","Kto ma ochotę na kolację ze mną?","Co sądzisz o moim stroju?","Spełnie twoje fantazje","Chcesz zobaczyć moją bieliznę?","co przychodzi ci do głowy, kiedy na mnie patrzysz?","Chcesz się ze mną spotkać?","Przyjdź i powiedz mi, o czym dzisiaj myślisz","Co mogę dla ciebie zrobic?","Czy moja figura jest w twoim typie?","Jakie jest twoje zdanie na temat mojego stroju?","Chodź tu i daj mi klapsa","Spędzimy namiętnie wieczór?","Czy mogę być twoją małą niewolnicą?","Może do mnie dołączysz?","Bardzo tęsknię za ciepłą pogoda 😩 A Wy?","Ocena od 1 do 10?","Chcesz trochę mnie?","jeśli pozwolę, zrobisz mi niegrzeczne rzeczy?","Co byś zrobił gdybyś mnie zobaczył taką w twoim łóżku?","Lato musi przyjść wcześniej","Pójdziesz za mną wszędzie i zagrasz ze mną w coś niegrzecznego?","Podoba ci się taki widok?","Chodź, zabaw się ze mną","Jestem samotna, czy są jacyś faceci, którzy chcą porozmawiać z seksowną dziewczyną taką jak ja?","Czy lubisz to co widzisz?","bardzo samotna, chcesz iść ze mną?","Za dużo jak na pierwszą randkę?","Uwielbiam być niegrzeczna i być zdominowana","Jak w tym wyglądam?","Chciałbyś zrobic coś niegrzecznego?","Masz ochotę na namiętne spotkanie?","Bądź szczery: co najpierw przykuwa twoją uwagę?"]





xlsx_file_path1 = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\1fb.xlsx"
xlsx_file_path2 = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\2fb.xlsx"
xlsx_file_path3 = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\3fb.xlsx"
xlsx_file_path4 = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\4fb.xlsx"

date_str = input("Podaj date opublikowania pierwszego posta '%Y-%m-%d %H:%M': ")
ilosc_postów = int(input("ile postów chcesz zaplanować?"))



path1 = "S:\\ARCHIWUM\\fanpage\\1fb"
path2 = "S:\\ARCHIWUM\\fanpage\\2fb"
path3 = "S:\\ARCHIWUM\\fanpage\\3fb"
path4 = "S:\\ARCHIWUM\\fanpage\\4fb"


def convert_and_numbering_name():
    # Lista obsługiwanych rozszerzeń plików
    supported_extensions = ['.webp', '.png']

    # Licznik dla numeracji plików
    counter = 1

    # Przejście przez pliki w folderze
    for filename in os.listdir(path1, path2, path3, path4):
        # Pełna ścieżka do pliku
        file_path = os.path.join(path1 filename)
        
        # Sprawdzenie rozszerzenia pliku
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Jeśli rozszerzenie jest obsługiwane, konwertuj na JPG
        if file_ext in supported_extensions:
            # Utwórz nową nazwę pliku
            new_filename = f'{counter}.jpg'
            new_file_path = os.path.join(path, new_filename)
            
            # Konwertuj plik do formatu JPG
            image = Image.open(file_path)
            image.convert('RGB').save(new_file_path, 'JPEG')
            
            # Zwiększ licznik
            counter += 1
        else:
            # Zostaw plik bez zmian
            
            # Utwórz nową nazwę pliku
            new_filename = f'{counter}{file_ext}'
            new_file_path = os.path.join(path, new_filename)
            
            # Zmień nazwę pliku
            os.rename(file_path, new_file_path)
            
            # Zwiększ licznik
            counter += 1