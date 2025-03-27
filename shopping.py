from sys import stdin


def universe(N):
    return (1 << N) - 1

def is_elt(n, X):
    return (X | (1 << n)) == X

def remove_elt(n, X):
    return X - (1 << n) if is_elt(n, X) else X

def singleton(n, X):
    return X == (1 << n)


INF = float('inf')

def phi_memo(N, w, u, X, mem):
    ans,key = None,(u,X)
    if key in mem: ans = mem[key]
    else:
        if not(is_elt(u, X)): ans = INF
        elif singleton(u, X): ans = w[0][u]
        else:
            ans,Y = INF,remove_elt(u, X)
            for v in range(1, N):
                if is_elt(v, Y):
                    ans = min(ans, phi_memo(N, w, v, Y, mem)+w[v][u])
        mem[key] = ans
    return ans

def shopping(N, w):
    ans = INF
    X = remove_elt(0, universe(N))
    mem = dict()
    for u in range(1, N):
        ans = min(ans, phi_memo(N, w, u, X, mem)+w[u][0])
    return ans

def main():
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        N, M = map(int, stdin.readline().rstrip().split())
        roads = [[INF] * N for _ in range(N)]
        for i in range(N):
            roads[i][i] = 0
        for _ in range(M):
            X, Y, D = map(int, stdin.readline().rstrip().split())
            roads[X][Y] = D
            roads[Y][X] = D
        S = int(stdin.readline().rstrip())
        stores = [0] + [int(stdin.readline().rstrip()) for _ in range(S)]
        N = len(stores)
        w = [[roads[i][j] if i != j else 0 for j in stores] for i in stores]
        resultado = shopping(N, w)
        print(resultado)
        cantCasos-=1

main()
