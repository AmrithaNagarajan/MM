

import numpy as np
import statistics
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def measures(y, y_cap):
  n=len(y)
  sse = 0
  sst = 0
  y_bar = sum(y)/n
  for i in range(n):
    diff = y[i] - y_cap[i]
    sse += (y[i] - y_cap[i]) * (y[i] - y_cap[i])
    sst += (y[i] - y_bar) * (y[i] - y_bar)

  correlation = 1-(sse/sst)
  return sse, sst, correlation


def linear_reg(x,y):
  n=len(x)
  xy = np.dot(np.array(x),np.array(y))

  x_sq = 0
  for i in x:
    x_sq+=i**2


  a = (((n*xy) - (sum(x)*sum(y))) /((n*x_sq) - (pow(sum(x),2))))
  b = ((sum(y) -(a*sum(x)))/n)

  return a,b


def multiple_lin_reg(x,y, x_pred):
  b = np.matmul(np.linalg.inv(np.matmul(x.transpose(), x)), np.matmul(x.transpose(), y))
  return np.multiply(np.repeat([b], repeats = x_pred.shape[0], axis = 0), x_pred).sum(axis=1)

#linear reg

x=[200,250,200,250,189.65,260.35,225,225,225,225,225,225]
y=[43,78,69,73,48,78,65,74,76,79,83,81]

a,b = linear_reg(x,y)
print(a)
print(b)
y_cap = [((a*i)+b) for i in x]
print(y_cap)


sse, sst, correlation = measures(y,y_cap)
print(correlation)
print(sse)
print(sst)


#multi lin reg

x1 = np.array([1.26926382, -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929 ,  1.87002637 ])
x2 = np.array([-8.97613991, 1.26926382, -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929])
y = np.array([ -9.43542734, 7.59084266, 7.52067092, -13.94486326,  11.63625102,   9.56782929 ,  1.87002637,  -7.09845358])

x0 = np.ones(len(x1))
x = np.stack((x0,x1,x2), axis = 1)
y_pred = multiple_lin_reg(x, y, x)
print(y_pred)



# b = np.log(a)
# a = math.exp(b)

# r2 = np.corrcoef(x,y)

