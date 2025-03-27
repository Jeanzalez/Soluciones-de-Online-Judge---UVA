# Jean Paul Gonzalez Pedraza
#codigo: 8954011

from sys import stdin

def BestCoallitions(n, x, A, mem):
    ans = None
    if (n, x) in mem: 
        ans = float(mem[(n, x)])
    else:
        if(x > 5000): 
            ans =  float((A[-1]/x)* 100)
        elif(n == -1):
            ans = 0
        elif(n != -1): 
            ans = max(BestCoallitions(n-1, x, A, mem),
                      BestCoallitions(n-1, x + A[n], A, mem))
        mem[(n, x)] = float(ans)
    return ans

def main():
    n, x = list(map(int, stdin.readline().rstrip().split()))
    while(n != 0 and x!=0):
        A=[]
        mem={}
        for i in range(n):
            linea = float(stdin.readline().rstrip())
            A.append(linea * 100)
        A[-1], A[x-1] = A[x-1], A[-1]
        respuesta = float(BestCoallitions(len(A)-2, A[-1], A, mem))
        print("%.2f" % respuesta)
        n, x = list(map(int, stdin.readline().rstrip().split()))
main()