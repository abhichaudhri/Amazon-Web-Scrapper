from bs4 import BeautifulSoup
import random
import requests
from requests import get
import re
import csv
from urllib.request import urlopen
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html )'}

# asin = input("Enter the ASIN number, else leave it blank and press enter:")

pref = input("Do you want to scrap a product or a webpage?")
# B07X7JH41Q
def asin_number():

    asin = input("Enter the ASIN number of the product:")

    url = 'https://www.amazon.in/dp/' + asin + '/'

    resp = requests.get(url,headers=headers)
    # print(resp)
    s = BeautifulSoup(resp.content, features="lxml")

    product_title = s.select('#productTitle')[0].get_text().strip()
    print('Product Name:', end=' ')
    print(product_title)
    product_orgprice = s.select('.a-text-strike')[0].get_text().strip()
    print('Original price:', end='')
    print(product_orgprice)
    product_price = s.select('#priceblock_ourprice')[0].get_text()
    print('Discounted price:', end='')
    print(product_price)
    print('ASIN number:', end = ' ')
    print(asin)
    product_seller = s.select('#sellerProfileTriggerId')[0].get_text()
    print('Seller Name:', end='')
    print(product_seller)

############################  BREAK  ################################

import requests
from bs4 import BeautifulSoup
def link_func():

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    url = input('Enter the link you want to scrap:')
    # url = 'https://www.amazon.in/s?i=computers&bbn=1375424031&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375424031%2Cp_85%3A10440599031%2Cp_72%3A1318477031&pf_rd_i=1375424031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=93ab47fc-f487-498b-aff1-4e97b87b9dbc&pf_rd_r=MFP9XV7TZ2RTK0MKZVEJ&pf_rd_s=merchandised-search-9&pf_rd_t=101&ref=s9_acss_bw_cg_INTELEXC_2b1_w'

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'lxml')

    product_containers = soup.find('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})

    products = product_containers.find_all('div', {'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})

    for product in products:
        product_link_div = product.find('a', {'class': 'a-link-normal a-text-normal'})
        product_link = product_link_div['href'].strip()
        product_name = product_link_div.text.strip()
        product_price_class = product.find('span', {'class': 'a-price'})
        product_price = product_price_class.find('span', {'class': 'a-offscreen'}).text.strip()
        product_list_price_class = product.find('span', {'class': 'a-price a-text-price'})
        product_list_price = product_list_price_class.find('span', {'class': 'a-offscreen'}).text.strip()
        asin = re.findall(r"(?<=dp/)[A-Z0-9]{10}", product_link)[0]

        print('Name: ' + product_name)
        print('Link: ' + product_link)
        print('ASIN: ' + asin)
        print('Final price: ' + product_price)
        print('List price: ' + product_list_price)
        print('\n')

    print("Products scraped: " + str(len(products)))

# asin_number()

if (pref == 'Webpage' or pref == 'webpage'):
    link_func()
else:
    asin_number()
# if (asin == ''):
#     link_func()
# else:
#     asin_number()
# link_func()