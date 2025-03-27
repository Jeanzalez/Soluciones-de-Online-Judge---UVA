from sys import stdin
from collections import deque



def main():
    comando = int(stdin.readline())
    cantCasos=comando
    while(cantCasos > 0):
        pqLeft=deque()
        pqRight=deque()
        comando=stdin.readline().strip()
        comando=comando.split()
        cantCarrosBarco=int(comando[0])
        tiempo=int(comando[1])
        cantInstrucciones=int(comando[2])
        for i in range(cantInstrucciones):
            comando=stdin.readline().strip()
            comando=comando.split()
            if(comando[1]=="left"):
                pqLeft.append(int(comando[0]))
            elif(comando[1]=="right"):
                pqRight.append(int(comando[0]))
        contTiempo = 0
        estadoFerry="L"
        while(len(pqLeft)!=0 or len(pqRight!=0)):
            pass

        cantCasos+=1


main()