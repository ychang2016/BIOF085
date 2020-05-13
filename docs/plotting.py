#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abhijit
"""
#%% preamble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-notebook')

#%% datasets

mtcars = pd.read_csv('data/mtcars.csv')
diamonds = pd.read_csv('data/diamonds.csv.gz')
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')
fmri = sns.load_dataset('fmri')

#%% Univariate

mtcars.plot(y = 'mpg', kind = 'hist')
plt.show()

mtcars.plot.hist( y = 'mpg')
mtcars['mpg'].plot.hist()

mtcars.plot(y = 'mpg', kind = 'kde')

mtcars['cyl'].value_counts().plot.bar()

sns.distplot(mtcars['mpg'], kde = False)
sns.distplot(mtcars['mpg'], kde=True, hist=False)

sns.countplot(data = mtcars, x = 'cyl', color = 'blue')

ordered_color = ['E','F','G','H','I','J']
sns.catplot(data=diamonds, x = 'color', 
            kind = 'count', color = 'blue',
            order = ordered_color)

iris.plot(kind = 'box')

#%% Bivariate

diamonds.head()
diamonds.plot(x = 'carat', y = 'price', kind = 'scatter')

sns.scatterplot(data = diamonds, x = 'carat', y = 'price')
sns.jointplot(data = diamonds, x = 'carat', y = 'price', kind = 'scatter')

diamonds.plot(x = 'carat', y = 'price', kind = 'hex')

sns.jointplot(data = diamonds, x = 'carat', y = 'price', kind = 'hex')

# Boxplots

diamonds.boxplot(column = 'price', by = 'color')

ordered_color = ['D','E','F','G','H','I','J']

sns.catplot(data=diamonds, x = 'color', y = 'price', 
            kind = 'box', order = ordered_color)

ordered_cuts = ['Fair','Good', 'Very Good', 'Premium', 'Ideal']
sns.catplot(data=diamonds, x = 'cut', y = 'price', 
            kind = 'box', order = ordered_cuts)

sns.catplot(data=diamonds, x = 'cut', y = 'price', 
            kind = 'violin', order = ordered_cuts)

#%% colors


iris.head()

sns.scatterplot(data = iris, x = 'sepal_width', 
                y = 'sepal_length', 
                hue = 'species')

ts = pd.read_csv('data/ts.csv')

ts_wide = ts.pivot(index = 'dt', columns = 'kind', values = 'value')

ts_wide.boxplot()

ts_wide.plot()

g = sns.FacetGrid(ts, hue='kind', height=5, aspect = 1.5)
g.map(plt.plot, 'dt', 'value').add_legend()

sns.scatterplot(data = diamonds, x = 'carat', y = 'price', 
                hue = 'color')

sns.scatterplot(data = diamonds, x = 'carat', y = 'price', 
                hue = 'color', size = 'depth')


#%% Facets

g = sns.FacetGrid(iris, col = 'species', hue = 'species', height = 5)
g.map(plt.scatter, 'sepal_width', 'sepal_length')

sns.relplot(data = iris, x = 'sepal_width', y = 'sepal_length',
                hue = 'species', col = 'species')


sns.relplot(x = 'timepoint', y = 'signal', data = fmri,
             col = 'region', row = 'event', height = 3)


sns.relplot(x = 'timepoint', y = 'signal', data = fmri,
             col = 'region', row = 'event', height = 3, 
             kind = 'line')

sns.relplot(x = 'timepoint', y = 'signal', data = fmri,
             col = 'region', row = 'event', height = 3, 
             kind = 'line', hue = 'subject')


sns.relplot(x = 'timepoint', y = 'signal', data = fmri,
             col = 'subject', col_wrap = 5, height = 3, 
             kind = 'line', hue = 'event', style = 'event')


g = sns.FacetGrid( data =  diamonds, row = 'color', 
                  height = 1.7, aspect = 4)
g.map(sns.distplot, 'price', hist = False, rug = True)



ans = sns.load_dataset('anscombe')
g = sns.FacetGrid(data = ans, col = 'dataset', col_wrap = 2)
g.map(sns.regplot, 'x', 'y', ci = None)

#%% pairs

sns.pairplot(iris, diag_kind = 'kde', hue = 'species')

g = sns.PairGrid(iris, diag_sharey=False)
g.map_lower(sns.kdeplot, colors = 'C0')
g.map_upper(sns.scatterplot)
g.map_diag(sns.kdeplot)


g = sns.PairGrid(diamonds, diag_sharey=False)
g.map_lower(sns.kdeplot, colors = 'C0')
g.map_upper(sns.scatterplot)
g.map_diag(sns.kdeplot)


#%% theme

plt.style.use('tableau-colorblind10')
ordered_color = ['E','F','G','H','I','J']
sns.catplot(data=diamonds, x = 'color', 
            kind = 'count', 
            order = ordered_color)

#%%

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim = [-10000, 140000], xlabel = 'Total revenue', 
       ylabel = 'Company', title = 'Company Revenue')

fig.savefig('sales.png', dpi = 300, bbox_inches = 'tight')











