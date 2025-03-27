from sys import stdin
from collections import deque


def main():
    contadorEscenarios = 1
    comando = int(stdin.readline())
    numEquipo = comando
    while(comando != 0 ):
        TodosLosEquiposEncolados=deque()
        listaEncolados=deque()
        diccionarioEquipos={}
        for k in range(0,numEquipo):
            i=deque()
            TodosLosEquiposEncolados.append(i)
            linea=stdin.readline()
            separado = linea.split()
            for x in range(1,len(separado)):
                diccionarioEquipos[separado[x]]=k
        print('Scenario #{}'.format(contadorEscenarios))
        comando=stdin.readline().strip()
        comando=comando.split()
        while(comando[0]!="STOP"):
            if(comando[0]=="ENQUEUE"):
                posicion=diccionarioEquipos.get(comando[1])
                if(len(TodosLosEquiposEncolados[posicion])==0):
                    listaEncolados.append(posicion)
                TodosLosEquiposEncolados[posicion].append(comando[1])
            elif(comando[0]=="DEQUEUE"):
                posicion = listaEncolados[0]
                print(TodosLosEquiposEncolados[posicion].popleft())
                if(len(TodosLosEquiposEncolados[posicion])==0):
                    listaEncolados.popleft()
            comando=stdin.readline().strip()
            comando=comando.split()
        print()
        contadorEscenarios+=1
        numEquipo=int(stdin.readline())
        comando=numEquipo
        

main()


