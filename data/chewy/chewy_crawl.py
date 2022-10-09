# File: chewy_crawl.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: Scrape chewy.com and get product information saved in a file
# Imported By: shopefy.py

import requests
import bs4
import re
import pandas as pd

url = "https://www.chewy.com/b/treats_c335"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"referer": "https://www.chewy.com/"}

#res = requests.get(url, timeout=5, headers=headers)

def find_number(s):
    match_res = re.match(r'^\$[0-9]+(\.)?[0-9]*', s)
    if match_res:
        return match_res.group(0)
    return None

def find_review_number(s):
    re_count = ""
    for c in s:
        if '0' <= c <= '9':
            re_count += c
    return int(re_count)

'''Scrape one page of chewy data'''
def scrape_one_page(res_content, items):
    soup = bs4.BeautifulSoup(res_content, 'html.parser')
    page_one_items = soup.find_all("div", {"class": "kib-product-card__content"})  
    
    for item in page_one_items:
        item_dicc = {"brand": "", "name": "", "price": -1, "review": -1, "message": ""}
        # Get the name of the product
        title_div = item.find_all("div", {"class": "kib-product-title__text"})
        if len(title_div) > 0:
            title_strong = title_div[0].find_all("strong")
            if len(title_strong) > 0:
                prod_name = title_strong[0].string
                item_dicc["brand"] = prod_name
            item_dicc["name"] = title_div[0].text
        # Get the price
        price_div = item.find_all("div", {"class": "kib-product-price"})
        if len(price_div) > 0:
            prod_price = find_number(price_div[0].text)
            if prod_price:
                item_dicc["price"] = prod_price
        # Get the rating count
        rating_count_div = item.find_all("span", {"class": "kib-product-rating__count"})
        if len(rating_count_div) > 0:
            item_dicc["review"] = find_review_number(rating_count_div[0].text)
        # Get product message
        prod_info_msg = item.find_all("p", {"class": "kib-product-message"})
        if len(prod_info_msg) > 0:
            item_dicc["message"] = prod_info_msg[0].text
        # Append the item
        items.append(item_dicc)

def scrape_all(items, page_number, url_prefix, headers):
    for i in range(page_number):
        url = url_prefix + "_p" + str(i+1)
        res = requests.get(url, timeout=5, headers=headers)
        res_content = res.content
        scrape_one_page(res_content, items)
        print("page{0}".format(i+1))

'''main function to scrape data by number of pages to scrape'''
def main(items, page_num):
    # Main part to scrape the page
    #url_prefix = "https://www.chewy.com/b/toys_c315" # change this to change category
    url_prefix = "https://www.chewy.com/b/treats_c335"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "referer": "https://www.chewy.com/"}
    scrape_all(items, page_num, url_prefix, headers)

# all_page_items = []
# main(all_page_items, 100)
# pd.DataFrame(all_page_items).to_csv("chewy_dog_treats_info.csv", index=False)

'''Search for a word then return one page of product'''
def search_and_return(term):
    url = "https://www.chewy.com/s"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "referer": "https://www.chewy.com/"}
    params = {"query": term}
    res = None
    try:
        res = requests.get(url, headers=headers, params=params, timeout=5)
    except:
        print("[ERROR] Connection error")
        return []
    if not res.ok:
        print("[ERROR] Connection error")
        return []
    search_res_items = []
    res_content = res.content
    scrape_one_page(res_content, search_res_items)
    return search_res_items

# Input search word
def chewy_search(term):
    item_list = search_and_return(term)
    pd.DataFrame(item_list).to_csv("chewy_search_term.csv", index=False)