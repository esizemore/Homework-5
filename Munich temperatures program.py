#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:31:45 2017

@author: elizabethsizemore
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
 

x, y = np.loadtxt(open('munich_temperatures_average_with_bad_data.txt'), unpack = True)



a=15 #guess amp
b= 2.8 #guess phase
c=np.mean(y) #guess offset

p0=[a,b,c]


#create the function we want to fit for temperature
def F(x, a, b, c):
   return a*np.cos(2*np.pi*x+b)+c
    
fit= curve_fit(F, x, y, p0=p0)
First_guess=F(x, *p0)

ymax=max(First_guess)
ymin=min(First_guess)



plt.plot(x, y)
plt.plot(x, First_guess)
plt.xlabel('Time in Years')
plt.ylabel('Temperature in Degrees Celsius')
plt.title('Average Temperatures in Munich')
plt.show()
print (' The best fit parameters are: a=', a, 'b=', b, 'c=', c)
print('The overall average temperature in Munich is', c, 'degrees Celsius')
print ('The maximum daily value for the hottest time of year (degrees Celsius):', ymax)
print('The minimum daily value for the coldst time of year (degrees Celsius):', ymin)


#The b parameter affects the phase of our model. Our value makes sense, because it 
#allows the model to fit the data...in other words, our year starts off with cold
#temperatures as opposed to warm temperatures. 