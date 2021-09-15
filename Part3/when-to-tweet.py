# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:53:59 2021

@author: BjornN
"""


import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd
import datetime
from datetime import date

# import os
# os.chdir("c:\\temp\\when-to-tweet-for-best-effect")

df = pd.read_csv("tweet_engagements.csv")
df.info()
df.describe()
df.dtypes

###

df["Date"] = pd.to_datetime(df["Date"])
calendar = [date.isocalendar(d) for d in df["Date"]]
df["Week"] = [c[1] for c in calendar]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df["Weekday"] = [days[c[2]-1] for c in calendar]
df["Rate"] = df["Engagement"] / df["Impression"]

df_pivot = df.pivot_table(index="Week", aggfunc="sum", columns="Weekday", values="Engagement").dropna()

df_pivot

def p_val(data_array_a,data_array_b):
    extreme_mean_diff = abs(np.mean(data_array_a) - np.mean(data_array_b))
    
    total_data = np.hstack([data_array_a, data_array_b])
    number_extreme_values = 0.0
    for _ in range(30000):
        np.random.shuffle(total_data)
        sample_a = total_data[:data_array_a.size]
        sample_b = total_data[data_array_a.size:]
        if abs(sample_a.mean() - sample_b.mean()) > extreme_mean_diff:
            number_extreme_values += 1

    p_value = number_extreme_values / 30000
    return p_value

df_pivot['Friday']
df_pivot[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']]
p_vals = {}
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']:
    p_vals[day] = p_val(df_pivot['Friday'],df_pivot[day])

p_vals
