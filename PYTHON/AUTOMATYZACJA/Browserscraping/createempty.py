# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

root_dir = Path('files')

for i in range(10, 21):
  filename = str(i) + '.txt'
  filepath = root_dir / Path(filename)
  filepath.touch()