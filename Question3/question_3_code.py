#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:30:45 2021

@author: Josey
"""
#import

import pandas as pd 
# import matplotlib.pyplot as plt 
# from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import tree

train_data = pd.read_csv('/Users/Josey/Desktop/AY20_MBDS_questions/Question 3/train_data.txt', sep='\t',  lineterminator='\n', names=None) 
# train_data.head() #show top 5 records
train_truth = pd.read_csv('/Users/Josey/Desktop/AY20_MBDS_questions/Question 3/train_truth.txt', sep='\t',  lineterminator='\n', names=None)
# train_truth.head()

#get the axes
X = np.array(train_data)
y = np.array(train_truth)
X_train, X_test, y_train, y_test = train_test_split(train_data, train_truth)
dtree = tree.DecisionTreeClassifier() #instance in decision tree
##can't solve this as there is a ValueError: unknown label type: 'Continuous'
dtree.fit(X_train, y_train) #train model

#predict
y_pred = dtree.predict(X_test)
test_data = pd.read_csv('/Users/Josey/Desktop/AY20_MBDS_questions/Question 3/test_data.txt', sep='\t',  lineterminator='\n', names=None) 
pred_test = dtree.predict([test_data])
pred_test[0]

