# File: funct_2.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: functions for option 2
# Imported By: shopetfy.py

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

''' Get products filterd by user selected category, sorted by prices'''
def get_by_category(df,category):
    df_subset = df[(df['category'] == str(category)) & (df['price_new'] > 0)]
    df_result = df_subset.sort_values(by=['price_new'], ascending=True).reset_index()
    df_result = df_result[['name','message','price_new','channel']]
    return df_result

''' Display overlapping histogram for 2 channels'''
def display_graph(df):
    cheapest_amz = df[df['channel'] == 'amazon'].sort_values(by=['price_new'], ascending=True).reset_index()
    cheapest_cwy = df[df['channel'] == 'chewy'].sort_values(by=['price_new'], ascending=True).reset_index()
    cheapest_pst = df[df['channel'] == 'petsmarts'].sort_values(by=['price_new'], ascending=True).reset_index()
    top100_amz = cheapest_amz.head(100)
    top100_cwy = cheapest_cwy.head(100)
    top100_pst = cheapest_pst.head(100)
    plt.hist(top100_cwy['price_new'], 
            alpha=0.5, # the transaparency parameter
            label='Chewy',
            bins = 10)
    
    plt.hist(top100_amz['price_new'],
            alpha=0.5,
            label='Amazon',
            bins = 10)

    plt.hist(top100_pst['price_new'],
            alpha=0.5,
            label='Petsmart',
            bins = 10)

    plt.legend(loc='upper right')
    plt.title('Overlapping Lowest Prices Histogram')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
