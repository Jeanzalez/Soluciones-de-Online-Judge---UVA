# Jean Paul Gonzalez Pedraza
#codigo: 8954011
from sys import stdin

def racing(TianJiCaballos, ReyCaballos):
    ans = 0
    i, j = 0, 0
    while(i < len(TianJiCaballos) and j < len(ReyCaballos)):
        if(TianJiCaballos[i] > ReyCaballos[j]):
            ans += 200
            i += 1
            j += 1
        elif(TianJiCaballos[-1] > ReyCaballos[-1]):
            ans += 200
            TianJiCaballos.pop()
            ReyCaballos.pop()
        elif(TianJiCaballos[i] < ReyCaballos[-1]):
            ans -= 200
            i += 1
            ReyCaballos.pop()
        else:
            i += 1
            ReyCaballos.pop()
    return ans

def main():
    Linea = int(stdin.readline().rstrip())
    while(Linea != 0):
        TianJi = list(map(int, stdin.readline().rstrip().split()))
        TianJi.sort()
        Rey = list(map(int, stdin.readline().rstrip().split()))
        Rey.sort()
        respuesta=racing(TianJi, Rey)
        print(respuesta)
        Linea = int(stdin.readline().rstrip())
main()
