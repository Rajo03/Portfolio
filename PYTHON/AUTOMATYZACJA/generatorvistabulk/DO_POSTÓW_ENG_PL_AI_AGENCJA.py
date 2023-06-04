import xlsxwriter
import csv
import datetime
import pandas as pd
import os
import time





# Set up the input and output file paths
csv_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\generatorvistabulk\\input\\opis.csv"
xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\generatorvistabulk\\output\\output.xlsx"

date_str = input("Enter date and time in the format 'DD.MM.YYYY HH:MM': ")
date = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")

# Create a new XLSX file and add a worksheet
workbook = xlsxwriter.Workbook(xlsx_file_path)
worksheet = workbook.add_worksheet()

    
    

# Set the column headers
header_row = ["message", "type", "link", "time"]
worksheet.write_row(0, 0, header_row)

# Set up the CSV reader and read the column data
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    column_data = [row[0] for row in csv_reader]

# Write the column data and other data to the worksheet
for i in range(len(column_data)):
    # Write the message column data
    worksheet.write(i + 1, 0, column_data[i])
    
    # Write the type column data
    worksheet.write(i + 1, 1, "image")
    
    # Write the link column data
    link = f"http://hosting2275851.online.pro/zdjecia/markaosobista/ENG/{i+1}_n.mp4"
    worksheet.write(i + 1, 2, link)
    
    # Write the time column data
    
    
    worksheet.write(i + 1, 3, date.strftime("%d.%m.%Y %H:%M"))
    date += datetime.timedelta(hours=24)




# Close the workbook
workbook.close()



#convert from xlsx to csv
input_folder = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\generatorvistabulk\\output"
output_folder = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\generatorvistabulk\\input"


# Create the output folder (if it doesn't already exist)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Continuously monitor the input folder for XLSX files
while True:
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xlsx'):
            # Set the paths of the input and output files
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace('.xlsx', '.csv'))

            # Read the XLSX file into a Pandas dataframe
            df = pd.read_excel(input_file)

            # Write the dataframe to a CSV file
            df.to_csv(output_file, encoding='utf-8', index=False)

            # Delete the input file
            os.remove(input_file)

            print(f"{input_file} converted to {output_file}")

    # Wait for 5 seconds before checking for new files
    time.sleep(5)