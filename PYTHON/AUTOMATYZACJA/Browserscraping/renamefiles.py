# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.iterdir()
print(Path.cwd())
for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix
  new_filepath = path.with_name(new_filename)
  print(new_filepath)
  path.rename(new_filepath)
  