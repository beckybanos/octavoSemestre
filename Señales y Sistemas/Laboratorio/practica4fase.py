import numpy as np
import matplotlib.pyplot as plt
#Python3

#Se declara el vector base del tiempo
t = np.linspace(0,2)
#Se declaran las dos funciones a graficar, la segunda con el desfase adecuado
x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*t)

#Se grafica la gráfica coseno con respecto al tiempo y la función con desfase
plt.subplot(421)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva de Lissajous
plt.subplot(422)
plt.plot(x,y)

#Se genera la segunda funcion con diferente desfase
y = np.cos((2*np.pi*t)+(np.pi/4))

#Se grafica la función normal con el tiempo y la función con desfase
plt.subplot(423)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva de Lissajous
plt.subplot(424)
plt.plot(y,x)

#Se genera la tercer funcion con diferente desfase
y = np.cos((2*np.pi*t)+(np.pi/2))

#Se grafica la función normal con el tiempo y la función con desfase
plt.subplot(425)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva de Lissajous
plt.subplot(426)
plt.plot(y,x)

#Se genera la cuarta función con diferente desfase
y = np.cos((2*np.pi*t)+(3*np.pi/4))

#Se grafica la función normal con respecto al tiempo y la función con desfase
plt.subplot(427)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva de Lissajous
plt.subplot(428)
plt.plot(y,x)

#Se genera la quinta función con desfase
y = np.cos((2*np.pi*t)+(np.pi))

#Se grafica la función normal con respecto al tiempo y la función con desfase
plt.figure()
plt.subplot(121)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva de Lissajous
plt.subplot(122)
plt.plot(y,x)

#Muestra todas las gráficas
plt.show()