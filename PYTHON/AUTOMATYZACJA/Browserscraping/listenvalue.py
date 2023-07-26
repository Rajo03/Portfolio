import gspread
import time

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')
worksheet2 = spreadsheet.worksheet('Watch')

while True:
  value1 = worksheet1.acell('G26').value
  print(value1, type(value1))
  time.sleep(2)
  value2 = worksheet1.acell('G26').value
  if value1 != value2:
    worksheet2.update('A1', 'CHANGED')