# File: pet_data.py
# Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
# Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
# Purpose: automatically pulls and cleans pet characteristics data
# Imported By: funct5.py

# import modules
import requests
import json
import pandas as pd
import numpy as np

# call Dog API (all breeds endpoint)
url = "https://api.thedogapi.com/v1/breeds"
payload={}
files={}
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload, files=files)

# json to df
df = pd.read_json(response.text)
df = pd.json_normalize(response.json())

# replace characters
df = df.replace(' – ',' - ', regex=True)
df = df.replace('up','', regex=True)
df = df.replace('NaN','', regex=True)

# split columns by '-' to get min and max
df[['lifespan_min', 'lifespan_max']] = df['life_span'].str.lower().str.strip(" years").str.split(" - ", expand=True)
df[['imperial_weight_min', 'imperial_weight_max']] = df['weight.imperial'].str.split(" - ", expand=True)
df[['imperial_height_min', 'imperial_height_max']] = df['height.imperial'].str.split(" - ", expand=True)
df[['metric_weight_min', 'metric_weight_max']] = df['weight.metric'].str.split(" - ", expand=True)
df[['metric_height_min', 'metric_height_max']] = df['height.metric'].str.split(" - ", expand=True)

# replace columns with no max with their respective min value
df.loc[df['life_span_max'] == '', 'life_span_max'] = df['life_span_min']
df.loc[df['imperial_weight_max'] == '', 'imperial_weight_max'] = df['imperial_weight_min']
df.loc[df['imperial_height_max'] == '', 'imperial_height_max'] = df['imperial_height_min']
df.loc[df['metric_weight_max'] == '', 'metric_weight_max'] = df['metric_weight_min']
df.loc[df['metric_height_max'] == '', 'metric_height_max'] = df['metric_height_min']

# divide range to get mid value
# df['imperial_weight_mid'] = (df['imperial_weight_max'] + df['imperial_weight_max']) / 2
# df['imperial_height_mid'] = (df['imperial_height_max'] + df['imperial_height_max']) / 2
# df['metric_weight_mid'] = (df['metric_weight_max'] + df['metric_weight_max']) / 2
# df['metric_height_mid'] = (df['metric_height_max'] + df['metric_height_max']) / 2
# pet_df['life_span_mid'] = (pet_df['life_span_max'] + pet_df['life_span_max']) / 2

# save raw data to json file
# with open('pet_raw.json', 'w', encoding='utf-8') as f:
#     json.dump(response.json(), f, ensure_ascii=False, indent=4)

# save df to csv
df.to_csv('data/pet_characteristics/pet_cleaned_auto.csv', index='False')