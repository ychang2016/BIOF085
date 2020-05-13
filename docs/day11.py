#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:04:34 2020

@author: abhijit
"""

# set a splitting point
split_point = 3

# make two empty lists
lower = []; upper = []

# Split numbers from 0 to 9 into two groups, one lower or equal to the split point and one higher than the split point
for i in range(10): # count from 0 to 9
  if (i <= split_point):
    lower.append(i)
  else: 
    upper.append(i)

print("lower:", lower)
print('upper:', upper)


a = 1.2
b = 5
c = 'hello'
d = "goodbye"
e = True


first_name = 'Abhijit'

first_name * 3
last_name = 'Dasgupta'

first_name + ' ' + last_name


b < 10

b == 10

b >= 10
b <= 10

b != 10

(a > 0) | (b == 5)

(a < 0) & (b == 5)

not (a > 0)






int i = 5;

a = 'abra'
a = 39

# list
[]
#tuple
()
# dict
{}


l1 = ['a', 35, True, [3, 5]]


l1[0]

l1[:3]

l1[1:3]

l1[2:]


l1[-1]

l1[-3:-1]


test_nested_list = [[1,'a',2,'b'],
[3, 'c', 4, 'd']]

test_tuple = (1,2,3)

test_list = [1,2,3]

test_list[2] = 40
test_list
test_tuple[2] = 40


contact = {
  "first_name": "Abhijit",
  "last_name": 'Dasgupta',
  "Age": 48,
  "address": "124 Main St",
  "Employed" : True
}



contact[2]
contact['Age']
contact['address'] = '123 Main St'
contact


3 in [1,2,3,4,5,6,7]




x = [-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = [] # an empty list

for u in x:
  if u < 0:
    y.append('Negative')
  elif u % 2 == 1:         # what is remainder when dividing by 2
    y.append('Odd')
  else:
    y.append('Even')

print(y)



def my_mean(x):
    y = 0
    for u in x:
        y = y + u
    y = y/len(x)
    return(y)


my_mean([0, 1, 2,3])




import numpy as np

np.pi



# in terminal

conda install numpy





























