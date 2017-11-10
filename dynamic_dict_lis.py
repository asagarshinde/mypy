#!/usr/bin/env python

from random import randint
""" Create dynamic dictionary using mutable list"""
key_list = ['server1','server2','server3']

class Values():
    def __init__(self,counter):
        self.counter = counter
        self.values_list = []
    
    def list_generator(self):
        for i in range(self.counter):
            self.values_list.append(i)
        return self.values_list


dic = {}
for key in key_list:
    counter = randint(0,10)
    value_list_object = Values(counter)
    value_list = value_list_object.list_generator()
    dic[key]=value_list

print dic

