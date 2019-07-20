import re
import csv
import requests

from bs4 import BeautifulSoup
import pandas as pd


def getprice(soup, d='div', c='pdp-product-price', li='li'):
    try:
        ret = soup.find(d, class_=c).find(li).text.split('  ')[1][:-2]
        return ret
    except(AttributeError):
        None


def gettitle(soup, title='title'):
    try:
        ret = soup.find_all('span',title)
        return ret
    except(AttributeError):
        None


def getrating(soup, d, c1, li, c2):
    try:
        ret = soup.find(d, class_=c1).find(li, class_=c2).find('p').text
        return ret
    except(AttributeError):
        None


def getcomment(soup, d='div', c='content'):
    try:
        ret = soup.find(d, class_=c).text
        return ret
    except(AttributeError):
        None


d = dict()

urls = ['https://hamrobazaar.com/i1631584-usb-sound-card-5-1.html']


def getdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # price = getprice(soup, 'ul', 'row mrp-outer', 'li')
    print(r.text)
    title = gettitle(soup, 'title')
    print(title)
    rating = getrating(soup, 'div', 'fullWidth writeReview', 'li', 'reviewCount')
    comment = [getcomment(i, 'div', 'content') for i in soup.find_all('div', class_='item-content')]
    image_link = soup.find('figure').find('img')['src']
    d['sastodeal'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'image_link': image_link}

    return d


print(getdata(urls[0]))
# for url in urls:
#     print(getdata(url))

# print(r.text)
# x = r.find_all('div', class_='pdp-mod-product-badge-wrapper')
# print(x.text)
