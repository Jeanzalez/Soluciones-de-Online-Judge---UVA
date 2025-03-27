from sys import stdin


def doors(N):
    low, hi = 1, N+1
    while(low + 1 != hi):
        mid = low + ((hi-low) >> 1)
        if(mid * mid <= N): low = mid
        else: hi = mid
    return low ** 2

def main():
    linea = int(stdin.readline().rstrip())
    while(linea!=0):
        Respuesta = doors(linea)
        print(Respuesta)    
        linea = int(stdin.readline().rstrip())
    print()
    
main()