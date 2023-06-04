import xlsxwriter
import csv
import datetime
import pandas as pd
import os
import time
import random
from PIL import Image

#generowanie zdania
poczatek = ["Sexy", "Treffen", "Treffen Sie das Schöne", "Schön", "Hot", "Erotisch", "Hübsch", "Attraktiv","Frech","Süß","Einmalig"]

imiona = ['Mia', 'Emma', 'Hannah', 'Emilia', 'Lina', 'Sophia', 'Anna', 'Marie', 'Milena', 'Lena', 'Lara', 'Lea', 'Maja', 'Clara', 'Amelie', 'Johanna', 'Mila', 'Ida', 'Laura', 'Leni', 'Frieda', 'Luisa', 'Mathilda', 'Paula', 'Nele', 'Helena', 'Charlotte', 'Nora', 'Greta', 'Marlene', 'Jule', 'Melina', 'Jana', 'Sofie', 'Jasmin', 'Lotta', 'Fiona', 'Lisa', 'Paulina', 'Leonie', 'Carlotta', 'Annika', 'Victoria', 'Isabella', 'Franziska', 'Karoline', 'Annelie', 'Celina', 'Ronja', 'Lynn', 'Katharina', 'Alina', 'Nina', 'Teresa', 'Kira', 'Chiara', 'Stella', 'Ella', 'Lia', 'Julie', 'Rosa', 'Leila', 'Elisa', 'Lucie', 'Linda', 'Jette', 'Mira', 'Gloria', 'Juliana', 'Ina', 'Jara', 'Magdalena', 'Amalia', 'Svea', 'Emily', 'Elina', 'Hedi', 'Henriette', 'Josephine', 'Anni', 'Elena', 'Liv', 'Felicitas', 'Emmi', 'Elisabeth', 'Tilda', 'Tara', 'Eva', 'Kaja', 'Juna', 'Annemarie', 'Maira', 'Merle', 'Nike', 'Milla', 'Ines', 'Josefine', 'Marlene', 'Angelina', 'Romy', 'Jolina', 'Klara']


naileoceniasz = ",Wie hoch schätzen Sie ein?"

emotki = ["😍","🤭","👍","😮","😘","🥰","🤪","😜"]

hashtags = ['#deutschland', '#girl', '#germany', '#münchen', '#kinderdirndl', '#германия', '#me', '#russian', '#taufkleid', '#德国', '#travel', '#лето', '#photography', '#summervibes', '#nomakeup', '#lithuanian', '#hamburg', '#taufdirndl', '#fest', '#女孩', '#annakaval', '#девочка', '#ukrainian', '#summer', '#alemania', '#nofilters', '#afrika', '#liebe', '#alpen']


#rename pliki i convert na jpg
path = "S:\\insta\\niemiecki"

# get list of files in folder
files = os.listdir(path)

# keep only files with extension .webp or .png
files = [f for f in files if f.endswith('.webp') or f.endswith('.png')]

# loop through files and convert to jpg
for i, file in enumerate(files):
    # open file
    im = Image.open(os.path.join(path, file))
    
    # convert to jpg and save with new name
    new_name = f'{i+1}.jpg'
    im = im.convert('RGB')
    im.save(os.path.join(path, new_name))
    
    # delete original file
    os.remove(os.path.join(path, file))

# rename remaining files to numbering from 1
files = os.listdir(path)
for i, file in enumerate(files):
    # ignore files that are already jpg
    if not file.endswith('.jpg'):
        # construct new name
        new_name = f'{i+1}.jpg'
        
        # rename file
        os.rename(os.path.join(path, file), os.path.join(path, new_name))




# Set up the input and output file paths
xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.xlsx"

date_str = input("Podaj date opublikowania pierwszego posta 'DD.MM.YYYY HH:MM': ")

date = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")

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
    link = f"http://hosting2275851.online.pro/zdjecia/ero/instaDE/{i+1}.jpg"
    worksheet.write(i + 1, 2, link)
    
    # Write the time column data
    
    
    worksheet.write(i + 1, 3, date.strftime("%d.%m.%Y %H:%M"))
    date += datetime.timedelta(hours = 24)
    
    
    



# Close the workbook
workbook.close()








# read the xlsx file
df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.xlsx")

# save as csv file
df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\InstaEroDE.csv", index=False)

# end the program
exit()