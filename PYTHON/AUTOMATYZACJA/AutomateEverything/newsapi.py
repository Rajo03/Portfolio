# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests


def get_news(topic, from_date, to_date, language='en',
            api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.
print(get_news(topic='space', from_date='2022-11-25', to_date='2022-11-28'))



