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

keyword_alibaba = 'power bank'
keyword_alibaba = keyword_alibaba.replace(' ', '+')
alibaba_url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=' + keyword_alibaba
alibaba_url_request = urlopen(alibaba_url)
alibaba_html = alibaba_url_request.read()
alibaba_html = alibaba_html.decode('utf-8')
print(alibaba_html)



list_html = alibaba_html.split('price')
# result = re.search(price_scraper,alibaba_html)
price_list = []
for item in list_html:
    # price_value = re.search('(?<=US )$',item).group(0)
    price_list.append()

"""find 15 letters after US $"""
# starts at 9
#
# "price":"US
# alibaba_url_request.raise_for_status()
# soup_alibaba = bs.BeautifulSoup(alibaba_url_request.text, 'json')
# result = soup_alibaba.find_allr('a', string='price')
# price_scraper = r'"price:"([^"]*)"'
# result = re.search(price_scraper,soup_alibaba).group(1)
# re.search(r'"fmt_headline":"([^"]*)"', y)
# list_href=[]
# for a in soup_alibaba(href=True):
#     list_href += [a['href']]

# list_price=soup_alibaba.find_all('div', class_= 'price')

# soup = bs.BeautifulSoup(sauce, 'lxml')
# soup_page = soup.body
# soup_page_div = soup.find_all('div', class_='l-page')
# # soup_l_page = soup_page.find('div', class_='l-page')
# soup_l_page = soup_page_div.findall('div', class_='l-page-main')
# for i in soup_l_page:
#     print(i.prettify())
