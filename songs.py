# Jean Paul Gonzalez Pedraza
#codigo: 8954011
from sys import stdin

def main():
    cantCanciones = stdin.readline().rstrip()
    while(cantCanciones != ""):
        cantCanciones = int(cantCanciones)
        lista=[]
        lista2=[]
        numeroTotal=cantCanciones*3
        while(numeroTotal!=0):
            linea = list(map(float, stdin.readline().rstrip().split()))
            lista.extend(linea)
            numeroTotal-=len(linea)
        uno, dos , tres = 0,1,2
        for i in range(cantCanciones):
            S, longitud,frecuencia=(lista[uno], lista[dos], lista[tres])
            lista2.append((longitud/frecuencia, longitud, frecuencia, int(S)))
            uno += 3
            dos += 3
            tres += 3 
        lista2.sort()
        song = int(stdin.readline().rstrip())
        respuesta=lista2[song-1]
        print(int(respuesta[3]))
        cantCanciones = stdin.readline().rstrip()
main()