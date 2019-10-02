#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3

import numpy as np

def simularEnvios(p):
    n = round((50 / (p * p))*1.5)
    envCorrA = 0
    envCorrB = 0
    colision = 0
    colAck = 0
    maxRepeat = 0
    ack = False
    repeat = 0
    for i in range(1,n):
        envioA = 1 if (np.random.randint(1,1001)/1000)<=p and ack == False else 0  
        envioB = 1 if (np.random.randint(1,1001)/1000)<=p else 0
        if (envioA and envioB) or (ack and envioB):
            colision = colision + 1
        elif envioA:
            envCorrA = envCorrA + 1
            ack = True
        elif envioB:
            envCorrB = envCorrB +1
        else:
            ack = False
            repeat = 0

        if(ack and envioB):
            repeat = repeat + 1
            colAck = colAck + 1
        if(repeat==2):
            repeat = 0 
            ack = False
            maxRepeat = maxRepeat +1
            
    return [n,colision,envCorrA,envCorrB, colAck, maxRepeat]

p1 = 0.1
sim1 = simularEnvios(p1)
print("Probabilidad de envío 0.1")
print("número de ranuras simuladas: " + str(sim1[0]))
print("número de colisiones: " + str(sim1[1]))
print("colisiones del ack: " + str(sim1[4]))
print("veces que se alcanzó el número máximo de retransmisiones: " + str(sim1[5]))
print("total de tramas enviadas correctamente: " + str(sim1[2]+sim1[3]) )
print("tramas enviadas correctamente por A: " + str(sim1[2]) )
print("tramas enviadas correctamente por B: " + str(sim1[3]) )
print("\n")

p2 = 0.07 
sim2 = simularEnvios(p2)
print("Probabilidad de envío 0.07")
print("número de ranuras simuladas: " + str(sim2[0]))
print("número de colisiones: " + str(sim2[1]))
print("colisiones del ack: " + str(sim2[4]))
print("veces que se alcanzó el número máximo de retransmisiones: " + str(sim2[5]))
print("total de tramas enviadas correctamente: " + str(sim2[2]+sim2[3]) )
print("tramas enviadas correctamente por A: " + str(sim2[2]) )
print("tramas enviadas correctamente por B: " + str(sim2[3]) )
print("\n")

p3 = 0.05
sim3 = simularEnvios(p3)
print("Probabilidad de envío 0.05")
print("número de ranuras simuladas: " + str(sim3[0]))
print("número de colisiones: " + str(sim3[1]))
print("colisiones del ack: " + str(sim3[4]))
print("veces que se alcanzó el número máximo de retransmisiones: " + str(sim3[5]))
print("total de tramas enviadas correctamente: " + str(sim3[2]+sim3[3]) )
print("tramas enviadas correctamente por A: " + str(sim3[2]) )
print("tramas enviadas correctamente por B: " + str(sim3[3]) )
print("\n")

p4 = 0.01 
sim4 = simularEnvios(p4)
print("Probabilidad de envío 0.01")
print("número de ranuras simuladas: " + str(sim4[0]))
print("número de colisiones: " + str(sim4[1]))
print("colisiones del ack: " + str(sim4[4]))
print("veces que se alcanzó el número máximo de retransmisiones: " + str(sim4[5]))
print("total de tramas enviadas correctamente: " + str(sim4[2]+sim4[3]) )
print("tramas enviadas correctamente por A: " + str(sim4[2]) )
print("tramas enviadas correctamente por B: " + str(sim4[3]) )
print("\n")

p5 = 0.005
sim5 = simularEnvios(p5)
print("Probabilidad de envío 0.005")
print("número de ranuras simuladas: " + str(sim5[0]))
print("número de colisiones: " + str(sim5[1]))
print("colisiones del ack: " + str(sim5[4]))
print("veces que se alcanzó el número máximo de retransmisiones: " + str(sim5[5]))
print("total de tramas enviadas correctamente: " + str(sim5[2]+sim5[3]) )
print("tramas enviadas correctamente por A: " + str(sim5[2]) )
print("tramas enviadas correctamente por B: " + str(sim5[3]) )
print("\n")

    