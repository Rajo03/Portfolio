import xlsxwriter
import datetime
import pandas as pd
import os
import random
from PIL import Image

#opis 
gora = ["🌞☀️🤍","Modern home🤍🤍","One of my favorite design🤍✨","Modern design🤍🤍🤍","Peace and serenity 🤍✨","Minimalist bedroom🤍🤍🤍","🤍✨🤍✨🤍","Simple livingroom🤍✨","🤍🤍🤍","This is just perfect🤍","Classy home🤍✨","Minimalist bedroom🤍✨🤍","What a beautiful home♥️🤍","So serene. ✨🤍 What do you think about this space?","What do you think about this space?","Just imagine waking up to this view. What do you think about this space?","Bright, refined and cozy. The beautiful bedroom","Spacious and elegant. How do you like this space?","Neutral dreams. ✨🤍","What do you think about this space?","Simply perfect ✨🤍✨","Simplicity is key🤍✨","White interior🤍🤍🤍","Monday vibes🤍🤍🤍","Cozy space🤍✨"]

link = "Remember to follow us @minimalist.decors_ for more daily inspiration!"

hashtagi = ["#interiordesign", "#interiortrends", "#homedecorideas", "#moderninterior", "#interiormagazine", "#roomdesign", "#houseinterior", "#interiordecore", "#interiorwarrior", "#nordichomes", "#minimalisthome", "#minimalhome", "#minimalistdecor", "#simpledecor", "#myinteriorstyle", "#interiors4you", "#myhouseidea", "#homedecorating", "#minimalistdesign", "#livingroominterior", "#minimalistinterior", "#homestyling"]

emotki = ["😍","🤭","👍","😮","😘","🥰","🤪","😜"]


path = "S:\\ARCHIWUM\\MinimalistInterior\\instagram"

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

    xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.xlsx"

    date_str = input("Podaj date opublikowania pierwszego posta '%Y-%m-%d %H:%M': ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    # Create a new XLSX file and add a worksheet
    workbook = xlsxwriter.Workbook(xlsx_file_path)
    worksheet = workbook.add_worksheet()

        
        

    # Set the column headers
    header_row = ["message", "type", "link", "time"]
    worksheet.write_row(0, 0, header_row)

    # Set up the CSV reader and read the column data

    # Write the column data and other data to the worksheet
    for i in range(50):
        
        # Write the message column data
        
        message = f"{random.choice(gora)} {random.choices(hashtagi, k=15)} \n {link}"
        
        worksheet.write(i + 1, 0, message)
        
        # Write the type column data
        worksheet.write(i + 1, 1, "video")
        
        # Write the link column data
        link_path = f"http://hosting2275851.online.pro/ARCHIWUM/MinimalistInterior/instagram/{i+1}.jpg"
        worksheet.write(i + 1, 2, link_path)
        
        # Write the time column data
        
        
        worksheet.write(i + 1, 3, date.strftime("%Y-%m-%d %H:%M"))
        date += datetime.timedelta(hours=24)
        



    # Close the workbook
    workbook.close()




def convert_xlsx_to_csv():
    df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.xlsx")

    df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.csv", index=False)

    exit()



convert_and_numbering_name()
tworzenie_pliku_excel()
convert_xlsx_to_csv()