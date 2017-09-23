from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
import bs4 as bs
import urllib

access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'

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



asin_id = get_asin(test_url)
price = find_price(asin_id)
