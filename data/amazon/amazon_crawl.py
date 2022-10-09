import requests
import bs4
import re
import pandas as pd

def find_number(s):
    match_res = re.match(r'^\$[0-9]+(\.)?[0-9]*', s)
    if match_res:
        return match_res.group(0)
    return None


def scrape_one_page(res_content, items):
    soup = bs4.BeautifulSoup(res_content, 'lxml')
    page_one_items = soup.find_all("div", {
        "class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})
    # name, deal, price, arrival date information , (Amazon's number of reviews and rating are both picture qaq )
    for item in page_one_items:
        item_dicc = {"name": "", "deal_info": "", "price": -1, "arr_info": ""}
        # name
        title_div = item.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
        if len(title_div) > 0:
            item_dicc["name"] = title_div[0].text

            # deal
        deal_div = item.find_all("span", {"class": "a-badge-text"})
        if len(deal_div) > 0:
            item_dicc["deal_info"] = deal_div[0].text
        else:
            item_dicc["deal_info"] = "no discount"

        # price
        price_div = item.find_all("span", {"class": "a-offscreen"})
        if len(price_div) > 0:
            prod_price = find_number(price_div[0].text)
            if prod_price:
                item_dicc["price"] = prod_price

        # arrival date information
        arr_div = item.find_all("span", {"class": "a-color-base a-text-bold"})
        if len(arr_div) > 0:
            item_dicc["arr_info"] = arr_div[0].text
        items.append(item_dicc)


def scrape_all(items, page_number, url_prefix, headers):
    for i in range(page_number):
        url = url_prefix + "_pg_" + str(i+1)
        res = requests.get(url, timeout=5,headers = headers)
        res_content = res.content
        scrape_one_page(res_content, items)

def main(items,page_num,catagory):
    url_prefix = "https://www.amazon.com/s?k="+catagory+"&i=pets&rh=n%3A2975434011&page=2&c=ts&qid=1663384591&ts_id=2975434011&ref=sr"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
          "referer":"https://www.amazon.com"}
    scrape_all(items,page_num,url_prefix,headers)

#scrape treats and toys
ctg = ["Dog+Toys","Dog+Treats"]
for i in range(len(ctg)):
    all_page_items = []
    main(all_page_items, 100, ctg[i])
    pd.DataFrame(all_page_items).to_csv('amazon_'+ctg[i]+'_info.csv', index = False, header = True)
