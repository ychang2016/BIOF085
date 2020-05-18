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

# %% [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#An-example-gallery" data-toc-modified-id="An-example-gallery-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>An example gallery</a></span></li><li><span><a href="#Why-visualize-data?" data-toc-modified-id="Why-visualize-data?-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Why visualize data?</a></span></li><li><span><a href="#Conceptual-ideas" data-toc-modified-id="Conceptual-ideas-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conceptual ideas</a></span><ul class="toc-item"><li><span><a href="#Begin-with-the-consumer-in-mind" data-toc-modified-id="Begin-with-the-consumer-in-mind-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Begin with the consumer in mind</a></span></li><li><span><a href="#Tell-a-story" data-toc-modified-id="Tell-a-story-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Tell a story</a></span></li><li><span><a href="#A-matter-of-perception" data-toc-modified-id="A-matter-of-perception-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>A matter of perception</a></span></li><li><span><a href="#Some-principles" data-toc-modified-id="Some-principles-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>Some principles</a></span></li></ul></li></ul></li><li><span><a href="#Plotting-in-Python" data-toc-modified-id="Plotting-in-Python-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Plotting in Python</a></span><ul class="toc-item"><li><span><a href="#Static-plots" data-toc-modified-id="Static-plots-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Static plots</a></span></li><li><span><a href="#Dynamic-or-interactive-plots" data-toc-modified-id="Dynamic-or-interactive-plots-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Dynamic or interactive plots</a></span></li></ul></li><li><span><a href="#Univariate-plots" data-toc-modified-id="Univariate-plots-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Univariate plots</a></span><ul class="toc-item"><li><span><a href="#pandas" data-toc-modified-id="pandas-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>pandas</a></span><ul class="toc-item"><li><span><a href="#Histogram" data-toc-modified-id="Histogram-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Histogram</a></span></li><li><span><a href="#Bar-plot" data-toc-modified-id="Bar-plot-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Bar plot</a></span></li><li><span><a href="#Density-plot" data-toc-modified-id="Density-plot-3.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Density plot</a></span></li></ul></li><li><span><a href="#seaborn" data-toc-modified-id="seaborn-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>seaborn</a></span><ul class="toc-item"><li><span><a href="#Histogram" data-toc-modified-id="Histogram-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Histogram</a></span></li><li><span><a href="#Bar-plot" data-toc-modified-id="Bar-plot-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Bar plot</a></span></li><li><span><a href="#Density-plot" data-toc-modified-id="Density-plot-3.2.3"><span class="toc-item-num">3.2.3&nbsp;&nbsp;</span>Density plot</a></span></li></ul></li></ul></li><li><span><a href="#Bivariate-plots" data-toc-modified-id="Bivariate-plots-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Bivariate plots</a></span><ul class="toc-item"><li><span><a href="#pandas" data-toc-modified-id="pandas-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>pandas</a></span><ul class="toc-item"><li><span><a href="#Scatter-plot" data-toc-modified-id="Scatter-plot-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Scatter plot</a></span></li><li><span><a href="#Box-plot" data-toc-modified-id="Box-plot-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Box plot</a></span></li></ul></li><li><span><a href="#seaborn" data-toc-modified-id="seaborn-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>seaborn</a></span><ul class="toc-item"><li><span><a href="#Scatter-plot" data-toc-modified-id="Scatter-plot-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Scatter plot</a></span></li><li><span><a href="#Box-plot" data-toc-modified-id="Box-plot-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Box plot</a></span></li><li><span><a href="#Violin-plot" data-toc-modified-id="Violin-plot-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Violin plot</a></span></li><li><span><a href="#Barplot-(categorical-vs-continuous)" data-toc-modified-id="Barplot-(categorical-vs-continuous)-4.2.4"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>Barplot (categorical vs continuous)</a></span></li><li><span><a href="#Joint-plot" data-toc-modified-id="Joint-plot-4.2.5"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>Joint plot</a></span></li></ul></li></ul></li><li><span><a href="#Facets-and-multivariate-data" data-toc-modified-id="Facets-and-multivariate-data-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Facets and multivariate data</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Scatter-plots-by-group" data-toc-modified-id="Scatter-plots-by-group-5.0.1"><span class="toc-item-num">5.0.1&nbsp;&nbsp;</span>Scatter plots by group</a></span></li></ul></li><li><span><a href="#Facets" data-toc-modified-id="Facets-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Facets</a></span></li><li><span><a href="#Pairs-plots" data-toc-modified-id="Pairs-plots-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Pairs plots</a></span></li></ul></li><li><span><a href="#Customizing-the-look" data-toc-modified-id="Customizing-the-look-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Customizing the look</a></span><ul class="toc-item"><li><span><a href="#Themes" data-toc-modified-id="Themes-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Themes</a></span></li></ul></li><li><span><a href="#Finer-control-with-matplotlib" data-toc-modified-id="Finer-control-with-matplotlib-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Finer control with matplotlib</a></span><ul class="toc-item"><li><span><a href="#Matlab-like-plotting" data-toc-modified-id="Matlab-like-plotting-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Matlab-like plotting</a></span></li></ul></li></ul></div>

# %% [markdown]
# # Data visualization using Python
#
# ## Introduction
#
# Data visualization is a basic task in data exploration and understanding. Humans are mainly visual creatures, and data visualization provides an opportunity to enhance communication of the story within the data. Often we find that data and the data-generating process is complex, and a visual representation of the data and our innate ability at pattern recognition can help reveal the complexities in a cognitively accessible way.
#
# ### An example gallery
#
# Data visualization has a long and storied history, from Florence Nightangle onwards. Dr. Nightangle was a pioneer in data visualization and developed the *rose plot* to represent causes of death in hospitals during the Crimean War.
#
# ![](graphs/rose.jpg)
#
#  John Snow, in 1854, famously visualized the cholera outbreak in London, which showed the geographic proximity of cholera prevalence with particular water wells.
#
# ![](graphs/snow_map.png)
#
# In one of the more famous visualizations, considered by many to be an optimal use of display ink and space, Minard visualized Napoleon's disastrous campaign to Russia
#
# ![](graphs/map-full-size1.png)
#
# In more recent times, an employee at Facebook visualized all connections between users across the world, which clearly showed geographical associations with particular countries and regions.
#
# ![](graphs/facebook-high-res-friendship-world-map-paul-butler.png)
#
# ### Why visualize data?
#
# We often rely on numerical summaries to help understand and distinguish datasets. In 1973, Anscombe published an influential set of 4 datasets, each with two variables and with the means, variances and correlations being identical. When you graphed these data, the differences in the datasets were clearly visible. This set is popularly known as Anscombe's quartet.
#
# ![](graphs/anscombe.png)
#
# A more recent experiment in data construction by Matejka and Fitzmaurice (2017) started with a representation of a dinosaur and created 10 more bivariate datasets which all shared the same univariate means and variances and the same pairwise correlations.
#
# ![](graphs/datasaurus.png)
#
# These examples clarify the need for visualization to better understand relationships between variables. 
#
# Even when using statistical visualization techniques, one has to be careful. Not all visualizations can discriminate between statistical characteristics. This was also explored by Matejka and Fitzmaurice. 
#
# |      Strip plot      |       Boxplot        |     Violin plot      |
# | :------------------: | :------------------: | :------------------: |
# | ![](graphs/box1.png) | ![](graphs/box2.png) | ![](graphs/box3.png) |
#
# ### Conceptual ideas
#
# #### Begin with the consumer in mind
#
# + You have a deep understanding of the data you're presenting
# + The person seeing the visualization **doesn't**
# + Develop simpler visualizations first that are easier to explain
#
# #### Tell a story
#
# + Make sure the graphic is clear
# + Make sure the main point you want to make "pops"
#
# #### A matter of perception
#
# + Color (including awareness of color deficiencies)
# + Shape
# + Fonts
#
# #### Some principles
#
# 1. Data-ink ratio
# 2. No mental gymnastics
#     1. The graphic should be self-evident
#     2. Context should be clear
# 3. Is a graph the wrong choice?
# 4. Focus on the consumer
#
# > See [my slides](http://araastat.com/BIOF439/lectures/01-DataViz.pdf) for some more opinionated ideas

# %% [markdown]
# ## Plotting in Python
#
# Let's take a very quick tour before we get into the weeds. We'll use the mtcars dataset as an exemplar dataset that we can import using `pandas`

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-notebook')

mtcars = pd.read_csv('data/mtcars.csv')
# %% [markdown]
# ### Static plots
#
# We will demonstrate plotting in what I'll call the `matplotlib` ecosystem. `matplotlib` is the venerable and powerful visualization package that was originally designed to emulate the Matlab plotting paradigm. It has since evolved and as become a bit more user-friendly. It is still quite granular and can facilitate a lot of custom plots once you become familiar with it. However, as a starting point, I think it's a bit much. We'll see a bit of what it can offer later.

# %% [markdown]
# We will consider two other options which are built on top of `matplotlib`, but are much more accessible. These are `pandas` and `seaborn`. The two packages have some different approaches, but both wrap `matplotlib` in higher-level code and decent choices so we don't need to get into the `matplotlib` trenches quite so much. We'll still call `matplotlib` in our code, since both these packages need it for some fine tuning. Both packages are also very much aligned to the `DataFrame` construct in `pandas`, so makes plotting a much more seamless experience. 

# %%
mtcars.plot.scatter(x = 'hp', y = 'mpg');
# mtcars.plot(x = 'hp', y = 'mpg', kind = 'scatter');

# %%
import seaborn as sns
sns.scatterplot(data = mtcars, x = 'hp', y = 'mpg');

# %% [markdown]
# There are of course some other choices based on your background and preferences. For static plots, there are a couple of emulators of the popular R package `ggplot2`. These are `plotnine` and `ggplot`. `plotnine` seems a bit more developed and uses the `ggplot2` semantics of aesthetics and layers, with almost identical code syntax. 
#
# > You can install `plotnine` using `conda`: 
# >
# > ```shell
# > conda install -c conda-forge plotnine
# > ```

# %%
from plotnine import *

(ggplot(mtcars) + 
  aes(x = 'hp', y = 'mpg') +
  geom_point())

# %% [markdown]
# ### Dynamic or interactive plots
#
# There are several Python packages that wrap around Javascript plotting libraries that are so popular in web-based graphics like D3 and Vega. Three that deserve mention are `plotly`, `bokeh`, and `altair`.

# %% [markdown]
# > If you actually want to experience the interactivity of the plots, please use the "Live notebooks" link in Canvas to run these notebooks. Otherwise, you can download the notebooks from the GitHub site and run them on your own computer. 

# %% [markdown]
# `plotly` is a Python package developed by the company [Plot.ly](https://www.plotly.com) to interface with their interactive Javascript library either locally or via their web service. Plot.ly also develops an R package to interface with their products as well. It provides an intuitive syntax and ease of use, and is probably the more popular package for interactive graphics from both R and Python.

# %%
import plotly.express as px

fig = px.scatter(mtcars, x = 'hp', y = 'mpg')
fig.show()

# %% [markdown]
# `bokeh` is an interactive visualization package developed by Anaconda. It is quite powerful, but its code can be rather verbose and granular

# %%
from bokeh.plotting import figure, output_file
from bokeh.io import output_notebook, show
output_notebook()
p = figure()
p.xaxis.axis_label = 'Horsepower'
p.yaxis.axis_label = 'Miles per gallon'

p.circle(mtcars['hp'], mtcars['mpg'], size=10)

show(p)


# %% [markdown]
# `altair` that leverages ideas from Javascript plotting libraries and a distinctive code syntax that may appeal to some

# %%
import altair as alt

alt.Chart(mtcars).mark_point().encode(
    x='hp',
    y='mpg'
).interactive()

# %% [markdown]
# We won't focus on these dynamic packages in this workshop in the interests of time, but you can avail of several online resources for these.
#
# | Package | Resources                                                    |
# | ------- | ------------------------------------------------------------ |
# | plotly  | [Fundamentals](https://plotly.com/python/)                   |
# | bokeh   | [Tutorial](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb) |
# | altair  | [Overview](https://altair-viz.github.io/getting_started/overview.html) |

# %% [markdown]
# ## Univariate plots
#
# We will be introducing plotting and code from 3 modules: `matplotlib`, `seaborn` and `pandas`. As we go forth, you may ask the question, which one should I learn? Chris Moffitt has the following advice.
#
# A pathway to learning ([Chris Moffit](https://pbpython.com/effective-matplotlib.html))
#
# 1. Learn the basic matplotlib terminology, specifically what is a `Figure` and an `Axes` .
# 2. Always use the object-oriented interface. Get in the habit of using it from the start of your analysis. (*not really getting into this, but basically don't use the Matlab form I'll show at the end, if you don't have to*)
# 3. Start your visualizations with basic pandas plotting.
# 4. Use seaborn for the more complex statistical visualizations.
# 5. Use matplotlib to customize the pandas or seaborn visualization.

# %% [markdown]
# ### pandas
#
# #### Histogram

# %%
mtcars.plot.hist(y = 'mpg');

# mtcars.plot(y = 'mpg', kind = 'hist')
#mtcars['mpg'].plot(kind = 'hist')

# %% [markdown]
# #### Bar plot

# %%
mtcars['cyl'].value_counts().plot.bar();

# %% [markdown]
# #### Density plot

# %%
mtcars['mpg'].plot( kind = 'density');

# %% [markdown]
# ### seaborn
#
# #### Histogram

# %%
ax = sns.distplot(mtcars['mpg'], kde=False);

# %% [markdown]
# #### Bar plot

# %%
sns.countplot(data = mtcars, x = 'cyl');

# %%
diamonds = pd.read_csv('data/diamonds.csv.gz')
ordered_colors = ['E','F','G','H','I','J']
sns.catplot(data = diamonds, x = 'color', kind = 'count', color = 'blue');

# %% [markdown]
# #### Density plot

# %%
sns.distplot(mtcars['mpg'], hist=False);

# %% [markdown]
# ## Bivariate plots
#
# ### pandas
#
# #### Scatter plot

# %%
diamonds = pd.read_csv('data/diamonds.csv.gz')
diamonds.plot(x = 'carat', y = 'price', kind = 'scatter');

# %% [markdown]
# #### Box plot

# %%
diamonds.boxplot(column = 'price', by = 'color');

# %% [markdown]
# ### seaborn
#
# #### Scatter plot

# %%
sns.scatterplot(data = diamonds, x = 'carat', y = 'price');

# %% [markdown]
# #### Box plot

# %%
ordered_color = ['E','F','G','H','I','J']
sns.catplot(data = diamonds, x = 'color', y = 'price', 
            order = ordered_color, color = 'blue', kind = 'box');

# %% [markdown]
# #### Violin plot

# %%
g = sns.catplot(data = diamonds, x = 'color', y = 'price', 
                kind = 'violin', order = ordered_color);

# %% [markdown]
# #### Barplot (categorical vs continuous)

# %%
ordered_colors = ['D','E','F','G','H','I']
sns.barplot(data = diamonds, x = 'color', y = 'price', order = ordered_colors);

# %%
sns.barplot(data = diamonds, x = 'cut', y = 'price');

# %% [markdown]
# #### Joint plot

# %%
sns.jointplot(data = diamonds, x = 'carat', y = 'price');

# %%
sns.jointplot(data = diamonds, x = 'carat', y = 'price', kind = 'reg');

# %%
sns.jointplot(data = diamonds, x = 'carat', y = 'price', kind = 'hex');
# %% [markdown]
# ## Facets and multivariate data
#
# The basic idea in this section is to see how we can visualize more than two variables at a time. We will see two strategies:
#
# 1. Put multiple graphs on the same frame, with each graph referring to a level of a 3rd variable
# 1. Create a grid of separate graphs, with each graph referring to a level of a 3rd variable
#
# This strategy also can work any time we need to visualize the data corresponding to different levels of a variable, say by gender or race or country. 
#
# In this example we're going to start with 4 time series, labelled A, B, C, D. 

# %%
ts = pd.read_csv('data/ts.csv')
ts.dt = pd.to_datetime(ts.dt) # convert this column to a datetime object
ts.head()

# %% [markdown]
# For one strategy we will employ, it is actually a bit easier to change this to a wide data form, using `pivot`. 

# %%
dfp = ts.pivot(index = 'dt', columns = 'kind', values = 'value')
dfp.head()

# %%
fig, ax = plt.subplots()
dfp.plot(ax=ax);

# %% [markdown]
# This creates 4 separate time series plots, one for each of the columns labeled A, B, C and D. The x-axis is determined by `dfp.index`, which during the pivoting operation, we deemed was the values of `dt` in the original data. 

# %% [markdown]
# Using `seaborn`...

# %%
sns.lineplot(data = dfp);

# %% [markdown]
# However, we can achieve this same plot using the original data, and `seaborn`, in rather short order

# %%
sns.lineplot(data = ts, x = 'dt', y = 'value', hue = 'kind');

# %% [markdown]
# In this plot, assigning a variable to `hue` tells seaborn to draw lines (in this case) of different hues based on values of that variable. 
#
# We can use a bit more granular and explicit code for this as well. This allows us a bit more control of the plot.

# %%
g = sns.FacetGrid(ts, hue = 'kind', height = 5, aspect = 1.5)
g.map(plt.plot, 'dt', 'value').add_legend()
g.ax.set(xlabel = 'Date',
        ylabel = 'Value',
        title = 'Time series');

## All of this code chunk needs to be run at one time, otherwise you get weird errors. This
## is true for many plotting commands which are composed of multiple commands. 


# %% [markdown]
# The `FacetGrid` tells `seaborn` that we're going to layer graphs, with layers based on `hue` and the hues being determined by values of `kind`. Notice that we can add a few more details like the aspect ratio of the plot and so on. The documentation for [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html), which we will also use for facets below, may be helpful in finding all the options you can control.

# %% [markdown]
# We can also show more than one kind of layer on a single graph

# %%
fmri = sns.load_dataset('fmri')


# %%
plt.style.use('seaborn-notebook')
sns.relplot(x = 'timepoint', y = 'signal', data = fmri);

# %%
sns.relplot(x = 'timepoint', y = 'signal', data = fmri, kind = 'line');

# %%
sns.relplot(x = 'timepoint', y = 'signal', data = fmri, kind = 'line', hue ='event');

# %%
sns.relplot(x = 'timepoint', y = 'signal', data = fmri, hue = 'region', 
            style = 'event', kind = 'line');


# %% [markdown]
# Here we use color to show the region, and line style (solid vs dashed) to show the event.

# %% [markdown]
# #### Scatter plots by group

# %%
g = sns.FacetGrid(diamonds, hue = 'color', height = 7.5)
g.map(plt.scatter, 'carat', 'price').add_legend();

# %% [markdown]
# Notice that this arranges the colors and values for the `color` variable in random order. If we have a preferred order we can impose that using the option `hue_order`. 

# %%
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds);


# %% [markdown]
# ### Facets
#
# Facets or trellis graphics is a visualization method where we draw multiple plots in a grid, with each plot corresponding to unique values of a particular variable or combinations of variables. This has also been called *small multiples*. 
#
# We'll proceed with an example using the `iris` dataset.

# %%
iris = pd.read_csv('data/iris.csv')
iris.head()

# %%
g = sns.FacetGrid(iris, col = 'species', hue = 'species', height = 5)
g.map(plt.scatter, 'sepal_width', 'sepal_length').add_legend();

# %% [markdown]
# Here we use `FacetGrid` to indicate that we're creating multiple subplots by specifying the option `col` (for column). So this code says we are going to create one plot per level of species, arranged as separate columns (or in effect along one row). You could also specify `row` which would arrange the plots one to a row, or, in effect, in one column. 
#
# The `map` function says, take the facets I've defined and stored in `g`, and in each one, plot a scatter plot with `sepal_width` on the x-axis and `sepal_length` on the y-axis. 

# %% [markdown]
# We could also use `relplot` for a more compact solution.

# %%
sns.relplot(x = 'sepal_width', y = 'sepal_length', data = iris, 
            col = 'species', hue = 'species');

# %% [markdown]
# A bit more of a complicated example, using the `fmri` data, where we're coloring lines based on the subject, and creating a 2-d grid, where region of the brain in along columns and event type is along rows. 

# %%
sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", estimator=None, data=fmri);

# %% [markdown]
# In the following example, we want to show how each subject fares for each of the two events, just within the frontal region. We let `seaborn` figure out the layout, only specifying that we'll be going along rows ("by column") and also saying we'll wrap around to the beginning once we've got to 5 columns. Note we use the `query` function to filter the dataset. 

# %%
sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=3, aspect=.75, linewidth=2.5,
            kind="line", data=fmri.query("region == 'frontal'"));

# %% [markdown]
# In the following example we want to compare the distribution of price from the diamonds dataset by color, and so it makes sense to create density plots of the price distribution and stack them one below the next so we can visually compare them. 

# %%
ordered_colors = ['E','F','G','H','I','J']
g = sns.FacetGrid(data = diamonds, row = 'color', height = 1.7, 
                  aspect = 4, row_order = ordered_colors)
g.map(sns.kdeplot, 'price');

# %% [markdown]
# You need to use `FacetGrid` to create sets of univariate plots since there is no particular method that allows univariate plots over a grid like `relplot` for bivariate plots.

# %% [markdown]
# ### Pairs plots
#
# The pairs plot is a quick way to compare every pair of variables in a dataset (or at least, every pair of continuous variables) in a grid. You can specify what kind of univariate plot will be displayed on the diagonal locations on the grid, and which bivariate plots will be displayed on the off-diagonal locations. 

# %%
sns.pairplot(data=iris)

# %% [markdown]
# You can achieve more customization using `PairGrid`.

# %%
g = sns.PairGrid(iris, diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, colors="C0")
g.map_diag(sns.kdeplot, lw=2);


# %% [markdown]
# ## Customizing the look 

# %% [markdown]
# ### Themes
#
# There are several themes available in the modern `matplotlib`, some of which borrow from `seaborn`. You can see the available themes and play around. 

# %%
plt.style.available

# %% [markdown]
# See some examples below.

# %%
plt.style.use('fivethirtyeight')
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length');

# %%
plt.style.use('bmh')
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length');

# %%
plt.style.use('classic')
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length');

# %%
plt.style.use('ggplot')
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length');

# %%
plt.style.use('Solarize_Light2')
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length');

# %% [markdown]
# > One small syntax point. You may have noticed in your own work that you get a little annoying line in the output when you plot. You can prevent that from happening by putting a semi-colon (`;`) after the last plotting command

# %% [markdown]
# ## Finer control with matplotlib
#
# ![https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py](graphs/matplotlib-anatomy.png)
#
#
# As you can see from the figure, you can control each aspect of the plot displayed above using `matplotlib`. I won't go into the details, and will leave it to you to look at the `matplotlib` [documentation](https://matplotlib.org/contents.html) and [examples](https://matplotlib.org/gallery/index.html) if you need to customize at this level of granularity. 
#
# The following is an example using pure `matplotlib`. You can see how you can build up a plot. The crucial part here is that you need to run the code from each chunk together.  

# %%
from matplotlib.ticker import FuncFormatter

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

# %%
plt.style.use('default')
fig, ax = plt.subplots()
# %%
fig, ax = plt.subplots()
ax.barh(group_names, group_data);

# %%
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
ax.set(xlim = [-10000, 140000], xlabel = 'Total Revenue', ylabel = 'Company', 
       title = 'Company Revenue');

# %%
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue');

# %% [markdown]
# After you have created your figure, you do need to save it to disk so that you can use it in your Word or Markdown or PowerPoint document. You can see the formats available. 

# %%
fig.canvas.get_supported_filetypes()

# %% [markdown]
# The type will be determined by the ending of the file name. You can add some options depending on the type. I'm showing an example of saving the figure to a PNG file. Typically I'll save figures to a vector graphics format like PDF, and then convert into other formats, since that results in minimal resolution loss. You of course have the option to save to your favorite format.

# %%
# fig.savefig('sales.png', dpi = 300, bbox_inches = 'tight') 

# %% [markdown]
# ### Matlab-like plotting
#
# `matplotlib` was originally developed to emulate Matlab. Though this kind of syntax is no longer recommended, it is still available and may be of use to those coming to Python from Matlab or Octave. 

# %%
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# %%
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# %%
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# %%
