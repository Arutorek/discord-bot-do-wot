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
  data_elements = soup.find('div', class_='post-inner post-hover')
  return data_elements


def get_link_of_data_to_post(data_elements):
  a = data_elements.find('a', href=True)
  url = a['href']
  return url


def checking_update(url, last_url):
  if url == last_url or url == None:
    return False
  else:
    return True


def main(last_url):
  data_elements = web_scraper_wot()
  url = get_link_of_data_to_post(data_elements)
  is_update = checking_update(url, last_url)
  return is_update, url


if __name__ == "__main__":
  main(last_url=None)
