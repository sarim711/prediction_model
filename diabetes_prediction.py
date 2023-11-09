# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hQqXd4VrPo8yvEgznum-u16-hCyfiMDZ
"""



"""Importing the Dependencies

"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis
PIMA Diabetes Dateset
"""

1 # loading Dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

#number of rows and columns in this dataset
diabetes_dataset.shape

#statistical measure of dataset
diabetes_dataset.describe()

#No. of diabetic and non-diabetic patients
#diabetic = 1, non-diabetic=0
diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

#separating data &labels
X = diabetes_dataset.drop(columns ='Outcome', axis = 1)
Y = diabetes_dataset['Outcome']

print(X)

"""Data Standardization

"""

scaler = StandardScaler()
scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

"""Train Test Split"""

X = standardized_data
Y = diabetes_dataset['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

"""Training the data"""

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

#accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction , Y_train)

print(training_accuracy)

"""Building Predictive System"""

inputdata = (8,183,64,0,0,23.3,0.672,32)
#changing tuple to numpy array
inputdataasnumpyarray = np.asarray(inputdata)
#reshaping data for 1 datapoint prediction
inputdatareshaped = inputdataasnumpyarray.reshape(1,-1)
prediction = classifier.predict(inputdatareshaped)
print(prediction)

if (prediction[0]==0):
  print('Patient is non diabetic')
else:
  print('Patient is diabetic')