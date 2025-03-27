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
    if(dicPadres[v]==dicPadres[v]): ans = v
    else:
        dicPadres[v + 1] = findSet(dicPadres[v + 1])
        ans = dicPadres[v + 1]
    return ans

def unionSet(u, v):
    global dicPadres
    u, v = findSet(u), findSet(v)
    if(u!=v):
        if(rango[u - 1] < rango[v - 1]): u, v = v, u
        dicPadres[v]=dicPadres[u]
        if(rango[u - 1] == rango[v - 1]): rango[u - 1] += 1

def move(p, q):
    global dicPadres
    dicPadres[p] = dicPadres[q]

def funcionSuma(numero):
    global dicPadres
    valor = dicPadres[numero]
    ClavesIguales = []
    for k, v in dicPadres.items():
        if v == valor:
            ClavesIguales.append(k)
    SumaClaves = sum(ClavesIguales)
    return len(ClavesIguales), SumaClaves


def main():
    global p, rango, impostor
    numero=stdin.readline().rstrip().split(" ")
    while(numero and numero[0]):
        n = int(numero[0])
        impostor = n
        conjuntos = []
        p = [0  for _ in range(n)]
        rango = [0  for _ in range(n)]
        for i in range(0, n):
            makeSet(i)
            conjuntos.append(i + 1)
        for i in range(int(numero[1])):
            comando=stdin.readline().rstrip().split(" ")
            opcion=int(comando[0])
            p=None
            q=None
            if(opcion==1):
                p=int(comando[1])
                q=int(comando[2])
                unionSet(p,q)
            elif(opcion==2):
                p=int(comando[1])
                q=int(comando[2])
                move(p,q)
            elif(opcion==3):
                p=int(comando[1])
                r1, r2 = funcionSuma(p)
                print(f'{r1} {r2}')
        numero=stdin.readline().rstrip().split(" ")
    print()
    
main()