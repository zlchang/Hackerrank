# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


F, N = map(int, input().split())

data = [list(map(float, input().split())) for i in range(N)]

data = np.array(data)

X_train, y_train = data[:, :-1], data[:, -1]

T = int(input())

X_test = [list(map(float, input().split())) for i in range(T)]

X_test = np.array(X_test)

degree = 3

poly = PolynomialFeatures(degree)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

predictions = model.predict(X_test_poly)

for p in predictions:
    print(round(p, 2))
