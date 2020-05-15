#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:13:14 2020

@author: abhijit
"""


import numpy as np
import pandas as pd

gapminder = pd.read_csv('data/gapminder.tsv', sep='\t')

gapminder[:5]
gapminder.head(5)

new_gm = gapminder[['country','gdpPercap','lifeExp']]

canada = gapminder.query('country=="Canada"')
canada = gapminder[gapminder['country']=='Canada']
canada = gapminder.groupby('country').get_group('Canada')

mtcars = pd.read_csv('data/mtcars.csv')
mtcars['kml'] = mtcars['mpg'] * 1.6/3.8

from glob import glob
fnames = glob('data/survey*.csv')

visited, person, site, survey = [pd.read_csv(f) for f in fnames]
d1 = pd.merge(survey, visited, how='inner', left_on = 'taken', right_on = 'ident')
d2 = pd.merge(survey, person, how = 'outer', left_on = 'person', right_on = 'ident')

weather = pd.read_csv('data/weather.csv')

## I will melt the data so tha tthe days become a column and their corresponding
## temperatures become a column. Then I'll pivot so that the values of element become column headers

d1 = pd.melt(weather, id_vars = ['id','year','month','element'])
#d2 = pd.pivot_table(weather, index = ['id','year','month','variable'], values = 'value')


gapminder.groupby(['continent','year'])['gdpPercap'].median()
