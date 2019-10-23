#Víctor Hugo Flores Pineda 155990
#Rebeca Baños Garcia 157655
#Python 3
import matplotlib.pyplot as plt
import numpy as np

#Ejercicio 1

def fourier(x,N,N1):
    res = np.zeros((2*N)+1)
    for i in range(-N,N):
        if(i!=0):
            ak = (1/N)*np.sin(2*np.pi*i*((N1+0.5)/N))/np.sin((np.pi*i)/N)
        else:
            ak = (2*N1+1)/N
        res[i+N] = ak
    return res

def funOrig(N,N1):
    aux = np.linspace(-N,N,(2*N)+1)
    x = np.zeros((2*N)+1)
    for i in aux:
        if(abs(aux[int(i)])<N1+1 or abs(aux[int(i)])>N1+(N/2)):
            x[int(i)] = 1
    return [aux,x]


#Caso 1
N=10
N1=2
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=10 y N1=2")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=10 y N1=2")

#Caso 2
N=20
N1=2
plt.figure()
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=20 y N1=2")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=20 y N1=2")

#Caso 3
N=40
N1=2
plt.figure()
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=40 y N1=2")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=40 y N1=2")

#Caso 4
N=30
N1=3
plt.figure()
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=30 y N1=3")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=30 y N1=3")

#Caso 5
N=30
N1=6
plt.figure()
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=30 y N1=6")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=30 y N1=6")

#Caso 6
N=30
N1=9
plt.figure()
[aux,x] = funOrig(N,N1)
plt.subplot(211)
plt.stem(aux,x)
plt.title("x[n], con N=30 y N1=9")

res = fourier(x,N,N1)
plt.subplot(212)
plt.stem(aux,res)
plt.title("ak, con N=30 y N1=9")

#Ejercicio 2


def fourier2(x,N,N1):
    res = np.zeros(40)
    for i in range(-20,20):
        if(i!=0):
            ak = (1/N)*np.sin(2*np.pi*i*((N1+0.5)/N))/np.sin((np.pi*i)/N)
        else:
            ak = (2*N1+1)/N
        res[i+20] = ak
    return res

def funOrig2(N,N1):
    aux = np.linspace(-20,20,40)
    x = np.zeros(40)
    for i in aux:
        if(abs(aux[int(i)])<N1+1 or abs(aux[int(i)])>N1+(N/2)):
            x[int(i)] = 1
    return [aux,x]

def sumaFourier(ak,M):
    x = np.linspace(-20,20,40)
    euler = np.zeros(40)
    for i in x:
        for j in range(1,M):
        	suma = 2 * ak[int(j)] * np.cos((j*2*np.pi*i)/9)
    	euler[int(i)] = ak[20] + suma
    return euler

N = 9
N1 = 2
[aux,x] = funOrig2(N,N1)
ak = fourier2(x,N,N1)
res = sumaFourier(ak,1)
plt.figure()
plt.plot(aux,res)
      

plt.show()
