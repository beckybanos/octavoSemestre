#Convolución
import numpy as np 
import scipy as sp
import matplotlib.pyplot as pl 
import scipy.integrate as integrate
import random as rand
#Python 3
#Rebeca Baños


def convolucion(x1,x2):
	i=0
	for i in range(0,len(x2)-1):
		res[i] = integrate.quad(x2[i]*x1,0,x1)
	return res
		

def generaFuncion(numAl):	
	if numAl<50:
		x = 0
	elif numAl<100:
		x = 1
	else:
		x = 0
	return x

#x1 = [[0, 0<t<50], [1,50<t<100], [0, 100<t<150]]
x2 = [0.25,0.25,0.25,0.25]
x3 = [0.05,0.25,0.4,0.25,0.05]
x4 = [1,0,-1]

numAl = rand.randrange(0,150)
x1 = generaFuncion(75)
print(x1)
print(convolucion(x1,x2))
