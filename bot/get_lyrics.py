from requests import get
from bs4 import BeautifulSoup
import time
import random


def scrapy():

    urls = ['https://www.metrolyrics.com/playboi-carti-alpage-1.html',
            'https://www.metrolyrics.com/playboi-carti-alpage-2.html']

    href_array = []

    verses_array = []

    for i in range(len(urls)):

        url_response = get(urls[i])

        urlsoup = BeautifulSoup(url_response.text, 'html.parser')

        href_class = urlsoup.find('div', class_='content')

        hrefs = href_class.find_all('a')

        for href in hrefs:
            href_array.append(href['href'])

        for j in range(len(href_array)):

            chosen_url = href_array[j]

            response = get(chosen_url)

            chosen_url_soup = BeautifulSoup(response.text, 'html.parser')
            all_verses = chosen_url_soup.find_all('p', class_='verse')

            for i in range(len(all_verses)):
                for text in all_verses[i].stripped_strings:
                    if text[0] != '[' and text[0] != '{':
                        verses_array.append(text.lower())

        return verses_array
