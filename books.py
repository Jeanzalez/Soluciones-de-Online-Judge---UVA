from sys import stdin

def validacion(lista,capacidadEvaluar,cantEscribas):
    val=False
    contEscriba=0
    j = 0
    acumTotal = 0
    while(contEscriba<cantEscribas):
        acumuladorEscriba=0
        while(j < len(lista) and acumuladorEscriba+lista[j] <= capacidadEvaluar):
            acumuladorEscriba+=lista[j]
            j+=1
        acumTotal += acumuladorEscriba
        contEscriba+=1
    if(j == len(lista)):
        val=True
    else:
        val=False
    return val



def binarySearch(lista,low,hight,cantEscribas):
    ans=False
    mid=0
    respuesta=0
    while(low+1!=hight):
        mid=(low+hight)//2
        ans=validacion(lista,mid,cantEscribas)
        if(ans==True):
            hight=mid
        else:
            low=mid
    respuesta=hight
    return respuesta


def main():
    contadorCasos = 0
    numCasos = int(stdin.readline())
    while(contadorCasos < numCasos ):
        comando=stdin.readline()
        separado = comando.split()
        cantLibros=int(separado[0])
        cantEscribas=int(separado[1])
        comando=stdin.readline()
        separado = comando.split()
        separadoN=list(map(int,separado))
        Respuesta=binarySearch(separadoN,0,sum(separadoN),cantEscribas)
        matriz=[]
        for i in range(cantEscribas):
            matriz.append([])
        
        contlibros=cantLibros
        contEscribas=cantEscribas
        posicion=0
        x=len(separadoN)-1
        while(contlibros!=0 and contEscribas!=0):
            acuEscriba=0
            contEscribas-=1
            while(acuEscriba+separadoN[x]<=Respuesta and contlibros-contEscribas!=0 and x>=0):
                acuEscriba+=separadoN[x]
                matriz[posicion].append(separadoN[x])
                contlibros-=1
                x-=1
            posicion+=1
        n=len(matriz)-1
        while(n>=0):
            j=len(matriz[n])-1
            while(j>=0):
                if(j==0):
                    print('{}'.format(matriz[n][j]), end='')
                else:
                    print('{} '.format(matriz[n][j]), end='')
                j-=1
            if(n!=0):
                print(' {} '.format("/"), end='')
            n-=1
        print()
        contadorCasos+=1

main()