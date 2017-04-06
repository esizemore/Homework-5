#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 10:16:19 2017

@author: elizabethsizemore
"""

import fitsio
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

line_fit= []


#import data
data=fitsio.FITS("allStar-l30e.2.fits")


#Select APOGEE stars only with 59<GLAT<61
cut = data[1].where('GLAT>59 && GLAT<61 && O_FE>-4 && FE_H>-3')
stars=data[1][cut]


#Fit Fe_H_ERR vs O_FE_ERR
#Fit linear and quadratic functions

y= stars['FE_H'][:]
x= stars['O_FE'][:]

plt.scatter(stars['FE_H'],stars['O_FE']) #want scatter plot, not line
#plt.plot(x,y)
plt.show()


#LINEAR FUNCTION
def linear (x,m,b):
    return (m*x)+b

popt, pcov=curve_fit(linear, x, y)

#print(popt[0], popt[1])


#QUADRATIC FUNCTION
def quadratic(x,a,c,d):
    return a*(x**2)+(c*x)+d

popt2, pcov2=curve_fit(quadratic, x, y)


xlin=np.linspace(-4., 2., 100)

guess_a=2.0 #amp
guess_b=-2.0 #phase shift
guess_c=1.0  #offset
guess_d=1.0 #frequency

p0=[guess_d, guess_a, guess_b, guess_c]

print('The best fit parameters are: Amplitude:', guess_a, 'Phase Shift:', guess_b, 'Offset:', guess_c, 'Frequency:', guess_d)


#Create function
def F_t(x, w, a, b, c):
    return np.cos((w*x)+b)*a +c

#The actual fit
fit=curve_fit(F_t, x, y, p0=p0)

#Plot guess
data_first_guess=F_t(x, *p0)

data_fit=F_t(x, *fit[0])

ylin = linear(xlin, popt[0], popt[1])
#print(xlin)
#print(ylin)


#Generate plots for each
#plt.plot(x,y)

#linear
plt.plot (xlin, ylin, label='Linear')


#quadratic
plt.plot(xlin, quadratic(xlin, popt2[0], popt2[1], popt2[2]), label='Quadratic')

plt.plot()

plt.title('Chemical Trends')
plt.xlabel('O_FE')
plt.ylabel('FE_H')

plt.show()



#b) The linear function best fits the data.
#c) There were other populations, but I ommitted that aspect of the fits table.