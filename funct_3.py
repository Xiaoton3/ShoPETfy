import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funct_2 import get_by_category, display_graph
from wordcloud import WordCloud
from IPython.display import display
# 1. display all stuffs
# 2. display price range
df = pd.read_csv("data/clean/df_final.csv")
#def summary_by_size(size_input):

def get_by_size(df, size_str):
    df_subset = df[(df['size'].str.contains(size_str))  & (df['review']>0)]
    return df_subset

def recommand_by(df_subset, user_reco_choice):
    #recommendation by reviews
    if user_reco_choice == '1':
        df_result = df_subset.sort_values(by=['review'], ascending = False).reset_index()
        df_result = df_result[['brand','name','message','price_new','channel','review']]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        display(df_result.head(10))
        brand_word_cloud = WordCloud().generate(' '.join(df_result['brand'].dropna()))
        plt.imshow(brand_word_cloud)
        plt.axis("off")
        plt.show()
    #recommendation by price
    elif user_reco_choice == '2':
        df_result = df_subset.sort_values(by=['price'], ascending = True).reset_index()
        df_result = df_result[['brand','name','message','price_new','channel','review']]
        display(df_result.head(10))
        brand_word_cloud = WordCloud().generate(' '.join(df_result['brand'].dropna()))
        plt.imshow(brand_word_cloud)
        plt.axis("off")
        plt.show()
def summary_by_size(df_subset):
    df_result = df_subset.sort_values(by=['review'], ascending = False).reset_index()
    #show the top 20 product in chosen size
    display(df_result.head(20))
    #diaplay using plot
    most_popular_amz = df_result[df_result['channel'] == 'amazon'].head(20)   
    most_popular_chewy = df_result[df_result['channel'] == 'chewy'].head(20)
    most_popular_petsmarts = df_result[df_result['channel'] == 'petsmarts'].head(20)
    plt.hist(most_popular_amz['price'], alpha = 0.5, label = 'Amazon')
    plt.hist(most_popular_chewy['price'], alpha = 0.5, label = 'Chewy')
    plt.hist(most_popular_petsmarts['price'], alpha = 0.5, label = 'PetSmarts')
    plt.title('The most popular product in three channel based on your size choice')
    plt.legend()
    
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
