from sys import stdin

def FryTabulacionOptimizada(T, E):
    N,SE = len(T),sum(E)
    tab_size = SE * 2 + 1
    tab = [[0 for _ in range(tab_size)] for _ in range(2)]
    n,e,curr,prev = N-1,0,0,1
    while(n!=-1):
        if(e==SE+1):
            n,e,curr,prev = n-1,0,1-curr,1-prev
        else:
            if(e==0):
                tab[curr][e] = T[n]+tab[prev][e+E[n]]
            else:
                tab[curr][e] = min(T[n]+tab[prev][e+E[n]],
                                (T[n]>>1)+tab[prev][e+E[n]-1])
            e += 1
    return tab[prev][0]


def main():
    cantViajes = int(stdin.readline())
    while(cantViajes!=0):
        T,M=[],[]
        for i in range(cantViajes):
            comando=stdin.readline().strip()
            comando=comando.split()
            T.append(int(comando[0]))
            M.append(int(comando[1]))
        print(FryTabulacionOptimizada(T,M))
        cantViajes=int(stdin.readline())
        

main()