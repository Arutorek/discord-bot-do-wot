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


def  get_link_of_data_to_post(data_element):
  a = data_element.find('a', href=True)
  return a['href']


def checking_update(url, last_url):
  if url == last_url:
    return False
  else:
    return True


def createing_list_of_urls(data_elements, last_url):
  urls = []
  is_update = False
  for data_element in data_elements:
    if data_element == data_elements[0]:
      continue
    url = get_link_of_data_to_post(data_element)
    is_new_article = checking_update(url, last_url)
    if is_new_article:
      is_update = True
      urls.append(url)
      continue
    break
  return urls, is_update


def main(last_url):
  data_elements = web_scraper_wot()
  urls = createing_list_of_urls(data_elements, last_url)
  return urls


if __name__ == "__main__":
  last_url = "https://rykoszet.info/2023/01/06/wczesne-pobranie-aktualizacji-1-19-1-jest-juz-mozliwe/"
  while True:
    time.sleep(2)
    data_elements = web_scraper_wot()
    urls, is_update = createing_list_of_urls(data_elements, last_url)
    if is_update:
      last_url = urls[0]
      print("Update!!! new links here:\n", urls)
    else:
      print("There is no update yet")
