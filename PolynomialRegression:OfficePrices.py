# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys
import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    F, N = map(int, input().rstrip().split())
    
    data = np.array([list(map(float, input().rstrip().split())) for _ in range(N)])
    
    T = int(input())
    
    test = np.array([list(map(float, input().rstrip().split())) for _ in range(T)])
    
    
    lr = LinearRegression()
    x = data[:,0:F]
    y = data[:,F]
    poly = PolynomialFeatures(degree=3)
    x_poly = poly.fit_transform(x)
    lr.fit(x_poly, y)
    
    price = lr.predict(poly.fit_transform(test))
    
    for row in price:
        fptr.write(f'{row:.2f}\n')

    fptr.close()
