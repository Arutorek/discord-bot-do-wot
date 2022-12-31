import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://rykoszet.info'

headers = {
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

data_from_page = []


def web_scraper_wot():
  data_elements = soup.find_all('div', class_='post-inner post-hover')
  return data_elements


def get_link_of_data_to_post(data_elements, last_url):
  urls = []
  is_update = False
  for data_element in data_elements:
    a = data_element.find('a', href=True)
    url = a['href']
    is_update = checking_update(url, last_url)
    if is_update:
      return is_update, urls
    urls.append(url)
  return is_update, urls
    


def checking_update(url, last_url):
  if url == last_url or url == None:
    return False
  else:
    return True


def main(last_url):
  data_elements = web_scraper_wot()
  return get_link_of_data_to_post(data_elements, last_url)


if __name__ == "__main__":
  main(last_url=None)
