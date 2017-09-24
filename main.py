from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
import bs4 as bs
from urllib.request import urlopen
import json

""" Access Keys"""
access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'

"""--------AMAZON-------"""

"""Sets up API"""
amazon = AmazonAPI(access_key,secret_key, assoc_tag)

"""Acts as User when requesting URL"""
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }


"""Gets the list of URLs found on the Keyword Search Page"""
def get_list_href(keyword):
    amazon_url = 'https://www.amazon.com/s?keyword=' + keyword
    amazon_url_request = requests.get(amazon_url, headers=headers)
    amazon_url_request.raise_for_status()
    soup_final = bs.BeautifulSoup(amazon_url_request.text, 'lxml')
    list_href=[]
    for a in soup_final.find_all(href=True):
        list_href += [a['href']]
    return list_href

"""Gets the asin id out of a URL string"""
def get_asin(url):
    asin_scraper = r'/([A-Z0-9]{10})'
    result = re.search(asin_scraper,url).group(1)
    return result

"""Gets list of asin ids out of a list of URLs"""
def get_list_asin(list_href):
    asin_list=[]
    for i in list_href:
        try:
            asin_list += [get_asin(i)]
        except:
            pass
    return asin_list

"""Gets the Product name and price given its respective asin id"""
def find_price(asin_id):
    product = amazon.lookup(ItemId=asin_id)
    title = product.title
    price = product.price_and_currency
    if price[0] == None or price[0] == 0:
        return None
    return price[0]
    # print (title)
    # print (price[0])

"""Prints the Product names and titles from a list"""
def get_list_prices(asin_list):
    list_prices = []
    for asin in asin_list:
        if find_price(asin) != None:
            list_prices.append(float(find_price(asin)))
    return list_prices


#
# for i, product in enumerate(products):
#     print("{0}. '{1}'".format(product.title, product.price_and_currency[0]))

"""------ALIBABA-------"""


def get_alibaba_html(keyword):
    keyword = keyword.replace(' ', '+')
    alibaba_url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=' + keyword
    alibaba_url_request = urlopen(alibaba_url)
    alibaba_html = alibaba_url_request.read()
    alibaba_html = alibaba_html.decode('utf-8')
    list_html = alibaba_html.split('price')
    return list_html


def get_price_list(html):
    price_list = []
    for item in html:
        price_list.append(item[0:20])
    return price_list



def get_result(price_list):
    result = []
    def find_price_value(word):
        price_test = ""
        for i in range(len(price_list[word])):
            if price_list[word][i] == '$':
                for k in range(i+1,len(price_list[word])):
                    if price_list[word][k] == '\"' or price_list[word][k] == '-':
                        break
                    else:
                        price_test += (price_list[word][k])
        return price_test
    for item in range(len(price_list)):
        if find_price_value(item) != '':
            result.append(float(find_price_value(item)))
    return result

def average_prices(list):
    total = 0
    for i in list:
        total += i
    return total/len(list)


def full_amazon(keyword):
    list_href = get_list_href(keyword)
    asin_list = get_list_asin(list_href)
    result_amazon = get_list_prices(asin_list[0:5])
    return result_amazon




def full_alibaba(keyword):
    list_html = get_alibaba_html(keyword)
    price_list = get_price_list(list_html)
    result_alibaba = get_result(price_list)
    return result_alibaba



def get_amazon_minus_alibaba(keyword):

    amazon_final = full_amazon(keyword)
    alibaba_final = full_alibaba(keyword)
    return average_prices(amazon_final) - average_prices(alibaba_final)
