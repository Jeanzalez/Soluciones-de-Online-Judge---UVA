from sys import stdin

def calcular(hipopotamos, H, Ta, Td):
    tiempo=0
    i=len(hipopotamos)-1
    j=0
    while(i>=j):
        if(i==j):
            i-=1
            tiempo+=Ta
        elif(i==1 and j==0 and hipopotamos[i]+hipopotamos[j]<H):
            if((Ta*2)<Td):
                i-=2
                tiempo=tiempo + Ta + Ta    
            else:
                i-=2
                tiempo+=Td
        elif(hipopotamos[i]+hipopotamos[j]<H):
            if((Ta*2)<Td):
                i-=1
                tiempo+=Ta    
            else:
                j+=1
                i-=1
                tiempo+=Td
        else:
            i-=1
            tiempo+=Ta
    return tiempo


def main():
    casos=int(stdin.readline().rstrip())
    contCasos=1
    while(casos!=0):
        linea=stdin.readline().rstrip().split(" ")
        numHipo = int(linea[0])
        H = int(linea[1])
        Ta = int(linea[2])
        Td = int(linea[3])
        linea=stdin.readline().rstrip().split(" ")
        lista = list(map(int, linea))
        lista.sort()
        Respuesta=calcular(lista, H, Ta, Td)
        print(f'Case {contCasos}: {Respuesta}')
        casos=casos - 1
        contCasos+=1

main()