import xlsxwriter
import datetime
import pandas as pd
import os
import random
from PIL import Image

#generowanie zdania
poczatek = ["Seksi", "Seksowna","Przepiękna", "Urocza", "Piękna", "Ładna", "Atrakcyjna", "Wyjątkowa", "Niegrzeczna","Milutka"]
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

naileoceniasz = "Na ile oceniasz?"

emotki = ["😍","🤭","👍","😮","😘","🥰","🤪","😜"]

hashtags = ["#bikini", "#polishgirl", "#polskadziewczyna", "#fit", "#summer", "#body", "#fitness", "#girl", "#sun", "#beach", "#fitgirl", "#poland", "#instagood", "#love", "#model", "#legs", "#photooftheday", "#bikinifitness", "#brunette", "#beautiful", "#motivation", "#me", "#fashion", "#bodybuilding", "#sea", "#happy", "#fitnessmotivation", "#instagirl", "#gym", "#beauty"]



path = "S:\\ARCHIWUM\\insta\\polski"

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
    xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroPL.xlsx"

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
        link = f"http://hosting2275851.online.pro/ARCHIWUM/insta/polski/{i+1}.jpg"
        worksheet.write(i + 1, 2, link)
        
        # Write the time column data
        
        
        worksheet.write(i + 1, 3, date.strftime("%Y-%m-%d %H:%M"))
        date += datetime.timedelta(hours = 24)
        
        
        



    # Close the workbook
    workbook.close()



def convert_xlsx_to_csv():
    df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroPL.xlsx")

    df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroPL.csv", index=False)


    exit()





convert_and_numbering_name()
tworzenie_pliku_excel()
convert_xlsx_to_csv()