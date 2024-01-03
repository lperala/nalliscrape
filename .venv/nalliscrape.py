import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

# Going through the example provided in:
# https://brightdata.com/blog/how-tos/web-scraping-with-python

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# Testing stuff:
if False:

    page = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    # get all <h1> elements
    # on the page
    h1_elements = soup.find_all('h1')
    #print(h1_elements)

    # get the element with id="main-title"
    main_title_element = soup.find(id='main-title')
    #print(main_title_element)

    # find the email input element
    # through its "name" attribute
    email_element = soup.find(attrs={'name': 'email'})
    #print(email_element)

    # find all the centered elements
    # on the page
    centered_element = soup.find_all(class_='text-center')
    #print(centered_element)

    # get all "li" elements
    # in the ".navbar" element
    #soup.find(class_='navbar').find_all('li')


    #footer_elements = soup.find(text={"1 h"})
    #centered_element = soup.find_all(class_='text-center')
    #print(soup.select('.navbar > li'))

    #print(footer_elements)

    quotes = []
    quote_elements = soup.find_all('div', class_ = "")
    #print(quote_elements)
"""
    for quote_element in quote_elements:
        # extract the text of the quote
        text = quote_element.find('span', class_='text').text
        # extract the author of the quote
        author = quote_element.find('small', class_='author').text

        # extract the tag <a> HTML elements related to the quote
        tag_elements = quote_element.select('.tags .tag')

        # store the list of tag strings in a list
        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.text)

    quotes.append(
        {
            'text': text,
            'author': author,
            'tags': ', '.join(tags)  # merge the tags into a "A, B, ..., Z" string
        }
    )
    print(quotes)
"""
browser = webdriver.Firefox()
url = 'https://nallisport.cintoia.com/'
browser.get(url)
time.sleep(10)
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")
#printing = soup.find_all("div", class_ = "MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button")
courts_list = soup.find_all("div", style ="display: flex;")
browser.close()
#test

courts_list_txt = []
for i in courts_list:
    courts_list_txt.append(i.text)

courts_list_txt_cleaned = []
for j in courts_list_txt:
    j.replace(" ", "")
    courts_list_txt_cleaned.append(j)

for k in courts_list_txt_cleaned:
    print(k)

#page = requests.get('https://nallisport.cintoia.com/')
#soup = BeautifulSoup(page.text, 'html.parser')

#h1_elements = soup.find_all('div', class_ = "")
#print(h1_elements)

#quote_elements = soup.find_all('div', class_ = 'row')

#print(quote_elements)
