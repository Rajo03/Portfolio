# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

root_dir = Path('.')
search_term = '14'

for path in root_dir.rglob("*"):
  if path.is_file():
    if search_term in path.stem:
      print(path.absolute())
