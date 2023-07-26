# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path 
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink()

