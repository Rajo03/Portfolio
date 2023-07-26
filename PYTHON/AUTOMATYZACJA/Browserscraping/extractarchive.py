# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path
import zipfile

root_dir = Path('.')
destination_path = Path('destination')

for path in root_dir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = destination_path / Path(path.stem)
    zf.extractall(path=final_path)