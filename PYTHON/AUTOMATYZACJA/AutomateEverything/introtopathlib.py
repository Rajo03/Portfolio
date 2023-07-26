# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

if not p1.exists():
  with open(p1, 'w') as file:
    file.write('Content 3')


print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path('files')
print(list(p2.iterdir()))
