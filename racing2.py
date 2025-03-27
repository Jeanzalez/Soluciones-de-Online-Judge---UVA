# Jean Paul Gonzalez Pedraza
#codigo: 8954011
from sys import stdin

def racing(TianJiCaballos, ReyCaballos):
    ans = 0
    while TianJiCaballos and ReyCaballos:
        if min(TianJiCaballos) > min(ReyCaballos):
            ans += 200
            TianJiCaballos.remove(min(TianJiCaballos))
            ReyCaballos.remove(min(ReyCaballos))
        elif max(TianJiCaballos) > max(ReyCaballos):
            ans += 200
            TianJiCaballos.remove(max(TianJiCaballos))
            ReyCaballos.remove(max(ReyCaballos))
        elif min(TianJiCaballos) < max(ReyCaballos):
            ans -= 200
            TianJiCaballos.remove(min(TianJiCaballos))
            ReyCaballos.remove(max(ReyCaballos))
        else:
            ans += 0
            TianJiCaballos.remove(min(TianJiCaballos))
            ReyCaballos.remove(min(ReyCaballos))
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