#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import numpy as np 
import matplotlib.pyplot as plt 


def generarTramas():
    tramas = list()
    rand = np.random.randint(5,11,1000)
    for i in range(0,999):
        tramas.append(np.random.bytes(rand[i]))
    distTramas(rand)    

def distTramas(rand):
        count = np.zeros(6)
        for j in rand:
                index = j-5
                count[index] = count[index]+1  
        print(count)

generarTramas()

