from sys import stdin

Matriz=[]
mem={}

def TowardsMemo(n, x, mem):
    ans = None
    if (n, x) in mem:
        ans = abs(mem[(n, x)])
    else:
        if n == (camino-1):
            ans = Matriz[n][x]
        else:
            if(n>=N):
                move_down = TowardsMemo(n + 1, x, mem) + Matriz[n][x]
                move_right = TowardsMemo(n + 1, x + 1, mem) + Matriz[n][x]
                ans = min(abs(move_down), abs(move_right))
            else:
                if x!=0: 
                    move_down = TowardsMemo(n + 1, x - 1, mem) + Matriz[n][x]
                if x!=n: 
                    move_right = TowardsMemo(n + 1, x, mem) + Matriz[n][x]
                ans = min(abs(move_down), abs(move_right))
        mem[(n, x)] = ans
    return ans

def main():
    global Matriz, mem, camino, N
    N = int(stdin.readline().rstrip())
    while(N!=0):
        Matriz=[]
        camino=(2*N)-1
        for i in range(camino):
            Linea = list(map(int, stdin.readline().rstrip().split()))
            Matriz.append(Linea)
        Resultado = TowardsMemo(0,0,{}) 
        print(Resultado)
        N = int(stdin.readline().rstrip())

main()