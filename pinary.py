from sys import stdin

lista = []

def Fibonacci(n):
    global lista
    while len(lista) < n:
        if len(lista) < 2:
            lista.append(len(lista) + 1)
        else:
            lista.append(lista[-1] + lista[-2])


def numeroPinario(posicion):
    ans = 10 ** (posicion - 1)
    return ans

def binsearch(A, low, hi, x): #forma recursiva
    global lista
    ans = None
    if(hi < low): ans = low
    else:
        mid = low+((hi-low)>>1)
        if(A[mid]==x): ans = mid + 1
        elif(A[mid] < x): ans = binsearch(A, mid + 1, hi, x)
        else: ans = binsearch(A, low, mid - 1, x)
    return ans


def main():
    global lista
    Fibonacci(38)
    casos=int(stdin.readline().rstrip())
    while(casos!=0):
        acu=0
        linea=int(stdin.readline().rstrip())
        while(linea != 0):
            indice = binsearch(lista,0,len(lista)-1, linea)
            pinario = (numeroPinario(indice))
            acu= acu + pinario
            linea = linea - lista[indice - 1]
        print(acu)
        casos=casos - 1
main()