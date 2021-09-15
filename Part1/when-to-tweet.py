# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:53:59 2021

@author: BjornN
"""


import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd

# import os
# os.chdir("c:\\temp\\when-to-tweet-for-best-effect\\Part1")

df = pd.read_csv("..\\tweet_engagements.csv")
df.info()

df.describe()
