#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:18:54 2018

@author: adi
"""

import pickle
import glob

dataset_folder = '/home/adil/Desktop/fdirs/dataset/knn_dataset'
imgs_name = glob.glob(dataset_folder+'/*.jpg')

persons_names = {}
for img in imgs_name:
   try:
       img_name_parts = img.split('/')[len(imgs_name[0].split('/'))-1].split('_')
    #   print img_name_parts
       if img_name_parts[0] + '_' + img_name_parts[1] in persons_names.keys(): 
           persons_names[img_name_parts[0] + '_' + img_name_parts[1]].append(img)
       else:
           persons_names[img_name_parts[0] + '_' + img_name_parts[1]] = [img]
   except:
        print img
with open('pickle_labels/labels.pkl', 'w') as f:
    pickle.dump(persons_names, f)
