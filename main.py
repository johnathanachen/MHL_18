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

access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'
amazon = AmazonAPI(access_key,secret_key, assoc_tag)


# test_url_alibaba = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=power+bank'
#
# sauce = urllib.request.urlopen(test_url_alibaba).read()
# soup = bs.BeautifulSoup(sauce, 'lxml')
# soup_page = soup.body
# soup_page = soup_page.find('div', class_='l-page')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
keyword = 'macbook'
test_url_amazon = 'https://www.amazon.com/s?keyword=' + keyword
soup2 = requests.get(test_url_amazon, headers=headers)
soup2.raise_for_status()
soup_final = bs.BeautifulSoup(soup2.text, 'lxml')


def get_asin(url):
    asin_scraper = r'/([A-Z0-9]{10})'
  # asin_scraper = r'https://www.amazon.com/.*/dp/(.*)\''
    result = re.search(asin_scraper,url).group(1)
    return result

for a in soup_final.find_all('a', href=True):
    print (get_asin(a['href']))



def find_price(asin_id):
    product = amazon.lookup(ItemId=asin_id)
    title = product.title
    price = product.price_and_currency
    return price[0]
    # if price[1] == 'USD':
    #     print(title)
    #     print(price[0])
    #     return price[0]



# asin_id = get_asin(test_url_amazon)
# price = find_price(asin_id)
