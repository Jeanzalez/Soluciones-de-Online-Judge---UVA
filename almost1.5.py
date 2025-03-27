from sys import stdin

p, rango = [], []
conjuntos = []
impostor = 0

def makeSet(v):
    global p, rango, impostor, conjuntos
    impostor = impostor + 1
    p[v], rango[v] = impostor, 0

    
def findSet(v):
    global p, rango, impostor, conjuntos
    ans=None
    if(v == p[v - 1]): ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    global p, rango, impostor, conjuntos
    u, v = findSet(u), findSet(v)
    if(u!=v):
        if(rango[u] < rango[v]): u, v = v, u
        p[v]=u
        if(rango[u] == rango[v]): rango[u] += 1



def main():
    global p, rango, impostor, conjuntos
    numero=stdin.readline().rstrip().split(" ")
    while(numero and numero[0]):
        n = int(numero[0])
        impostor = n
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
                #move(p,q)
            elif(opcion==3):
                p=int(comando[1])
                #r1, r2 = funcionSuma(p)
                #print(f'{r1} {r2}')
        numero=stdin.readline().rstrip().split(" ")
    print()
    
main()