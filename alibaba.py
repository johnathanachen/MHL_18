import re
import requests
import bs4 as bs
from urllib.request import urlopen
import json

keyword_alibaba = 'power bank'
keyword_alibaba = keyword_alibaba.replace(' ', '+')
alibaba_url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=' + keyword_alibaba
alibaba_url_request = urlopen(alibaba_url)



# "US $9.53-9.99"
# list_href = [el["href"] for el in soup_final.findAll("a", href=re.compile("/dp/"))]
# def get_list_asin(list_href):
#     asin_list = []
#     for address in list_href:
#         asin_number = re.search('(?<=/dp/)\w+', address)
#         asin_list.append(asin_number.group(0))
#     print("list of asin numbers - PASS")
#     return asin_list