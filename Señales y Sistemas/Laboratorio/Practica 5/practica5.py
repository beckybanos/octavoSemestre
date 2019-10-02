#Víctor Hugo Flores Pineda 155990
#Python 3
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,250,251)
y = np.cos(x/3)
z = np.cos(x/4)
w = y + z

plt.subplot(311)
plt.plot(x,y)
plt.subplot(312)
plt.plot(x,z)
plt.subplot(313)
plt.plot(x,w)

plt.figure()
x = np.linspace(-12,12,200)
# periodo 0
y = np.zeros(200)+2
# periodo 3
z = np.cos(2*np.pi*x/3)
# periodo 6/5
w = 4*np.sin(5*np.pi*x/3)
# periodo señal sumada completa
v = y + z + w
plt.subplot(411)
plt.plot(x,y)
plt.subplot(412)
plt.plot(x,z)
plt.subplot(413)
plt.plot(x,w)
plt.subplot(414)
plt.plot(x,v)


plt.figure()
x = np.linspace(-1,1,100)
#primer termino de la serie
t1 = (4/np.pi)*np.sin(x*np.pi)
plt.plot(x,t1)
#segundo termino de la serie
t2 = (4/np.pi)*(1/3)*np.sin(3*x*np.pi)
plt.plot(x,t2,'m')
#tercer termino de la serie
t3 = (4/np.pi)*(1/5)*np.sin(5*x*np.pi)
plt.plot(x,t3,'r')
#cuarto termino de la serie
t4 = (4/np.pi)*(1/7)*np.sin(7*x*np.pi)
plt.plot(x,t4,'g')
#quinto termino de la serie
t5 = (4/np.pi)*(1/9)*np.sin(9*x*np.pi)
plt.plot(x,t5,'c')
#sexto termino de la serie
t6 = (4/np.pi)*(1/11)*np.sin(11*x*np.pi)
plt.plot(x,t6,'y')
#suma de los primeros seis terminos de la serie de fourier
s = t1 + t2 + t3 + t4 + t5 + t6
plt.plot(x,s,'k')


sum = np.zeros(100)
aux = 1
for val in range(0,25):
    term = (4/np.pi)*(1/aux)*np.sin(aux*x*np.pi)
    aux = aux + 2
    sum = sum + term

plt.figure()
plt.plot(x,sum)

x = np.linspace(-2,2,200)
sum2 = np.zeros(200)
aux = 1
for val in range(0,50):
    term = (1/(aux**2))*np.sin(aux*x*np.pi)
    aux = aux + 2
    sum2 = sum2 + ((-1)**val)*term
sum2 = (8/(np.pi**2))*sum2

plt.figure()
plt.plot(x,sum2)



x = np.linspace(-2,2,200)
sum3 = np.zeros(200)
for val in range(1,50):
    term = (1/val)*np.sin(val*x*np.pi)
    sum3 = sum3 + ((-1)**(val+1))*term
sum2 = (2/np.pi)*sum3

plt.figure()
plt.plot(x,sum3)



plt.show()