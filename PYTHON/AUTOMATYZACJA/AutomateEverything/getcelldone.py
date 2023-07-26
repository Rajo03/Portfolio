
import gspread
import re

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# Get cell
cell1 = worksheet1.get_values('D5')[0][0]

# Get cell using acell
cell2 = worksheet1.acell('D5').value

# Search for a cell 
cell3 = worksheet1.find('-10')

# Search for many cells 
cells = worksheet1.findall('-9')

# Search for partial matches
reg = re.compile(r'99')
cells = worksheet1.findall(reg)

for cell in cells:
  print(cell.row, cell.col)