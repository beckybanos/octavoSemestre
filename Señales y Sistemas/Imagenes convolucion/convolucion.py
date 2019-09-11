#Convolución
import numpy as np 
import matplotlib.pyplot as pl
#Python 3
#Rebeca Baños	157655

#Función que realiza la convolución de dos funciones
def convolucion(x1,x2):
	n = max(len(x1),len(x2))
	res = np.zeros(n)
	for i in range(0,n):
		ind = 0
		for j in range(0,n):
			if (i-j)>=0 and (i-j)<len(x2) and (j)<len(x1):
				ind = ind + x1[j]*x2[i-j]
			res[i] = ind
	return res
		
#Funciones de prueba
x1 = np.append(np.zeros(50),[np.ones(50),np.zeros(50)])
x2 = [0.25,0.25,0.25,0.25]
x3 = [0.05,0.25,0.4,0.25,0.05]
x4 = [1,0,-1]


#Graficas de las funciones
#x1
pl.figure()
a = pl.subplot(221)
a.set_title("Funcion x1")
pl.stem((np.linspace(0,149,150)),x1)

#x2
b = pl.subplot(222)
b.set_title("Función x2")
pl.stem([0,1,2,3],x2)

#x3
c = pl.subplot(223)
c.set_title("Función x3")
pl.stem([0,1,2,3,4],x3)

#x4
d = pl.subplot(224)
d.set_title("Función x4")
pl.stem([0,1,2],x4)


#inciso 1
print("Convolución x1 vs x2")
x1vsx2 = convolucion(x1,x2)
print(x1vsx2)
pl.figure()
n = max(len(x1),len(x2))
pl.stem((np.linspace(0,n-1,n)),x1vsx2)
e = pl.subplot(321)
e.set_title("Convolucion de x1 con x2")

#inciso 2
print("Convolución x1 vs x3")
x1vsx3 = convolucion(x1,x3)
print(x1vsx3)
n = max(len(x1),len(x3))
pl.stem((np.linspace(0,n-1,n)),x1vsx3)
f = pl.subplot(322)
f.set_title("Convolucion de x1 con x3")

#inciso 3
print("Convolución x1 vs x4")
x1vsx4 = convolucion(x1,x4)
print(x1vsx4)
n = max(len(x1),len(x4))
pl.stem((np.linspace(0,n-1,n)),x1vsx4)
g = pl.subplot(323)
g.set_title("Convolucion de x1 con x4")

#inciso 4
print("Convolución x3 vs x4")
x3vsx4 = convolucion(x3,x4)
print(x3vsx4)
n = max(len(x3),len(x4))
pl.stem((np.linspace(0,n-1,n)),x3vsx4)
h = pl.subplot(324)
h.set_title("Convolucion de x3 vs x4")

print("Convolución x1 vs x3*x4")
x3vsx4 = convolucion(x3,x4)
x1vsx3x4 = convolucion(x1,x3vsx4)
print(x1vsx3x4)
n = max(len(x1),len(x4),len(x3))
pl.stem((np.linspace(0,n-1,n)),x1vsx3x4)
h = pl.subplot(325)
h.set_title("Convolucion de x1 con x3*x4")

#inciso 5
print("Convolución x1 vs x1")
x1vsx1 = convolucion(x1,x1)
print(x1vsx1)
n = max(len(x1),len(x1))
pl.stem((np.linspace(0,n-1,n)),x1vsx1)
i = pl.subplot(326)
i.set_title("Convolucion de x1 con x1")


pl.show()