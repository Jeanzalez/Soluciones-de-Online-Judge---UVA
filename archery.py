from sys import stdin

resultado=[]

def backtracking(n, N, S, lista):
    suma=sum(resultado) + lista[n]
    if(suma < S):
        resultado.append(lista[n])
        backtracking(n, N, S, lista)
    elif(suma != S and n<N-1):
        resultado.pop()
        backtracking(n+1,N,S,lista)
    elif(suma != S and n>=N-1):
        resultado.pop()
        backtracking(n+1,N,S,lista)



def main():
    contCases=0
    numCase = int(stdin.readline())
    while(numCase!=contCases):
        contCases+=1
        comando = stdin.readline().strip().split()
        N,S=int(comando[0]),int(comando[1])
        lista=[]
        lista2=[]
        flechas = stdin.readline().strip().split()
        for i in range(N):
            lista.append(int(flechas[i]))
        j = len(lista) - 1
        while j >= 0:
            lista2.append(lista[j])
            j -= 1
        backtracking(0,N,S,lista2)
        print(resultado)

main()