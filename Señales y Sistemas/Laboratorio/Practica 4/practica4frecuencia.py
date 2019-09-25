import numpy as np
import matplotlib.pyplot as plt
#Python 2.7

#Se crea el vector base para el tiempo
t = np.linspace(0,2,200)
#Se genera la función normal
x = np.cos(2*np.pi*t)
#Se genera la función con diferente frecuencia
y = np.cos(2*np.pi*2*t)
#Se genera la función con desfase
z = np.cos((2*np.pi*2*t)+(np.pi/2))

#Se grafica la función normal con respecto al tiempo y la función con diferente frecuencia
plt.subplot(331)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva con desfase
plt.subplot(332)
plt.plot(x,y)
#Se grafica la curva de Lissajous
plt.subplot(333)
plt.plot(x,z)

#Se genera la segunda función con diferente frecuencia
y = np.cos(2*np.pi*3*t)
#Se genera la función con desfase
z = np.cos((2*np.pi*3*t)+(np.pi/2))

#Se grafica la función normal con respecto al tiempo y la función con diferente frecuencia
plt.subplot(334)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva con desfase
plt.subplot(335)
plt.plot(x,y)
#Se grafica la curva de Lissajous
plt.subplot(336)
plt.plot(x,z)


#Se genera la tercer función con diferente frecuencia
y = np.cos(2*np.pi*4*t)
#Se genera la función con desfase
z = np.cos((2*np.pi*4*t)+(np.pi/2))

#Se grafica la función normal con respecto al tiempo y la función con diferente frecuencia
plt.subplot(337)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
#Se grafica la curva con desfase
plt.subplot(338)
plt.plot(x,y)
#Se grafica la curva de Lissajous
plt.subplot(339)
plt.plot(x,z)

#Se muestran las gráficas
plt.show()