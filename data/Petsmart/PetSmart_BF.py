import requests
import bs4
import pandas as pd
#url = "https://www.petsmart.com/dog/toys/"
url = "https://www.petsmart.com/dog/treats/"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"referer": "https://www.petsmart.com/"}


res = requests.get(url, timeout=5, headers=headers)

import re
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

def scrape_one_page(res_content, items):
    soup = bs4.BeautifulSoup(res_content, 'html.parser')
    page_one_items = soup.find_all("div", {"class": "product-tile"})  
    
    for item in page_one_items:
        item_dicc = {"name": "", "price": -1, "review": -1, "message": ""}
        # Get the name of the product
        title_div = item.find_all("div", {"class": "product-name"})
        if len(title_div) > 0:
            item_dicc["name"] = title_div[0].text
        # Get the price
        price_div = item.find_all("span", {"class": "price-regular"})
        if len(price_div) > 0:
            item_dicc["price"] = price_div[0].text
        else:
            price_sale_div = item.find_all("span", {"class": "price-sales"})
            if len(price_sale_div) > 0:
                item_dicc["price"] = price_sale_div[0].text
        # Get the rating count
        rating_count_div = item.find_all("div", {"class": "bv-review-count"})
        if len(rating_count_div) > 0:
            item_dicc["review"] = find_review_number(rating_count_div[0].text)
        # Get product message
        prod_info_msg = item.find_all("div", {"class": "promotional-message"})
        if len(prod_info_msg) > 0:
            item_dicc["message"] = prod_info_msg[0].text #prod_info_msg[1].text
        # Append the item
        items.append(item_dicc)

res = requests.get(url, timeout=5, headers=headers)

res_content = res.content
items = []
scrape_one_page(res_content, items)

def scrape_all(items, page_number, url_prefix, headers):
    for i in range(page_number):
        url = url_prefix + str(24*(i)) + '&sz=24&format=ajax'
        res = requests.get(url, timeout=5, headers=headers)
        res_content = res.content
        scrape_one_page(res_content, items)
        print("page{0}".format(i+1))

def main(items, page_num):
    # Main part to scrape the page
    url_prefix = "https://www.petsmart.com/dog/treats/?pmin=0.01&srule=best-sellers&start="
    #url_prefix = "https://www.petsmart.com/dog/toys/?pmin=0.01&srule=best-sellers&start="
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "referer": "https://www.petsmart.com/"}
    scrape_all(items, page_num, url_prefix, headers)

all_page_items = []
main(all_page_items, 44)

pd.DataFrame(all_page_items).to_csv("PetSmart_dog_treats_info.csv", index=False)