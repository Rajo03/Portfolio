# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(content['articles'])