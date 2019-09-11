import numpy as np
import matplotlib.pyplot as pl

#inciso 1
x = [0,2,4,-1]
h = [1,1,1,1]

c = np.convolve(x,h)
print(c)
pl.figure()
pl.stem(np.linspace(0,6,7),c)
pl.xlim(-2,8)
pl.ylim(-2,7)

#inciso 2
n = np.linspace(0,20,20)
x1 = np.cos(((np.pi)/10)*n)
h1 = np.random.rand(1,11)
pl.figure()
pl.subplot(221)
pl.stem(np.linspace(0,20,20),x1)
pl.subplot(222)
pl.stem(np.linspace(0,10,11),h1[0])
pl.xlim(-2,12)
pl.ylim(-1,1)

#Checar conmutativa
c1 = np.convolve(x1,h1[0])
c2 = np.convolve(h1[0],x1)
print(c1)
pl.subplot(223)
pl.stem(np.linspace(0,20,30),c1)
pl.subplot(224)
pl.stem(np.linspace(0,20,30),c2)


#inciso 3
h2 = np.random.rand(1,11)*-1
pl.figure()
pl.subplot(331)
pl.stem(np.linspace(0,20,20),x1)
pl.subplot(332)
pl.stem(np.linspace(0,10,11),h1[0])
pl.subplot(333)
pl.stem(np.linspace(0,10,11),h2[0])
pl.xlim(-2,12)
pl.ylim(-1,1)

#Checar distributiva
c3 = np.convolve(x1,(h1[0]+h2[0]))
print(c3)
pl.subplot(334)
pl.subplot(335)
pl.stem(np.linspace(0,10,11),h1[0]+h2[0])
pl.stem(np.linspace(0,20,30),c3)
c4 = np.convolve(x1,h1[0])+np.convolve(x1,h2[0])
print(c4)
pl.subplot(336)
pl.stem(np.linspace(0,20,30),c3)


pl.show()