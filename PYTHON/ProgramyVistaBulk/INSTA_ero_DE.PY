import xlsxwriter

import datetime
import pandas as pd
import os
import random
from PIL import Image

#generowanie zdania
poczatek = ["Sexy", "Treffen", "Treffen Sie das Schöne", "Schön", "Hot", "Erotisch", "Hübsch", "Attraktiv","Frech","Süß","Einmalig"]

imiona = ['Mia', 'Emma', 'Hannah', 'Emilia', 'Lina', 'Sophia', 'Anna', 'Marie', 'Milena', 'Lena', 'Lara', 'Lea', 'Maja', 'Clara', 'Amelie', 'Johanna', 'Mila', 'Ida', 'Laura', 'Leni', 'Frieda', 'Luisa', 'Mathilda', 'Paula', 'Nele', 'Helena', 'Charlotte', 'Nora', 'Greta', 'Marlene', 'Jule', 'Melina', 'Jana', 'Sofie', 'Jasmin', 'Lotta', 'Fiona', 'Lisa', 'Paulina', 'Leonie', 'Carlotta', 'Annika', 'Victoria', 'Isabella', 'Franziska', 'Karoline', 'Annelie', 'Celina', 'Ronja', 'Lynn', 'Katharina', 'Alina', 'Nina', 'Teresa', 'Kira', 'Chiara', 'Stella', 'Ella', 'Lia', 'Julie', 'Rosa', 'Leila', 'Elisa', 'Lucie', 'Linda', 'Jette', 'Mira', 'Gloria', 'Juliana', 'Ina', 'Jara', 'Magdalena', 'Amalia', 'Svea', 'Emily', 'Elina', 'Hedi', 'Henriette', 'Josephine', 'Anni', 'Elena', 'Liv', 'Felicitas', 'Emmi', 'Elisabeth', 'Tilda', 'Tara', 'Eva', 'Kaja', 'Juna', 'Annemarie', 'Maira', 'Merle', 'Nike', 'Milla', 'Ines', 'Josefine', 'Marlene', 'Angelina', 'Romy', 'Jolina', 'Klara']
naileoceniasz = ",Wie hoch schätzen Sie ein?"
emotki = ["😍","🤭","👍","😮","😘","🥰","🤪","😜"]
hashtags = ['#deutschland', '#girl', '#germany', '#münchen', '#kinderdirndl', '#германия', '#me', '#russian', '#taufkleid', '#德国', '#travel', '#лето', '#photography', '#summervibes', '#nomakeup', '#lithuanian', '#hamburg', '#taufdirndl', '#fest', '#女孩', '#annakaval', '#девочка', '#ukrainian', '#summer', '#alemania', '#nofilters', '#afrika', '#liebe', '#alpen']


path = "S:\\ARCHIWUM\\insta\\niemiecki"


def convert_and_numbering_name():
# Lista obsługiwanych rozszerzeń plików
    supported_extensions = ['.webp', '.png']

    # Licznik dla numeracji plików
    counter = 1

    # Przejście przez pliki w folderze
    for filename in os.listdir(path):
        # Pełna ścieżka do pliku
        file_path = os.path.join(path, filename)
        
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



def tworzenie_pliku_excel():
    xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.xlsx"

    date_str = input("Podaj date opublikowania pierwszego posta '%Y-%m-%d %H:%M': ")

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    # Create a new XLSX file and add a worksheet
    workbook = xlsxwriter.Workbook(xlsx_file_path)
    worksheet = workbook.add_worksheet()

        
        

    # Set the column headers
    header_row = ["message", "type", "link", "time","commment1"]
    worksheet.write_row(0, 0, header_row)

    # Set up the CSV reader and read the column data


    # Write the column data and other data to the worksheet
    for i in range(14):
        # Write the message column data
        
        sentence = f"{random.choice(poczatek)} {random.choice(imiona)} {naileoceniasz} {random.choice(emotki)} \n{random.choices(hashtags, k=15)}"
        
        worksheet.write(i + 1, 0, sentence)
        
        # Write the type column data
        worksheet.write(i + 1, 1, "image")
        
        # Write the link column data
        link = f"http://hosting2275851.online.pro/ARCHIWUM/insta/niemiecki/{i+1}.jpg"
        worksheet.write(i + 1, 2, link)
        
        # Write the time column data
        
        
        worksheet.write(i + 1, 3, date.strftime("%Y-%m-%d %H:%M"))
        date += datetime.timedelta(hours = 24)
        
        
        



    # Close the workbook
    workbook.close()


def convert_xlsx_to_csv():
    df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.xlsx")

    df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.csv", index=False)

    exit()


convert_and_numbering_name()
tworzenie_pliku_excel()
convert_xlsx_to_csv()