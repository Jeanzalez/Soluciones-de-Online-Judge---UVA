from sys import stdin

p, rango = [], []
dicPadres = {}
impostor = 0

def makeSet(v):
    global p, rango , impostor
    impostor = impostor + 1
    dicPadres[v + 1] = impostor 
    p[v], rango[v] = v + 1, 0

def findSet(v):
    global dicPadres
    ans=None
    if(v==p[v - 1]): ans = v
    else:
        p[v - 1] = findSet(p[v - 1])
        ans = p[v - 1]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if(u!=v):
        if(rango[u - 1] < rango[v - 1]): u, v = v, u
        p[v - 1]=u
        if(rango[u - 1] == rango[v - 1]): rango[u - 1] += 1



def main():
    global p, rango, impostor
    numero=stdin.readline().rstrip().split(" ")
    n = int(numero[0])
    impostor = n
    conjuntos = []
    p = [0  for _ in range(n)]
    rango = [0  for _ in range(n)]
    for i in range(0, n):
        makeSet(i)
        conjuntos.append(i + 1)
    unionSet(1, 2)
    unionSet(3, 4)
    unionSet(2, 3)
    print(p)
    print()
    print(rango)

    
main()