#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:13:14 2018

@author: tam
"""

import pickle
import pandas as pd
import glob
import face_recognition

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

with open('pickle_labels/training_database.pkl') as f:  
    df = pickle.load(f)
    
testing_folder = '/home/adil/Desktop/fdirs/dataset/test_dataset/'
testing_imgs = glob.glob(testing_folder + '/*.jpg')

testing_recall = []
testing_prec = []

for img in testing_imgs:
    img_name_parts = img.split('/')[len(img.split('/'))-1].split('_')
    img_lbl = img_name_parts[0] + '_' + img_name_parts[1]
   
    image = face_recognition.load_image_file(img)
    face_landmarks_list = face_recognition.face_encodings(image)

    for fl in face_landmarks_list:
        results = face_recognition.compare_faces(df['features'].tolist(), fl, tolerance=0.552)
        #print results
        retriv = []
        for i in range(len(results)):
            if results[i] == True:
               # print i
                retriv.append(i)
              #  print df['imgs_addrs'].tolist()[i]
        image1 = Image.open(img)
        f, axarr = plt.subplots((len(retriv)/4)+2,4)
        axarr[0,0].imshow(image1)
        counter = 2
        
        for j in range(len(retriv)):
            image1 = Image.open(df['imgs_addrs'][retriv[j]])
            axarr[counter/4,counter%4].imshow(image1)
            counter += 1
       # img_counter += 1
 
        all_labels = df['labels'].tolist()
        prec_match = 0
 #      print len(results)
        for i in range(len(results)):
            if results[i] and all_labels[i] == img_lbl:                
                prec_match += 1
        
        if sum(results):
           # print float(prec_match)
            testing_prec.append(float(prec_match)/sum(results))
        else:
            testing_prec.append(0)
            
 #       image2 = Image.open(df['imgs_addrs'][i])
 #       axarr[img_counter/4,img_counter%4].imshow(image2)
 #       img_counter += 1
     #   image1.show()
      #  image2.show()
       # print results
        
  #      plt.show()
  
        recall_match = 0
        for lbl in all_labels:
            if img_lbl == lbl:
                recall_match += 1
        testing_recall.append(float(prec_match)/recall_match)
        break
        

print 'Precision : ' + str(np.mean(testing_prec) * 100)+' %'
print 'Recall : ' + str(np.mean(testing_recall) * 100)+' %'