import pandas as pd
import numpy as np
import re

def get_by_category(df,category):
    df['price_new'] = df.apply(lambda x : float(re.sub(r'((?<=\d),(?=\d))|(\$(?=\d))', r'', x['price'])),axis=1)
    df_subset = df[(df['category'] == str('toys')) & (df['price_new'] > 0)]
    df_result = df_subset.sort_values(by=['price_new'], ascending=True).reset_index()
    df_result = df_result[['brand','name','discount','price_new']]
    print(df_result.head(10))
