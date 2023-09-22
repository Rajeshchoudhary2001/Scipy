# OPtimizers in SCipy: they are a set of procedures defined in scipy that either find the minimum value of a function or a root of an equation.
# optimizing function: all the algorithms which helps in minimizing the data.
# Root of an equation: x + cos(x), we will solve it via optimize.root function. 
# this function takes 2 arguments: "fun" and x0
# example: here we will find the root of the equation x + cos(x) :

from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)     #[-0.73908513]



# here we want the info about not just x but the whole root:
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot)

# output:
#  fjac: array([[-1.]])
#      fun: array([ 0.])
#  message: 'The solution converged.'
#     nfev: 9
#      qtf: array([ -2.66786593e-13])
#        r: array([-1.67361202])
#   status: 1
#  success: True
#        x: array([-0.73908513])

''' Minimizing a Function
A function, in this context, represents a curve, curves have high points and low points.

High points are called maxima.

Low points are called minima.

The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.

# Finding Minima
We can use scipy.optimize.minimize() function to minimize the function.

The minimize() function takes the following arguments:

fun - a function representing an equation.

x0 - an initial guess for the root.

method - name of the method to use. Legal values:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'

callback - function called after each iteration of optimization.

options - a dictionary defining extra params:

{
     "disp": boolean - print detailed description
     "gtol": number - the tolerance of the error
  } '''

# Example
# Minimize the function x^2 + x + 2 with BFGS:

from scipy.optimize import minimize
def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

# output
'''  fun: 1.75
 hess_inv: array([[ 0.50000001]])
      jac: array([ 0.])
  message: 'Optimization terminated successfully.'
     nfev: 12
      nit: 2
     njev: 4
   status: 0
  success: True
        x: array([-0.50000001])'''