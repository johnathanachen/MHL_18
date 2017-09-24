from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
import bs4 as bs
import urllib
from time import sleep

""" Access Keys"""
access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'

"""Sets up API"""
amazon = AmazonAPI(access_key,secret_key, assoc_tag)

"""Acts as User when requesting URL"""
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

userSearchKeyword = input("Search Keyword: ")
keyword = userSearchKeyword

"""Gets the list of URLs found on the Keyword Search Page"""
def get_list_href(keyword):
    amazon_url = 'https://www.amazon.com/s?keyword=' + keyword
    amazon_url_request = requests.get(amazon_url, headers=headers)
    amazon_url_request.raise_for_status()
    soup_final = bs.BeautifulSoup(amazon_url_request.text, 'lxml')

    # List all URL in with /dp/
    list_href = [el["href"] for el in soup_final.findAll("a", href=re.compile("/dp/"))]
    print("All url with /dp/ - PASS")

    # # Extract asin
    # m = re.search('(?<=/dp/)\w+', mystring)
    # print(m.group(0))

    return list_href


"""Gets the asin id out of a URL string"""
# def get_asin(url):
#     asin_scraper = r'/([A-Z0-9]{10})'
#     result = re.search(asin_scraper,url).group(1)
#     return result

# Gets list of asin ids out of a list of URLs
def get_list_asin(list_href):
    asin_list = []
    for address in list_href:
        asin_number = re.search('(?<=/dp/)\w+', address)
        asin_list.append(asin_number.group(0))
    print("list of asin numbers - PASS")
    return asin_list

"""Gets the Product name and price given its respective asin id"""
def product_info(asin_list):
    for asin_id in asin_list:
        product = amazon.search(ItemId=asin_id)
        title = product.title
        price = product.price_and_currency
        print (title)
        sleep(3)
        print (price[0])
        sleep(3)



"""Prints the Product names and titles from a list"""
def get_list_prices(asin_list):
    for asin in asin_list:
        find_price(asin)

list_href = get_list_href(keyword)
asin_list = get_list_asin(list_href)
product_info(asin_list)

    # if price[0] == None or price[0] == 0:
    #     return

# test_url_alibaba = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=power+bank'
#
# sauce = urllib.request.urlopen(test_url_alibaba).read()
# soup = bs.BeautifulSoup(sauce, 'lxml')
# soup_page = soup.body
# soup_page = soup_page.find('div', class_='l-page')
