import pandas as pd
import numpy as np
import os
import re
os.chdir("..")

df_chewy_toys = pd.read_csv('chewy/chewy_dog_toys_info.csv')
df_chewy_treats = pd.read_csv('chewy/chewy_dog_treats_info.csv')
df_amazon_toys = pd.read_csv('amazon/amazon_dog_toys_info.csv')
df_amazon_treats = pd.read_csv('amazon/amazon_dog_treats_info.csv')
df_petsmart_toys = pd.read_csv('Petsmart/PetSmart_dog_toy_info_c.csv')
df_petsmart_treats = pd.read_csv('Petsmart/PetSmart_dog_treats_info_c.csv')

# drop first index column
df_petsmart_toys = df_petsmart_toys.iloc[: , 1:]
df_petsmart_treats = df_petsmart_treats.iloc[: , 1:]

df_chewy_toys['category'] = 'toys'
df_chewy_treats['category'] = 'treats'
df_amazon_toys['category'] = 'toys'
df_amazon_treats['category'] = 'treats'
df_petsmart_toys['category'] = 'toys'
df_petsmart_treats['category'] = 'treats'

# assign channel info
df_chewy = pd.concat([df_chewy_toys, df_chewy_treats], ignore_index=True, sort=False)
df_chewy['channel'] = 'chewy'
# only keep data that has valid brand and name info
df_chewy = df_chewy[(df_chewy['brand'].str.len() > 0) & (df_chewy['name'].str.len() > 0)]

# handle amazon data
df_amazon = pd.concat([df_amazon_toys, df_amazon_treats], ignore_index=True, sort=False)
df_amazon['channel'] = 'amazon'
# drop arr_info (dates)
df_amazon = df_amazon.drop(['arr_info'],axis=1)
#rename the columns, add missing info
#Index(['brand', 'name', 'price', 'review', 'message', 'category', 'channel'], dtype='object')
df_amazon['brand'] = 'N/A'
df_amazon['review'] = 'N/A'
df_amazon = df_amazon.rename(columns={'deal_info': 'message'})
df_amazon = df_amazon.reindex(['brand','name','price','review','message','category','channel'], axis=1)

df_combine = pd.concat([df_amazon, df_chewy], ignore_index=True, sort=False)
df_combine[df_combine['category'] == 'toys']

df_petsmarts = pd.concat([df_petsmart_toys, df_petsmart_treats], ignore_index=True, sort=False)
df_petsmarts['channel'] = 'petsmarts'
#Index(['brand', 'name', 'price', 'review', 'discount', 'category', 'channel'], dtype='object')
df_petsmarts['brand'] = 'N/A'
df_petsmarts = df_petsmarts.reindex(['brand','name','price','review','message','category','channel'], axis=1)
df_combine = pd.concat([df_combine, df_petsmarts], ignore_index=True, sort=False)

# add size (small, medium, large)
def findSize(s):
    s = s.lower()
    size_list = []
    if 'small' in s:
        size_list.append('S')
    if 'medium' in s:
        size_list.append('M')
    if 'large' in s:
        size_list.append('L')
    return size_list

df_combine['size'] = df_combine.apply(lambda x : findSize(x['name']),axis=1)
df_combine = df_combine[df_combine['price'] != '-1']
# see if the price has clear price or range
new_price = []
for p in df_combine['price']:
    if p.find('-') != -1:
        # split by -, get the first index
        first_price = p.split('-')[0]
        p = float(re.sub(r'((?<=\d),(?=\d))|(\$(?=\d))', r'', first_price))
    else:
        p = float(re.sub(r'((?<=\d),(?=\d))|(\$(?=\d))', r'', p))
    new_price.append(p)
# add new price to df
df_combine['price_new'] = new_price
# save csv
df_combine.to_csv('clean/df_final.csv',index=False)