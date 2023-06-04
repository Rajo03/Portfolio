import xlsxwriter
import csv
import datetime
import pandas as pd
import os
import time
import random
from PIL import Image

#rename pliki i convert na jpg
path = "S:\\ARCHIWUM\\interiordesign\\instagram"

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





#opis 
gora = ["🌞☀️🤍","Modern home🤍🤍","One of my favorite design🤍✨","Modern design🤍🤍🤍","Peace and serenity 🤍✨","Minimalist bedroom🤍🤍🤍","🤍✨🤍✨🤍","Simple livingroom🤍✨","🤍🤍🤍","This is just perfect🤍","Classy home🤍✨","Minimalist bedroom🤍✨🤍","What a beautiful home♥️🤍","So serene. ✨🤍 What do you think about this space?","What do you think about this space?","Just imagine waking up to this view. What do you think about this space?","Bright, refined and cozy. The beautiful bedroom","Spacious and elegant. How do you like this space?","Neutral dreams. ✨🤍","What do you think about this space?","Simply perfect ✨🤍✨","Simplicity is key🤍✨","White interior🤍🤍🤍","Monday vibes🤍🤍🤍","Cozy space🤍✨"]



link = "Remember to follow us @minimalist.decors_ for more daily inspiration!"

hashtagi = ["#interiordesign", "#interiortrends", "#homedecorideas", "#moderninterior", "#interiormagazine", "#roomdesign", "#houseinterior", "#interiordecore", "#interiorwarrior", "#nordichomes", "#minimalisthome", "#minimalhome", "#minimalistdecor", "#simpledecor", "#myinteriorstyle", "#interiors4you", "#myhouseidea", "#homedecorating", "#minimalistdesign", "#livingroominterior", "#minimalistinterior", "#homestyling"]

emotki = ["😍","🤭","👍","😮","😘","🥰","🤪","😜"]


# Set up the input and output file paths

xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.xlsx"

date_str = input("Podaj date opublikowania pierwszego posta 'DD.MM.YYYY HH:MM': ")
date = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")

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
    link_path = f"http://hosting2275851.online.pro/zdjecia/minimalist interior insta/{i+1}.jpg"
    worksheet.write(i + 1, 2, link_path)
    
    # Write the time column data
    
    
    worksheet.write(i + 1, 3, date.strftime("%d.%m.%Y %H:%M"))
    date += datetime.timedelta(hours=24)
    



# Close the workbook
workbook.close()




# read the xlsx file
df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.xlsx")

# save as csv file
df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\minimalistinsta.csv", index=False)

# end the program
exit()
