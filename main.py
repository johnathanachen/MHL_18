from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
import bs4 as bs
import urllib
"""1. Find a way to get url of first search result
   2. Build out the Alibaba API side
   3. Create a function that finds the price differential between the two
   4. Build out the front-end"""

"""Add keys to the top"""


amazon = AmazonAPI(access_key,secret_key, assoc_tag)


test_url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=power+bank'

sauce = urllib.request.urlopen(test_url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
soup_page = soup.body
soup_page = soup_page.find('div', class_='l-page')

def get_asin(url):
    asin_scraper = r'/([A-Z0-9]{10})'
  # asin_scraper = r'https://www.amazon.com/.*/dp/(.*)\''
    result = re.search(asin_scraper,url).group(1)
    return result



def find_price(asin_id):
    product = amazon.lookup(ItemId=asin_id)
    title = product.title
    price = product.price_and_currency
    if price[1] == 'USD':
        print(title)
        print(price[0])
        return price[0]



# asin_id = get_asin(test_url)
# price = find_price(asin_id)
