#Convolución
import numpy as np 
import scipy as sp
import matplotlib.pyplot as pl 
import scipy.integrate as integrate
import random as rand
#Python 3
#Rebeca Baños


def convolucion(x1,x2):
	if len(x1)>len(x2):
		n = len(x1)
	else:
		n = len(x2)
	res = np.zeros(n)
	for i in range(0,n):
		val = 0
		for j in range(0,n):
			if (i-j)>=0 and (i-j)<len(x2) and (j)<len(x1):
				val = val + x1[j]*x2[i-j]
			res[i] = val
	return res
		

x1 = np.append(np.zeros(50),[np.ones(50),np.zeros(50)])
x2 = [0.25,0.25,0.25,0.25]
x3 = [0.05,0.25,0.4,0.25,0.05]
x4 = [1,0,-1]

 
print("Convolución x1 vs x2")
x1vsx2 = convolucion(x1,x2)
print(x1vsx2)
pl.figure()
pl.stem(np.linspace(0,1,2),x1vsx2)
print("Convolución x1 vs x3")
print( 	convolucion(x1,x3))
print("Convolución x1 vs x4")
print( 	convolucion(x1,x4 ))

pl.show()