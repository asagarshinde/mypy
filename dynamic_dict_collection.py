#!/usr/bin/env python
import collections
from random import randint
""" Create dynamic list using collection module"""
dic = collections.defaultdict(list)
lis1 = [1,2,3,4,5]
#lis2 = ['a','b','c','d','e']

def lis_generator(counter):
    lis2 = []
    for i in range(counter):
        lis2.append(i)
    return lis2

for key in lis1:
    counter = randint(0,29)
    value_list = lis_generator(counter)
    for value in value_list:
        dic[key].append(value)

for key in dic.keys():
    print dic[key]
