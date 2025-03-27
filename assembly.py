# Jean Paul Gonzalez Pedraza
#codigo: 8954011
from sys import stdin

def assembly(cantAlturas, alturas):
    ans = 0
    movimientos = 0
    alturaOrdenCorrecto = 1
    for i in range(cantAlturas):
        if(alturas[i] == alturaOrdenCorrecto):
            alturaOrdenCorrecto += 1
        else:
            movimientos += 1
    ans = movimientos
    return ans

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        cantAlturas = int(stdin.readline().rstrip())
        alturas = list(map(int, stdin.readline().rstrip().split()))
        respuesta=assembly(cantAlturas, alturas)
        print("Case {}: {}".format(caso, respuesta))
        caso += 1
        cantCasos-=1
main()