from amazon.api import AmazonAPI
import cgi, cgitb 
import re
import requests
import bs4 as bs
import urllib

form = cgi.FieldStorage() 
keyword = form.getvalue('Amazon')

access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'

# userSearchKeyword = input("Search Keyword: ")
# keyword = userSearchKeyword

amazon = AmazonAPI(access_key,secret_key, assoc_tag)
products = amazon.search(Keywords=keyword, SearchIndex='All')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

for i, product in enumerate(products):
    print("{0}. '{1}'".format(product.title, product.price_and_currency[0]))





