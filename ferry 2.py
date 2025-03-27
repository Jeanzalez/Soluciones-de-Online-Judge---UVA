from sys import stdin
from collections import deque
import math

def minViajes(A,capMax, t):
    tiempo = 0
    carga=0
    carros=len(A)
    repetidos=0
    if(len(A)% 2 == 0 and capMax%2==1):#par el arreglo y impar la capMax
        tiempo=A[0] + (t*2)
        A.popleft()
        carros=len(A)
    elif(len(A)% 2 == 1 and capMax%2==0):#impar el arreglo y par la capMax
        tiempo=A[0] + (t*2)
        A.popleft()
        carros=len(A)
    elif(len(A)% 2 == 1 and capMax%2==1):#impar el arreglo y impar la capMax
        repetidos=A.count(A[0])
        tiempo=A[0] + (t*2)
        if(repetidos>capMax):
            for i in range(capMax):
                A.popleft()
        else:
            for i in range(repetidos):
                A.popleft()
        carros=len(A)
    while(carros!=0):
            if(carga<capMax):
                if(len(A)==0):
                    carga+=1
                elif(A[0]<=tiempo):
                    carga+=1
                    A.popleft()
                elif(A[0]>tiempo):
                    tiempo=A[0]
                    A.popleft()
                    carga+=1
            else:
                tiempo= tiempo + (t*2)
                carga=0
                carros=len(A)
    tiempo-=t
    return tiempo


def main():
    cantCasos=0
    casos = int(stdin.readline())
    while(cantCasos!=casos):
        comando = stdin.readline().strip()
        comando=comando.split()
        n,t,m=int(comando[0]),int(comando[1]),int(comando[2])
        lista=deque()
        for i in range(m):
            tiempoLlegada=int(stdin.readline().strip())
            lista.append(tiempoLlegada)
        solucion=minViajes(lista,n,t)
        print("{menor} {viajes}".format(menor = solucion, viajes = math.ceil(m/n)))

        cantCasos+=1


main()