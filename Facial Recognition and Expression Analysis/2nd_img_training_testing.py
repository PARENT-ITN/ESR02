#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 00:16:17 2018

@author: tam
"""

import pickle
import os

with open('pickle_labels/labels.pkl') as f:  
    persons_names = pickle.load(f)

training_features = '/home/adil/Desktop/fdirs/dataset/features_dataset/'
testing_features = '/home/adil/Desktop/fdirs/dataset/test_dataset/'

for per_name in persons_names.keys():
    counter = len(persons_names[per_name])
    for i in range(counter):
        if i == counter - 1 and counter  >= 4:
            os.system('cp -r  '+ persons_names[per_name][i] + ' ' + testing_features)
        else:
            os.system('cp -r  '+ persons_names[per_name][i] + ' ' + training_features)
