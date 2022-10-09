# File: funct_1.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: functions for option 1
# Imported By: shopetfy.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud

# import data
pet_df = pd.read_csv('data/pet_characteristics/pet_cleaned.csv')

# divide (min + max) to get mid value
pet_df['imperial_weight_mid'] = (pet_df['imperial_weight_max'] + pet_df['imperial_weight_max']) / 2
pet_df['imperial_height_mid'] = (pet_df['imperial_height_max'] + pet_df['imperial_height_max']) / 2
pet_df['metric_weight_mid'] = (pet_df['metric_weight_max'] + pet_df['metric_weight_max']) / 2
pet_df['metric_height_mid'] = (pet_df['metric_height_max'] + pet_df['metric_height_max']) / 2
pet_df['life_span_mid'] = (pet_df['life_span_max'] + pet_df['life_span_max']) / 2

# binning by weight (imperial weight)
pet_df['size'] = pd.cut(pet_df['imperial_weight_mid'], bins = [0, 23, 55, 200], labels = ['small', 'medium', 'large'] )


# Functions for Option 1
def get_stats_by_size():
    # plot 3 boxplots (for height, weight and size)
    fig, ax = plt.subplots(nrows=1, ncols=3)
    pet_df.boxplot(column='imperial_height_mid', by='size', ax=ax[0])
    pet_df.boxplot(column='imperial_weight_mid', by='size', ax=ax[1])
    pet_df.boxplot(column='life_span_mid', by='size', ax=ax[2])
    plt.tight_layout()
    plt.show()

# Functions for Option 2
def is_valid_breed(breed):
    # check if breed exists in data
    return pet_df['name'].str.contains(breed, case = False).any()

def get_stats_by_breed(breed):
    # get stats for breed
    out_df = pet_df[pet_df['name'].str.contains(breed, case = False)]
    out_df = out_df[['name', 'imperial_weight_mid', 'imperial_height_mid', 'life_span_mid', 'temperament']]
    out_df = out_df.rename(columns = {
        'name': 'Breed Name', 
        'imperial_weight_mid': 'Weight (pounds)', 
        'imperial_height_mid': 'Height (feet)',
        'life_span_mid': 'Life Span (years)',
        'temperament': 'Temperament'
        })
    return out_df