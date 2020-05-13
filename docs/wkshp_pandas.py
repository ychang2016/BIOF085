#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:52:50 2020

@author: abhijit
"""

#%% preamble

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

mtcars = pd.read_csv('data/mtcars.csv')
mtcars.dtypes

s= pd.Series([1,3,5,np.nan, 9, 13])
s2 = pd.Series( np.arange(1,20))

s2[4]

s3 = pd.Series(np.random.normal(0, 1, 5),
               index = ['a','b','c','d','e'])

#%% data frame

rng = np.random.RandomState(25)
d1 = pd.DataFrame(rng.normal(0, 1, (4,5)))

d1.columns
d1.columns = ['V' + str(i) for i in range(1,6)]

df = pd.DataFrame({
    'A': 3.,
    'B': rng.random_sample(5), 
    'C': pd.Timestamp('20200512'), 
    'D': np.array([6]*5),
    'E': pd.Categorical(['y','n','n','y','n']),
    'F': 'NIH'})


#%%
df = pd.DataFrame(np.random.randn(5, 3), index = ['a','c','e', 'f','g'], columns = ['one','two','three']) # pre-specify index and column names
df['four'] = 20 # add a column named "four", which will all be 20
df['five'] = df['one'] > 0
df
df2 = df.reindex(['a','b','c','d','e','f','g'])
df2


df2.isna()

df2['one'].notna()

df2.dropna(how='any')

df2.fillna(5)
df3 = df2.copy()
df3 = df3.select_dtypes(exclude=[object])

df3.fillna(df3.mean())




