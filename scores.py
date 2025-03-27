from sys import stdin
from heapq import heappush,heappop

def main():
    comando=stdin.readline().strip()
    comando=comando.split()
    while(len(comando)!=0):
        cantGrupos=int(comando[1])
        partiturasCant=int(comando[0])-cantGrupos
        comando=stdin.readline().strip()
        comando=comando.split()
        gruposPartituras=[]
        for i in range(cantGrupos):
            numero=int(comando[i])
            tupla=((numero*(-1)),numero,0)
            heappush(gruposPartituras,tupla)
        while(partiturasCant!=0):
            tuplaActual=heappop(gruposPartituras)
            divisorCont=tuplaActual[2]
            grupoDividido=(tuplaActual[1])
            if(grupoDividido%(2+divisorCont)==0):
                GrupograndeDiv1=grupoDividido//(2+divisorCont)
                divisorCont+=1
                tuplaR=((GrupograndeDiv1*(-1)),grupoDividido,divisorCont)
                heappush(gruposPartituras,tuplaR)
            else:
                GrupograndeDiv1=int((grupoDividido/(2+divisorCont))+1)
                divisorCont+=1
                tuplaR=((GrupograndeDiv1*(-1)),grupoDividido,divisorCont)
                heappush(gruposPartituras,tuplaR)
            partiturasCant-=1 
        resultado=heappop(gruposPartituras)
        result=resultado[0]*(-1)
        print(result)
        comando=stdin.readline().strip()
        comando=comando.split()

main()