import gspread

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# Get a row or rows by cells
rows = worksheet1.get_values('A5:F7')

# Get a row by index 
rows = worksheet1.row_values(3)

# Get a column by index
column = worksheet1.col_values(2)[1:]

print(rows)
