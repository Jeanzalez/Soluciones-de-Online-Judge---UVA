# Jean Paul Gonzalez Pedraza
#codigo: 8954011

from sys import stdin

def fair(regalo, plataPersona2, cantPersonas, plataPersona):
    ans = [0 for _ in range(len(plataPersona2))]
    if(sum(plataPersona)>=regalo):
        for i in range (len(plataPersona2)):
            DineroCadaUno=regalo//cantPersonas
            if(plataPersona2[i][0]<=DineroCadaUno):
                regalo-=plataPersona2[i][0]
                ans[plataPersona2[i][1]] = plataPersona2[i][0]
            else:
                regalo-=DineroCadaUno
                ans[plataPersona2[i][1]]=(DineroCadaUno)
            cantPersonas-=1
    else:
        ans = "IMPOSSIBLE"
    return ans

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        regalo, cantPersonas = list(map(int, stdin.readline().rstrip().split()))
        plataPersona = list(map(int, stdin.readline().rstrip().split()))
        indices = {}
        for i in range(len(plataPersona)):
            numero = plataPersona[i]
            if(numero not in indices):
                indices[numero] = []
            indices[numero].append(i)
        plataPersona.sort()
        nuevosIndices = []
        for i in range(len(plataPersona)):
            nuevosIndices.append(indices[plataPersona[i]].pop())
        plataPersona2=[]
        for i in range(len(plataPersona)):
            plataPersona2.append((plataPersona[i],nuevosIndices[i]))
        respuesta=fair(regalo, plataPersona2, cantPersonas, plataPersona)
        if(respuesta=="IMPOSSIBLE"):
            print(respuesta)
        else:
            print(' '.join(map("{}".format, respuesta)))
        cantCasos-=1
main()