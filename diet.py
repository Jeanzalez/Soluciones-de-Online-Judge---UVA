from sys import stdin

A=[]

def DietMemo(n, x,mem):
    ans = None
    if (n, x) in mem: ans = mem[(n, x)]
    else:
        if(x == 0): ans = 0
        elif(x <= 0): ans = x
        elif(n == 0): ans = -float('inf')
        else: ans = max(DietMemo(n-1, x, mem), DietMemo(n - 1, x - A[n - 1],mem))
        mem[(n, x)] = ans
    return ans


def main():
    global A, mem
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        cantMinCalorias = int(stdin.readline().rstrip())
        CantCursos = int(stdin.readline().rstrip())
        mem={}
        A = list(map(int, stdin.readline().rstrip().split()))
        if(sum(A)<cantMinCalorias):
            RespuestaFinal = "NO SOLUTION"
        else:
            respuesta = DietMemo(len(A),cantMinCalorias,{})
            respuesta = respuesta * -1
            RespuestaFinal= cantMinCalorias+respuesta
        print(RespuestaFinal)
        cantCasos-=1

main()