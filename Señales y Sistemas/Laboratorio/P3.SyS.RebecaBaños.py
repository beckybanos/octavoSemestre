import numpy as np
import matplotlib.pyplot as pl

#Calcular la convolucion de dos señales
#Señales
x = [0,2,4,-1]
h = [1,1,1,1]

#Se hace la convolución
c = np.convolve(x,h)
print(c)

#Se grafican las dos funciones y su convolución
pl.figure()
pl.subplot(221)
pl.stem([0,1,2,3],x)
pl.title("Función x")
pl.xlim(-1,5)
pl.ylim(-2,5)
pl.subplot(222)
pl.stem([0,1,2,3],h)
pl.title("Función h")
pl.xlim(-1,4)
pl.ylim(-2,4)
pl.subplot(223)
pl.stem(np.linspace(0,6,7),c)
pl.title("Convolución de x*h")
pl.xlim(-2,8)
pl.ylim(-2,7)



#Probar la propiedad conmutativa
#Se define n y las señales a convolucionar
n = np.linspace(0,20,20)
x1 = np.cos(((np.pi)/10)*n)
h1 = np.random.rand(1,11)
#Se grafican las señales
pl.figure()
pl.subplot(221)
pl.stem(np.linspace(0,20,20),x1)
pl.title("Función x")
pl.xlim(0,21)
pl.ylim(-2,2)
pl.subplot(222)
pl.stem(np.linspace(0,10,11),h1[0])
pl.title("Funcion h")
pl.xlim(-2,12)
pl.ylim(-1,2)

#Se hace la convolución entre x y h y al revés para probar la propiedad conmutativa
c1 = np.convolve(x1,h1[0])
c2 = np.convolve(h1[0],x1)
print(c1)
pl.subplot(223)
pl.stem(np.linspace(0,20,30),c1)
pl.title("Convolución de x*h")
pl.xlim(0,20)
pl.ylim(-5,5)
pl.subplot(224)
pl.stem(np.linspace(0,20,30),c2)
pl.title("Convolución de h*x")
pl.xlim(0,20)
pl.ylim(-5,5)



#Probar la propiedad distributiva
#Se define la nueva señal a convolucionar, las anteriores las llamamos de arriba
h2 = np.random.rand(1,11)*-1
#Se grafican las funciones
pl.figure()
pl.subplot(331)
pl.stem(np.linspace(0,20,20),x1)
pl.title("Función x")
pl.xlim(0,20)
pl.ylim(-1.5,1.5)
pl.subplot(332)
pl.stem(np.linspace(0,10,11),h1[0])
pl.title("Función h1")
pl.xlim(0,10)
pl.ylim(-1.5,1.5)
pl.subplot(333)
pl.stem(np.linspace(0,10,11),h2[0])
pl.title("Función h2")
pl.xlim(0,10)
pl.ylim(-1.5,1.5)

#Se sacan las convoluciones correspondientes para probar la propiedad distributiva
c3 = h1[0] + h2[0]
print(c3)
c4  = np.convolve(x1,h1[0])
print(c4)
c5 = np.convolve(x1,h2[0])
print(c5)
c6 = np.convolve(x1,(c3))
print(c6)
c7 = np.convolve(x1,h1[0])+np.convolve(x1,h2[0])
print(c7)

#Se grafican las gráficas de las convoluciones
pl.subplot(334)
pl.stem(np.linspace(0,10,11),c3)
pl.title("Nueva función h1+h2")
pl.xlim(0,10)
pl.ylim(-1.5,1.5)
pl.subplot(335)
pl.stem(np.linspace(0,20,30),c4)
pl.title("Convolución de x*h1")
pl.xlim(0,20)
pl.ylim(-5,5)
pl.subplot(336)
pl.stem(np.linspace(0,20,30),c5)
pl.title("Convolución de x*h2")
pl.xlim(0,20)
pl.ylim(-5,5)
pl.subplot(337)
pl.stem(np.linspace(0,30,30),c6)
pl.title("Convolución de x1*(h1+h2)")
pl.xlim(0,30)
pl.ylim(-2,2)
pl.subplot(338)
pl.stem(np.linspace(0,30,30),c7)
pl.title("Convolución de x*h1 más la convolución de x*h2")
pl.xlim(0,30)
pl.ylim(-2,2)


#Probar la propiedad asociativa
#Se mandan a llamar las funciones utilizadas anteriormente
#Se grafican las funciones que se van a convolucionar
pl.figure()
pl.subplot(331)
pl.stem(np.linspace(0,20,20),x1)
pl.title("Función x")
pl.xlim(0,20)
pl.ylim(-1.5,1.5)
pl.subplot(332)
pl.stem(np.linspace(0,10,11),h1[0])
pl.title("Función h1")
pl.xlim(0,10)
pl.ylim(-1.5,1.5)
pl.subplot(333)
pl.stem(np.linspace(0,10,11),h2[0])
pl.title("Función h2")
pl.xlim(0,10)
pl.ylim(-1.5,1.5)

#Se sacan las convoluciones necesarias para probar la propiedad asociativa
d = np.convolve(x1,h1[0])
print(d)
d1 = np.convolve(h1[0],h2[0])
print(d1)
d2 = np.convolve((np.convolve(x1,h1[0])),h2[0])
print(d2)
d3 = np.convolve(x1,(np.convolve(h1[0],h2[0])))
print(d3)

#Se grafican las convoluciones resultantes
pl.subplot(334)
pl.stem(np.linspace(0,20,30),d)
pl.title("Convolución de x*h1")
pl.xlim(0,20)
pl.ylim(-5,5)
pl.subplot(335)
pl.stem(np.linspace(0,20,21),d1)
pl.title("Convolución de h1*h2")
pl.xlim(0,20)
pl.ylim(-5,5)
pl.subplot(337)
pl.stem(np.linspace(0,30,40),d2)
pl.title("Convolución de (x*h1)*h2")
pl.xlim(0,30)
pl.ylim(-10,10)
pl.subplot(338)
pl.stem(np.linspace(0,30,40),d3)
pl.title("Convolución de x*(h1*h2)")
pl.xlim(0,30)
pl.ylim(-10,10)



pl.show()