import requests
from bs4 import BeautifulSoup
import time


base_url = 'https://rykoszet.info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

data_from_page = []


def web_scraper_wot():
    data_elements = soup.find('div', class_='post-content')
    return data_elements


def checking_for_update(data_elements, year_of_lastes_post, month_of_lastes_post, day_of_lastes_post, hour_of_lastes_post, minute_of_lastes_post):
    date_time = data_elements.find('time', class_='published updated').text
    year, month, day, hour, minute = revriting_date_and_time_data(date_time)
    if int(year) > year_of_lastes_post or month > month_of_lastes_post or int(day) > day_of_lastes_post or int(hour) > hour_of_lastes_post or int(minute) > minute_of_lastes_post:
        return True, year, month, day, hour, minute
    else:
        return False, None, None, None, None, None


def revriting_date_and_time_data(date_time):
    hour = date_time[0:2]
    minute = date_time[3:5]
    day = date_time[7:9]
    month_string = date_time[10:13]
    month = convert_month_in_words_to_numbers(month_string)
    year = date_time[-4:]
    return year, month, day, hour, minute


def convert_month_in_words_to_numbers(month_string):
    if month_string == "sty":
        return 1
    elif month_string == "lut":
        return 2
    elif month_string == "mar":
        return 3
    elif month_string == "kwi":
        return 4
    elif month_string == "maj":
        return 5
    elif month_string == "cze":
        return 6
    elif month_string == "lip":
        return 7
    elif month_string == "sie":
        return 8
    elif month_string == "wrz":
        return 9
    elif month_string == "paź":
        return 10
    elif month_string == "lis":
        return 11
    else:
        return 12


def get_link_of_data_to_post(data_elements):
    a = data_elements.find('a', href=True)
    url = a['href']
    print(url)


def main():
    year_of_lastes_post = 0
    month_of_lastes_post = 0
    day_of_lastes_post = 0
    hour_of_lastes_post = 0
    minute_of_lastes_post = 0
    while True:
        time.sleep(60)
        data_elements = web_scraper_wot()
        is_update, year, month, day, hour, minute = checking_for_update(data_elements, year_of_lastes_post, month_of_lastes_post, day_of_lastes_post, hour_of_lastes_post, minute_of_lastes_post)
        print(is_update)
        if is_update:
            get_link_of_data_to_post(data_elements)
            year_of_lastes_post = int(year)
            month_of_lastes_post = month
            day_of_lastes_post = int(day)
            hour_of_lastes_post = int(hour)
            minute_of_lastes_post = int(minute)
        


main()
