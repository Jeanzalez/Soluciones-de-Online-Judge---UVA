from sys import stdin

def binsearchFirst(A, low, hi, x): #forma recursiva
    ans = None
    if low > hi: 
        ans = -1
    else:
        mid = low + ((hi - low) >> 1)
        if A[mid] == x:
            left = binsearchFirst(A, low, mid - 1, x)
            ans = left if left != -1 else mid
        elif A[mid] < x:
            ans = binsearchFirst(A, mid + 1, hi, x)
        else:
            ans = binsearchFirst(A, low, mid - 1, x)
    return ans

def binsearchLast(A, low, hi, x): #forma recursiva
    ans = None
    if low > hi: ans = -1
    else:
        mid = low + ((hi - low) >> 1)
        if A[mid] == x:
            right = binsearchLast(A, mid + 1, hi, x)
            ans = right if right != -1 else mid
        elif A[mid] < x:
            ans = binsearchLast(A, mid + 1, hi, x)
        else:
            ans = binsearchLast(A, low, mid - 1, x)
    return ans



def main():
    cantNumeros = stdin.readline().rstrip()
    while(cantNumeros!= ""):
        cantNumeros = int(cantNumeros)
        lista = []
        for i in range(cantNumeros):
            numero=int(stdin.readline().rstrip())
            lista.append(numero)
        lista.sort()
        tamLista=len(lista)
        if(tamLista == 1):
            print(f'{lista[0]} {1} {1}')
        elif(tamLista % 2 == 0):
            mitadLista = tamLista // 2
            PrimerAparicion = binsearchFirst(lista,0,len(lista)-1,lista[mitadLista - 1])
            UltimaAparicion = binsearchLast(lista,0,len(lista)-1,lista[mitadLista])
            if(lista[mitadLista - 1] == lista[mitadLista]):
                print(lista[mitadLista-1])
                print(lista[mitadLista])
                A = lista[PrimerAparicion]
                B = (UltimaAparicion - PrimerAparicion) + 1
                C = 1
                print(f'{A} {B} {C}')
            else:
                A = lista[PrimerAparicion]
                B = (UltimaAparicion - PrimerAparicion) + 1
                C = 1
                for i in range(lista[mitadLista - 1], lista[mitadLista]):
                    C += 1
                print(f'{A} {B} {C}')
        else:
            mitadLista = tamLista // 2
            PrimerAparicion = binsearchFirst(lista,0,len(lista)-1,lista[mitadLista])
            UltimaAparicion = binsearchLast(lista,0,len(lista)-1,lista[mitadLista])
            A = lista[PrimerAparicion]
            B = (UltimaAparicion - PrimerAparicion) + 1
            C = 1
            print(f'{A} {B} {C}')
        cantNumeros=stdin.readline().rstrip()
main()