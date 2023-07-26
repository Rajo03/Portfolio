from pathlib import Path

files_dir = Path('files')

for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    new_content = content[:-1]
  
  with open(filepath, 'w') as file:
    file.write(new_content)



with open('file3.csv', 'r') as file:
  content = file.read()


modified_content = content[:-1]

with open('file3.csv', 'w') as file:
  file.write(modified_content)