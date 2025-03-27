from sys import stdin

def memorizacion(T,M,n,e,mem):
    ans = None
    N=len(T)
    if (n, e) in mem: 
      ans = mem[(n, e)]
    else:
        if n == N: 
          ans = 0
        else:
          if(n<N and e==0): 
            ans = memorizacion(T,M,n+1, e+M[n], mem)+T[n]
          elif(e >= (N-n)):
              ans=memorizacion( T, M, n+1, e+M[n]-1, mem) + (T[n]>>1)
          else:
              ans=min(memorizacion(T ,M ,n+1, e + M[n], mem) + T[n], 
              memorizacion( T, M, n+1, e+M[n]-1, mem) + (T[n]>>1))
        mem[(n,e)]=ans
    return ans
    

def main():
    cantViajes = int(stdin.readline())
    while(cantViajes!=0):
        T,M=[],[]
        for i in range(cantViajes):
            comando=stdin.readline().strip()
            comando=comando.split()
            T.append(int(comando[0]))
            M.append(int(comando[1]))
        print(memorizacion(T,M,0,0,{}))
        cantViajes=int(stdin.readline())
        

main()

