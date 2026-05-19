#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':
    timeCharged = float(input().strip())
    
    data = []
    with open('trainingdata.txt', mode='r') as file:
        for line in file:
            row = list(map(float, line.strip().split(',')))
            data.append(row)
    data = np.array(data)

    x_raw = data[:,0]
    y_raw = data[:,1]
    #print(y_raw)
    
    threshold = min(x_raw[y_raw == 8])
    mask = y_raw < 8.0
    
    x = x_raw[mask].reshape(-1, 1)
    y = y_raw[mask].reshape(-1, 1)
    
    lr = LinearRegression()
    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x)
    lr.fit(x_poly, y)
    
    x_test = np.array([[timeCharged]])
    x_test_poly = poly.fit_transform(x_test)
    timeUse = np.array([[8.0]])
    if timeCharged < threshold:
        timeUse = lr.predict(x_test_poly)
    
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('{:.2f}\n'.format(timeUse[0][0]))
    fptr.close()
