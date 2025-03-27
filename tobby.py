from sys import stdin
from heapq import heappush,heappop


def main():
    casos=int(stdin.readline().rstrip())
    while(casos!=0):
        n, k=map(int,stdin.readline().rstrip().split())
        ColaDePrioridad = []
        diccionario = {}
        for i in range(n):
            linea=stdin.readline().rstrip().split()
            tripleta=(int(linea[1]),i+1,linea[0])
            diccionario[linea[0]] = int(linea[1])
            heappush(ColaDePrioridad, tripleta)
        for i in range(k):
            frecuencia, prioridad, nombre = heappop(ColaDePrioridad)
            print(f'{frecuencia} {nombre}')
            valor = diccionario[nombre]
            heappush(ColaDePrioridad, (frecuencia + valor, prioridad, nombre))
        casos=casos - 1

main()