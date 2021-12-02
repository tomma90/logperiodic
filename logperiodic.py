import numpy as np
import matplotlib.pyplot as pl
import math as ma
import cmath as cm

pi = np.pi
s = .001
R = 20.
R0 = 1.
t = 1.3

def phi(delta):
	r = np.arange(R0,R,s)
	phi1 = (pi/4)*np.sin(pi*np.log(r/R0)/np.log(t)) + delta
	phi2 = (pi/4)*np.sin(pi*np.log(r/R0)/np.log(t)) - delta
	return r, phi1, phi2

x, y1, y2 = phi(pi/8)

def pol2cart(r, a):
    X = r * np.sin(a)
    Y = r * np.cos(a)
    return(X, Y)

X1, Y1 = pol2cart(x,y1)
X2, Y2 = pol2cart(x,y2)

X1_90 = X1 * np.cos(pi/2) - Y1 * np.sin(pi/2)
Y1_90 = X1 * np.sin(pi/2) + Y1 * np.cos(pi/2)
X2_90 = X2 * np.cos(pi/2) - Y2 * np.sin(pi/2)
Y2_90 = X2 * np.sin(pi/2) + Y2 * np.cos(pi/2)

X1_180 = X1 * np.cos(pi) - Y1 * np.sin(pi)
Y1_180 = X1 * np.sin(pi) + Y1 * np.cos(pi)
X2_180 = X2 * np.cos(pi) - Y2 * np.sin(pi)
Y2_180 = X2 * np.sin(pi) + Y2 * np.cos(pi)

X1_270 = X1 * np.cos(3*pi/2) - Y1 * np.sin(3*pi/2)
Y1_270 = X1 * np.sin(3*pi/2) + Y1 * np.cos(3*pi/2)
X2_270 = X2 * np.cos(3*pi/2) - Y2 * np.sin(3*pi/2)
Y2_270 = X2 * np.sin(3*pi/2) + Y2 * np.cos(3*pi/2)

pl.plot(X1,Y1,color='red')
pl.plot(X2,Y2,color='red')
pl.plot(X1_90,Y1_90,color='blue')
pl.plot(X2_90,Y2_90,color='blue')
pl.plot(X1_180,Y1_180,color='green')
pl.plot(X2_180,Y2_180,color='green')
pl.plot(X1_270,Y1_270,color='black')
pl.plot(X2_270,Y2_270,color='black')
pl.show()
