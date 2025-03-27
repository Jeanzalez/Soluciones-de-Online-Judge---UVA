from sys import stdin

def phi(Di,T1,T2,H,n,x,mem):
    ans = None
    if((n,x) in mem):
        ans=mem[(n,x)]
    else:
        if(n==len(H)-1 and x==-1):
            ans=T1
        elif(n==len(H)-1):
            ans=0
        elif(x!=-1):
            ans=phi(Di,T1,T2,H,n+1,max(x-Di[n],-1),mem)
        else:
            ans=min(phi(Di,T1,T2,H,n+1,max(T1-Di[n],-1),mem) + T1, phi(Di,T1,T2,H,n+1,max(T2-Di[n],-1),mem) + T2)
        mem[(n,x)]=ans    
    return ans


def main():
    comando=stdin.readline()
    comando = comando.split()
    comando=list(map(int, comando))
    while(len(comando)!=0):
        N=comando[0]
        C=comando[1]
        T1=comando[2]
        T2=comando[3]
        huecos=stdin.readline()
        huecos = huecos.split()
        huecos = list(map(int, huecos))
        distancias=[]
        for i in range(N-1):
            distancias.append(huecos[i+1]-huecos[i])
        listaRespuestas=[]
        listaRespuestas.append(phi(distancias,min(T1,T2),max(T1,T2),huecos,0,-1,{}))
        shift=0
        i=-1
        posicion=huecos[-1]
        inicial=huecos[0]
        while(C-posicion+inicial<=max(T1,T2) and shift+1!=len(huecos)):
            i=i-1
            posicion=huecos[i]
            shift+=1
        listacopy=huecos
        while(shift!=0):
            inicial=C-listacopy[-1]
            listacopy.pop()
            for i in range(len(listacopy)):
                listacopy[i]+=inicial
            listacopy.insert(0,0)
            dis=[]
            for i in range(N-1):
                dis.append(listacopy[i+1]-listacopy[i])
            listaRespuestas.append(phi(dis,min(T1,T2),max(T1,T2),listacopy,0,-1,{}))
            shift-=1
        print(min(listaRespuestas))
        comando=stdin.readline()
        comando = comando.split()
        comando=list(map(int, comando))
        


main()