#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:04:20 2020

@author: abhijit
"""

#%% Preamble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#%%

z = [1,2,3,4,5,6,7,8,9.3, 10.6]
z_array = np.array(z)

z_array.sum()
z_array.min()

np.min(z_array)

y = [1, 3.0, 'a']
np.array(y)

#%% Generate data

np.arange(10)

np.linspace(start=0, stop = 1, num=11)

np.zeros(10)

np.zeros((10,10))

x = np.array([1,2,3,4])

np.eye(4)

rng = np.random.RandomState(50)
rng.randint(0, 10, (3,4))


A = rng.normal(0, 1, (4, 5))
A.shape
A.size
B = np.zeros_like(A)


x = [1,3,5,7,9, 'b']
x[:3]
x[1:4]
x[-2:-1]



A
A[1:2,:]

A[:, :3]


A1 = A
A1
A[0,0] = 5

A1 = A.copy()
A1[0,0] = 10





