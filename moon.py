from sys import stdin
import math

def conversionDiasSegundos(dias):
    segundos = dias * 86400
    return segundos

def conversionKmAMm(km):
    mm = km * 1000000
    return mm

def f(Tons):
    Velocidad = DMm / TSeg
    ans = Tons - Velocidad
    return ans

def biseccion(f, a, b, v):
    low, hi, ans = a, b, None
    eps = 1e-6
    while hi - low > eps:
        mid = (hi + low) / 2
        if v <= f(mid): hi = mid
        else: low = mid
    ans = low
    return ans



def main():
    global TSeg,S,DMm
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        Linea = list(map(int, stdin.readline().rstrip().split()))
        TSeg = conversionDiasSegundos(Linea[0])
        S = Linea[1]
        DMm = conversionKmAMm(Linea[2])
        Respuesta = biseccion(f, -800000  , 800000, 0)
        if(math.floor(Respuesta) <= 0):
            print(f'Add {math.floor(math.fabs(Respuesta))} tons')
        else:
            print(f'Remove {math.floor(Respuesta)} tons')
        cantCasos-=1

main()