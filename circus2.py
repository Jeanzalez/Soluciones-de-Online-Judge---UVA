from sys import stdin


def busquedaBinaria(hipopotamos, H, Ta, Td):
    tiempo=0
    while(len(hipopotamos)!=0):
        low=0
        hi=len(hipopotamos)-1
        while(low+1!=hi and hi!=0):
            mid=(low+hi)//2
            if(hipopotamos[mid]+hipopotamos[hi]<H):
                low=mid  
            else:
                hi=mid  
        if(hipopotamos[low]+hipopotamos[hi]<H and hi!=low):
            hipopotamos.pop(hi)
            hipopotamos.pop(low)
            tiempo+=Td
        elif(len(hipopotamos)!=0):
            hipopotamos.pop(low)
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
        Respuesta=busquedaBinaria(lista,H,Ta,Td)
        print(f'Case {contCasos}: {Respuesta}')
        casos=casos - 1
        contCasos+=1

main()