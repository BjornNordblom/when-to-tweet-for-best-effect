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

