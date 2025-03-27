# Jean Paul Gonzalez Pedraza
#codigo: 8954011
from sys import stdin

def terror(N, K, LineaXi, LineaYi):
    ans=None
    ganancia = 0
    lista=[]
    for i in range(len(LineaXi)):
        lista.append(LineaYi[i]-LineaXi[i])
    lista.sort()
    for i in range(len(lista)):
        if(lista[i] < 0 and K > 0):
            K -= 1
        else:
            ganancia += lista[i]
    if(ganancia > 0):
        ans=ganancia
    else:
        ans="No Profit"
    return ans

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        N, K = list(map(int, stdin.readline().rstrip().split()))
        LineaXi = list(map(int, stdin.readline().rstrip().split()))
        LineaYi = list(map(int, stdin.readline().rstrip().split()))
        respuesta=terror(N,K, LineaXi, LineaYi)
        print("Case {}: {}".format(caso, respuesta))
        caso += 1
        cantCasos-=1
main()