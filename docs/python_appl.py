# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
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

# %%
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent,Rmd
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
<<<<<<< HEAD
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # String manipulation
#
# String manipulation is one of Python's strong suites. It comes built in with methods for strings, and the `re` module (for *regular expressions*) ups that power many fold. 
#
# Strings are objects that we typically see in quotes. We can also check if a variable is a string.

# %%
a = 'Les Miserable'

type(a)

# %% [markdown]
# Strings are a little funny. They look like they are one thing, but they can act like lists. In some sense they 
# are really a container of characters. So we can have

# %%
len(a)

# %%
a[:4]

# %%
a[3:6]

# %% [markdown]
# The rules are basically the same as lists. To make this explicit, let's consider the word 'bare'. 
# In terms of positions, we can write this out.
#
# |           |      |      |      |      |
# | --------- | ---- | ---- | ---- | ---- |
# | index     | 0    | 1    | 2    | 3    |
# | string    | b    | a    | r    | e    |
# | neg index | -4   | -3   | -2   | -1   |
# |           |      |      |      |      |
#
# We can also slices strings (and lists for that matter) in intervals. So, going back to `a`, 

# %% language="R"
# a[: :2]

# %% [markdown]
# slices every other character. 
#
# Strings come with several methods to manipulate them natively. 

# %%
'White Knight'.capitalize()
"It's just a flesh wound".count('u')
'Almond'.endswith('nd')
'White Knight'.lower()
'White Knight'.upper()
'flesh wound'.replace('flesh','bullet')
' This is my song   '.strip()
'Hello, hello, hello'.split(',')

# %% [markdown]
# One of the most powerful string methods is `join`. This allows us to take a list of characters, and then 
# put them together using a particular separator. 

# %%
' '.join(['This','is','my','song'])

# %% [markdown]
# Also recall that we are allowed "string arithmetic".

# %%
'g' + "a' + 'f' + 'f' + 'e'

'a '*5

# %% [markdown]
# ### String formatting
#
# In older code, you will see a formal format statement.

# %%
var = 'horse'
var2 = 'car'

s = 'Get off my {}!'

s.format(var)
s.format(var2)

# %% [markdown]
# This is great for templates. 

# %%
template_string = """
{country}, our native village
There was a {species} tree.
We used to sleep under it.
"""

print(template_string.format(country='India', species = 'banyan'))
print(template_string.format(country = 'Canada', species = 'maple'))

# %% [markdown]
# In Python 3.6+, the concept of `f-strings` or formatted strings was introduced. They can be easier to read, faster and have better performance. 

# %%
country = 'USA'
f"This is my {country}!"

# %% [markdown]
# ## Regular expressions
#
# Regular expressions are amazingly powerful tools for string search and manipulation. They are available in pretty much every 
# computer language in some form or the other. I'll provide a short and far from comprehensive introduction here. The website [regex101.com](https://regex101.com) is a really good resource to learn and check your regular expressions. 
#
# ### Pattern matching
#
# | Syntax  | Description                                                  |
# | ------- | ------------------------------------------------------------ |
# | `.`     | Matches any one character                                    |
# | `^`     | Matches from the beginning of a string                       |
# | `$`     | Matches to the end of a string                               |
# | `*      | Matches 0 or more repetitions of the previous character      |
# | `+`     | Matches 1 or more repetitions of the previous character      |
# | `?`     | Matches 0 or 1 repetitions of the previous character         |
# | `{m}`   | Matches `m` repetitions of the previous character            |
# | `{m,n}` | Matches any number from `m` to `n` of the previous character |
# | `\`     | Escape character                                             |
# | `[ ]`   | A set of characters (e.g. `[A-Z]` will match any capital letter) |
# | `( )`   | Matches the pattern exactly                                  |
# | `|`     | OR                                                           |
#

# %% [markdown]
# # BioPython
#
# BioPython is a package aimed at bioinformatics work. As with many Python packages, it is opinionated towards the needs of the developers, so might not meet everyone's needs. 
#
# You can install BioPython using `conda install biopython`.
#
# We'll do a short example

# %%
from Bio.Seq import Seq

#create a sequence object
my_seq = Seq("CATGTAGACTAG")

#print out some details about it
print("seq %s is %i bases long" % (my_seq, len(my_seq)))
print("reverse complement is %s" % my_seq.reverse_complement())
print("protein translation is %s" % my_seq.translate())

# %% [markdown]
# BioPython has capabilities for querying databases like `Entrez`, read sequences, do alignments using FASTA, and the like. 

