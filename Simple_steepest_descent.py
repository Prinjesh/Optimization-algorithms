# -*- coding: utf-8 -*-
"""Copy_of_Optimization (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FyktYMO2nloST_TzpB-JtACkHFkO4ar2

### Steepest descent algorithm without Armijo step size rule.

#### This method is not one of the best methods used in the optimization field now-a-days but it is a stepping stone for the actual work horse algorithm that is used in a wide range.
"""

# importing required libraries 
import numpy as np

"""Rosenbrock equation to understand the descent method"""

# Creating rosenbrock equation
def rosenbrock(X, a=1, b=100):
    x1, x2 = X
    return (a - x1)**2 + b *((x2 - x1**2)**2)

# Creating a Gradient of the function
def gradient(x1,x2):
  # Manually added a gradient of a function
  grad_f = np.array([-2+(2*x1)+(400*(x1**3)-(400*x1*x2)),(200*x2)-(200*(x1**2))])
  return grad_f

"""We will now initialize 5 points on the rosenbrock equation and will put them into the descent algorithm."""

# Initialising 5 initial points
X0_list = []
for i in range(5):
  # Assigning values to seeds to create 5 random values
  np.random.seed(i)
  X0 = np.random.rand(2,1)
  print('initialised value:',i+1,X0)
  X0_list.append(X0)

"""Step size is hard coded in the simplest form of descent algorithm. We have taken 0.00125 step size and iterate over the loop for 10000 times."""

no_of_iteration = 100000
t = 0.00125

# Initializing list to store minimum points on the curve and the iteration values
X_min = []
X_temp_init ={}


for j in range(len(X0_list)): # Making a loop of initialized points
  # Getting the initialized value from the list 
  X = X0_list[j] 
  # Empty list to store iterations during the loop
  X_temp = []
  for i in range(no_of_iteration): # Condition 1 : To not exceed more than 10^5 iterations
    grad = gradient(X[0],X[1]) # Calculating gradient values
    if np.linalg.norm(grad) >= 0.00001: # Condition 2 : If the norm of the gradient is less than 10^-5 or not
      X = (X - (t*grad)) # Updating the X parameter
      X_temp.append(X)
    else:
      X = X
      X_temp.append(X)
  X_min.append(X) # Adding the minimum value to the list
  X_temp_init[j+1] = X_temp # Adding all the iterations in the list

# Result
for i in range(5):
  print('For the initialised value of:',X0_list[i],'The minimum value(x*) is:',X_min[i])

"""---

"""