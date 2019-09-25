import numpy as np
import matplotlib.pyplot as plt

#Inciso 1
t = np.linspace(0,250,251)
x = np.cos(t/3)
y = np.cos(t/4)
w = x+y

plt.figure()
plt.subplot(311)
plt.plot(t,x)
plt.subplot(312)
plt.plot(t,y)
plt.subplot(313)
plt.plot(t,w)

#Inciso 2
t1 = np.linspace(-12,12,200)
x1 = np.zeros(200)+2
y1 = np.cos(2*np.pi*(t1/3))
z1 = 4*np.sin(5*np.pi*(t1/3))
w1 = x1+y1+z1

plt.figure()
plt.subplot(411)
plt.plot(t1,x1)
plt.ylim(-5,6)
plt.xlim(-12,12)
plt.subplot(412)
plt.plot(t1,y1)
plt.ylim(-5,6)
plt.xlim(-12,12)
plt.subplot(413)
plt.plot(t1,z1)
plt.ylim(-5,6)
plt.xlim(-12,12)
plt.subplot(414)
plt.plot(t1,w1)
plt.ylim(-5,7)
plt.xlim(-12,12)

#Inciso 4
w0=np.pi
t2 = np.linspace(-1,1,100)
x2=(4/np.pi)*np.sin(w0*t2)
y2=(4/np.pi)*(1/3)*np.sin(3*w0*t2)
z2=(4/np.pi)*(1/5)*np.sin(5*w0*t2)
w2=(4/np.pi)*(1/7)*np.sin(7*w0*t2)
a2=(4/np.pi)*(1/9)*np.sin(9*w0*t2)
b2=(4/np.pi)*(1/11)*np.sin(11*w0*t2)
s = x2+y2+z2+w2+a2+b2

plt.figure()
plt.plot(t2,x2,'b')
plt.plot(t2,y2,'m')
plt.plot(t2,z2,'r')
plt.plot(t2,w2,'g')
plt.plot(t2,a2,'c')
plt.plot(t2,b2,'y')
plt.plot(t2,s,'k')

#Inciso 5
t3 = np.linspace(-1,1,100)
sum=np.zeros(100)
aux = 1
for cant in range(1,50):
	x=(4/np.pi)*(1/i)*(np.sin(i*np.pi*t3))
	i=i+2

plt.figure()
plt.plot(t3,x)

plt.show()