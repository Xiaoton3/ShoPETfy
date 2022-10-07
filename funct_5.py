# File: funct_5.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: functions for option 5
# Imported By: shopetfy.py

import pandas as pd
import numpy as np
import re

'''Cleans the price column of the scraped data'''
def clean_df(df):
    df = df[df['price'] != '-1']
    new_price = []
    for p in df['price']:
        if len(p) > 1:
            if p.find('-') != -1:
                # split by -, get the first index
                first_price = p.split('-')[0]
                p = float(re.sub(r'((?<=\d),(?=\d))|(\$(?=\d))', r'', first_price))
            else:
                p = float(re.sub(r'((?<=\d),(?=\d))|(\$(?=\d))', r'', p))
            new_price.append(p)
    df['price_new'] = new_price
    return df

'''Sorts the scraped product data by price, returns the 10 cheapest products'''
def sort_by_price(df):
    df_result = df.sort_values(by=['price_new'], ascending=True).reset_index()
    df_result = df_result[['brand','name','message','price_new']]
    return df_result.head(10)