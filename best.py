from sys import stdin

INF=float("inf")

def maxGanancia(m, n, lista,X, mem = {}):
    ans=None
    if(m == len(lista)):
        if(n > 5000):
            return 0
        return INF
    if((m, n) in mem):
        return mem[(m, n)]
    else:
        ans = INF
        if(m != X - 1):
            ans = maxGanancia(m + 1, n, lista, X, mem)
        ans = min(ans, maxGanancia(m + 1, n + lista[m], lista, X, mem) + lista[m])
        mem[(m, n)] = ans
    return ans



def main():
    comando = stdin.readline().strip()
    N, X = map(int, comando.split())
    while(N!=0 and X!=0):
        lista=[]
        respuesta=0
        for i in range(N):
            porcentaje = float(stdin.readline().strip())
            lista.append(porcentaje*100)
        if(lista[X-1]>=5000):
            respuesta=100.00
        else:
            respuesta = lista[X - 1] / maxGanancia(0,0,lista, X,{}) * 100.0
        print("{:.2f}".format(respuesta))
        comando = stdin.readline().strip()
        N, X = map(int, comando.split())
main()