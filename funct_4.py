# File: funct_4.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: functions for option 4
# Imported By: shopetfy.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''4)  Display summary by category, counts, user input keyword (Halloween) as filter'''

#filter the dataframe with the keyword
def fil_keyword(df, keyword):
    df_subset = df[df['name'].str.contains(keyword)]
    return df_subset

# price distribution in both categories
def draw(df):
    df_toys = df[df['category'] == 'toys']
    df_treats = df[df['category'] == 'treats']
    plt.hist(df_toys['price_new'],
             alpha=0.5,
             label='Toys',
             bins=10)

    plt.hist(df_treats['price_new'],
             alpha=0.5,
             label='Treats',
             bins=10)
    plt.legend(loc='upper right')
    plt.title('Designated Product Prices Histogram By Category')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
    print()

#the amount of products in both categories
def amount_cate(df):
    df_toys = df[df['category'] == 'toys']
    df_treats = df[df['category'] == 'treats']
    toys_amount = df_toys.shape[0]
    treats_amount = df_treats.shape[0]
    print("The amount of designated products in both categories: ")
    print('Toys:', toys_amount, '\n' + 'Treats:', treats_amount)

#the lowest price of product
def lowest_cate(df, key_words):
    df_toys = df[df['category'] == 'toys']
    df_treats = df[df['category'] == 'treats']
    if (key_words == 'toys'):
        df_category = df_toys
    else:
        df_category = df_treats
    df_category.sort_values(by=['price_new'], ascending=True).reset_index()
    if(df_category.shape[0]==0):
        print("No Such Product")
    else:
        print('The lowest price of product in this category and its channel:\n', df_category.iloc[0]['name'], 'is',
          df_category.iloc[0]['price_new'], 'dollars from', df_category.iloc[0]['channel'])
