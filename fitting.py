import numpy as np
from scipy.optimize import leastsq


# Standard Form of Quadratic Function
def func3(params, x):
    a, b, c = params
    return a * x * x + b * x + c
def func2(params, x):
    a, b = params
    return a * x + b

# Error function, that is, the difference between the value obtained by fitting curve and the actual value
def error2(params, x, y):
    return func2(params, x) - y

def error3(params, x, y):
    return func3(params, x) - y

# Solving parameters
def solvePara(X, Y, p0=[0, 0, 0]):
    X = np.array(X)
    Y = np.array(Y)
    if len(X) >= 3:
        Para = leastsq(error3, p0[0:3], args=(X, Y))
    elif len(X) == 2:
        Para = leastsq(error2, p0[0:2], args=(X, Y))
    elif len(X) <= 1:
        return p0
    return Para[0]

