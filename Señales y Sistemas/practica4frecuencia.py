import numpy as np
import matplotlib.pyplot as plt
#Python 2.7

t = np.linspace(0,2,200)
x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*2*t)
z = np.cos((2*np.pi*2*t)+(np.pi/2))

plt.subplot(331)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(332)
plt.plot(x,y)
plt.subplot(333)
plt.plot(x,z)


t = np.linspace(0,2,200)
x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*3*t)
w = np.cos((2*np.pi*t)+(np.pi/2))
z = np.cos((2*np.pi*3*t)+(np.pi/2))

plt.subplot(334)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(335)
plt.plot(x,y)
plt.subplot(336)
plt.plot(x,z)


x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*4*t)
w = np.cos((2*np.pi*t)+(np.pi/2))
z = np.cos((2*np.pi*4*t)+(np.pi/2))

plt.subplot(337)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(338)
plt.plot(x,y)
plt.subplot(339)
plt.plot(x,z)



plt.show()