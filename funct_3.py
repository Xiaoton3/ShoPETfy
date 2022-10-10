# File: funct_3.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: functions for option 3
# Imported By: shopetfy.py

import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from wordcloud import WordCloud

df = pd.read_csv("data/clean/df_final.csv")

''' Get the subset of data based on users' pets size'''
def get_by_size(df, size_str):
    df_subset = df[(df['size'].str.contains(size_str))  & (df['review']>0)]
    df_subset = df_subset[['brand','name','message','price_new','channel','review']]
    return df_subset

''' Get the top 10 products based on reviews or price based on users' choice'''
def recommand_by(df_subset, user_reco_choice):
    #recommendation by reviews
    if user_reco_choice == '1':
        df_result = df_subset.sort_values(by=['review'], ascending = False).reset_index()
        df_result = df_result[['brand','name','message','price_new','channel','review']]
        print(tabulate(df_result.head(10), headers = 'keys', tablefmt='psql'))
        brand_word_cloud = WordCloud().generate(' '.join(df_result['brand'].dropna()))
        plt.imshow(brand_word_cloud)
        plt.axis("off")
        plt.show()
    #recommendation by price
    elif user_reco_choice == '2':
        df_result = df_subset.sort_values(by=['price'], ascending = True).reset_index()
        df_result = df_result[['brand','name','message','price_new','channel','review']]
        print(tabulate(df_result.head(10), headers = 'keys', tablefmt='psql'))
        brand_word_cloud = WordCloud().generate(' '.join(df_result['brand'].dropna()))
        plt.imshow(brand_word_cloud)
        plt.axis("off")
        plt.show()

'''Based on the size of users' pets, display all informations about the top 20 products in different channel.'''
def summary_by_size(df_subset):
    df_result = df_subset.sort_values(by=['review'], ascending = False).reset_index()
    #show the top 20 product in chosen size
    print(tabulate(df_result.head(20), headers = 'keys', tablefmt='psql'))
    #diaplay using plots
    most_popular_amz = df_result[df_result['channel'] == 'amazon'].head(20) 
    print(most_popular_amz.head(10))  
    most_popular_chewy = df_result[df_result['channel'] == 'chewy'].head(20)
    most_popular_petsmarts = df_result[df_result['channel'] == 'petsmarts'].head(20)
    plt.hist(most_popular_amz['price_new'], alpha = 0.5, label = 'Amazon')
    plt.hist(most_popular_chewy['price_new'], alpha = 0.5, label = 'Chewy')
    plt.hist(most_popular_petsmarts['price_new'], alpha = 0.5, label = 'PetSmarts')
    plt.title('The most popular product in three channel based on your size choice')
    plt.legend()
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
