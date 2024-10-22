#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 01:45:03 2018

@author: tam
"""

import pickle
import glob
import face_recognition
import pandas as pd

training_folder = '/home/adil/Desktop/fdirs/dataset/features_dataset/'

training_imgs = glob.glob(training_folder + '/*.jpg')

#imgs_indexing_database = {}
#indexing_imgs_database = {}
#indexing_features_database = {}
counter = 0
df = pd.DataFrame(columns=['labels', 'features', 'imgs_addrs'])

for img in training_imgs:
    img_name_parts = img.split('/')[len(img.split('/'))-1].split('_')
   # print img_name_parts
    img_lbl = img_name_parts[0] + '_' + img_name_parts[1]
    
 #   indexing_imgs_database[counter] = img
  #  imgs_indexing_database[img] = counter
    image = face_recognition.load_image_file(img)
    # print image
    face_landmarks_list = face_recognition.face_encodings(image)
    
   # print face_landmarks_list
    
    for fl in face_landmarks_list:
        df.loc[counter] = [img_lbl, fl, img]    
        counter += 1
        
    
    
 
with open('pickle_labels/training_database.pkl', 'w') as f:
    pickle.dump(df, f)
    
