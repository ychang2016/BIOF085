# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,Rmd
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Statistical analysis
#
# ## Introduction
#
# Statistical analysis usually encompasses 3 activities in a data science workflow. These are (a) descriptive analysis, (b) hypothesis testing and (c) statistical modeling. Descriptive analysis refers to a description of the data, which includes computing summary statistics and drawing plots. Hypothesis testing usually refers to statistically seeing if two (or more) groups are different from each other based on some metrics. Modeling refers to fitting a curve to the data to describe the relationship patterns of different variables in a data set
#
# In terms of Python packages that can address these three tasks:
#
# | Task                   | Packages               |
# | ---------------------- | ---------------------- |
# | Descriptive statistics | pandas, numpy          |
# | Hypothesis testing     | scipy, statsmodels     |
# | Modeling               | statsmodels, lifelines |
#

# %% [markdown]
# ## Descriptive statistics

# %% [markdown]
# Descriptive statistics that are often computed are the mean, median, standard deviation, inter-quartile range, pairwise correlations, and the like. Most of these functions are available in `numpy`, and hence are available in `pandas`. We have already seen how we can compute these statistics and have even computed grouped statistics. For example, we will compute these using the diamonds dataset

# %%
import numpy as np
import scipy as sc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
diamonds = pd.read_csv('data/diamonds.csv.gz')

# %%
diamonds.groupby('color')['price'].agg([np.mean, np.median, np.std])

# %% [markdown]
# There were other examples we saw yesterday along these lines. 

# %% [markdown]
# ## Hypothesis testing
#
# Hypothesis testing is one of the areas where statistics is often used. There are functions for a lot of the standard statistical tests in `scipy` and `statsmodels`. However, I'm going to take a little detour to see if we can get some understanding of hypothesis tests using the powerful simulation capabilities of Python.

# %% [markdown]
# You have a coin and you flip it 100 times. You get 54 heads. How likely is it that you have a fair coin?
#
# We can simulate this process, which is random, using Python. The process of heads and tails from coin tosses can be modeled as a **binomial** distribution. So we can repeat this experiment many many times on our computer, assuming we have a fair coin,  and then see how likely what we observed is. 

# %%
rng = np.random.RandomState(205)

x = rng.binomial(100, 0.5, 100000)

sns.distplot(x)
plt.axvline(54, color = 'r')

# %%
pd.Series(x).describe()

# %%
np.mean(x > 54)

# %% [markdown]
# This is what would be considered the *p-value* for the test that the coin is fair. 
#
# What happens if we increase the number of tosses, and we look at the proportion of heads. We observe 54% heads.

# %%
rng = np.random.RandomState(205)
x = rng.binomial(10000, 0.5, 100000)/10000
sns.distplot(x)
plt.axvline(0.54, color = 'r')

# %%
pd.Series(x).describe()

# %%
np.mean(x > 0.54)

# %%
rng = np.random.RandomState(205)
x = rng.binomial(100, 0.54, 100000)/100
sns.distplot(x)
plt.axvline(0.54, color = 'r')

# %%
pd.Series(x).describe()

# %% [markdown]
# This is showing that as we increase the number of tosses, we get more robust signals about the coin. With 1000 tosses we see evidence that the coin is not fair, however small the unfairness is. This is related to the issue of statistical power. As we get more evidence, we can be more confident about what we are seeing. 

# %% [markdown]
# We can use simulation to make better inference about differences between groups, or to get confidence intervals for a parameter of interest, without making assumptions about distributions or having to test for distributions. Python allows us to do that quickly and efficiently.

# %% [markdown]
# ### A permutation test

# %% [markdown]
# A permutation test is a 2-group test that asks whether two groups are different with respect to some metric. Let us look at a breast cancer proteomics experiment to illustrate this. The experimental data contains protein expression for over 12 thousand proteins, along with clinical data. We can ask, for example, whether a particular protein expression differs by ER status. 

# %%
brca = pd.read_csv('data/brca.csv')
brca.head()

# %%
import scipy as sc
import statsmodels as sm

# %%
tst = sc.stats.ttest_ind(brca[brca['ER Status']=='Positive']['NP_001193600'], 
                   brca[brca['ER Status']=='Negative']['NP_001193600'], 
                  nan_policy = 'omit')
tst.pvalue

# %% [markdown]
# The idea about a permutation test is that, if there is truly no difference then it shouldn't make a difference if we shuffled the labels of ER status over the study individuals. That's literally what we will do. We will do this several times, and look at the average difference in expression each time. This will form the null distribution under our assumption of no differences by ER status. We'll then see where our observed data falls, and then be able to compute a p-value.

# %%
nsim = 10000
protein = 'NP_001193600'
rng = np.random.RandomState(294)
x = np.where(brca['ER Status']=='Positive', -1, 1)
y = brca[protein].to_numpy()

obs_diff = np.nanmean(y[x==1]) - np.nanmean(y[x==-1])

diffs = np.zeros(nsim)
for i in range(nsim):
    x1 = rng.permutation(x)
    diffs[i] = np.nanmean(y[x1==1]) - np.nanmean(y[x1 == -1])


# %%
sns.distplot(diffs)
plt.axvline(x = obs_diff, color ='r')

# %%
pval = np.mean(np.abs(diffs) > np.abs(obs_diff))
f"P-value from permutation test is {pval}"

# %% [markdown]
# ### Testing many proteins 
#
# We could do the permutation test all the proteins using the array operations in `numpy`

# %%
expr_names = [u for u in list(brca.columns) if u.find('NP') > -1]

exprs = brca[expr_names]

# %%
obs_diffs = exprs[x==1].mean(axis=0)-exprs[x==-1].mean(axis=0)

# %%
nsim = 1000
diffs = np.zeros((nsim, exprs.shape[1]))
for i in range(nsim):
    x1 = rng.permutation(x)
    diffs[i,:] =exprs[x1==1].mean(axis=0) - exprs[x1==-1].mean(axis=0)


# %%
pvals = np.zeros(exprs.shape[1])
len(pvals)

# %%
for i in range(len(pvals)):
    pvals[i] = np.mean(diffs[:,i] > obs_diffs.to_numpy()[i])

# %%
sns.distplot(pvals)

# %%
pd.Series(pvals).describe()

# %%
exprs_shortlist = [u for i, u in enumerate(list(exprs.columns)) if pvals[i] < 0.0001 ]

# %%
len(exprs_shortlist)

# %% [markdown]
# ## Regression analysis
#
# The regression modeling frameworks in Python are mainly in `statsmodels`, though some of it can be found in `scikit-learn` which we will see tomorrow. We will use the diamonds dataset for demonstration purposes. We will attempt to model the diamond price against several of the other diamond characteristics

# %%
import statsmodels.api as sm
import statsmodels.formula.api as smf

mod1 = smf.glm('price ~ carat + clarity + depth + cut + color', data = diamonds).fit()

# %%
mod1.summary()

# %% [markdown]
# This is the basic syntax for modeling in statsmodels. Let's go through and parse it. 
#
# One thing you notice is that we've written a formula inside the model
#
# ```
# mod1 = smf.glm('price ~ carat + clarity + depth + cut + color', data = diamonds).fit()
# ```
#
# This is based on another Python package, `patsy`, which allows us to write the model like this. This will read as 
# "price depends on carat, clarity, depth, cut and color". Underneath a lot is going on.
#
# 1. color, clarity, and cut are all categorical variables. They actually need to be expanded into dummy variables, so we will have one column for each category level, which is 1 when the diamond is of that category and 0 otherwise. 
# 1. An intercept terms is added
# 1. The dummy variables are concatenated to the continuous variables
# 1. The model is run
#
# We can see the dummy variables using `pandas`

# %%
pd.get_dummies(diamonds)
# %% [markdown]
#
#
