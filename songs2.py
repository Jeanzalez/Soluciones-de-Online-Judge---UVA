from sys import stdin

def main():
    cantCanciones = stdin.readline().rstrip()
    while(cantCanciones != ""):
        cantCanciones = int(cantCanciones)
        lista=[]
        for i in range(cantCanciones):
            S, longitud,frecuencia=list(map(float, stdin.readline().rstrip().split()))
            lista.append((longitud/frecuencia, longitud, frecuencia, S))
        lista.sort()
        song = int(stdin.readline().rstrip())
        respuesta=lista[song-1]
        print(int(respuesta[3]))
        cantCanciones = stdin.readline().rstrip()
main()