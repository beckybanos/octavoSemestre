import numpy as np
import matplotlib.pyplot as plt
#Python 2.7

t = np.linspace(0,2)
x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*t)

plt.subplot(421)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(422)
plt.plot(x,y)


x = np.cos(2*np.pi*t)
y = np.cos((2*np.pi*t)+(np.pi/4))

plt.subplot(423)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(424)
plt.plot(y,x)


x = np.cos(2*np.pi*t)
y = np.cos((2*np.pi*t)+(np.pi/2))

plt.subplot(425)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(426)
plt.plot(y,x)


x = np.cos(2*np.pi*t)
y = np.cos((2*np.pi*t)+(3*np.pi/4))

plt.subplot(427)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(428)
plt.plot(y,x)


x = np.cos(2*np.pi*t)
y = np.cos((2*np.pi*t)+(np.pi))

plt.figure()
plt.subplot(121)
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(122)
plt.plot(y,x)

plt.show()