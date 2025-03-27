from sys import stdin


def main():
    comando=stdin.readline()
    comando = comando.split()
    comando=list(map(int, comando))
    L=comando[0]
    G=comando[1]
    while(L!=0 and G!=0):
        listaTuplas=[]
        for i in range(G):
            comando=stdin.readline()
            comando = comando.split()
            comando=list(map(int, comando))
            listaTuplas.append((comando[0],comando[1]))
        UltimaCubierta=0
        cont=0
        for x in range(len(listaTuplas)):
            tuplaActual=listaTuplas[x]
            rango=(tuplaActual[0]-tuplaActual[1],tuplaActual[0]+tuplaActual[1])
            if(rango[1]>UltimaCubierta):
                UltimaCubierta=rango[1]
            else:
                cont+=1
        if(UltimaCubierta>=L):
            print(cont)
        else:
            print(-1)
        comando=stdin.readline()
        comando = comando.split()
        comando=list(map(int, comando))
        L=comando[0]
        G=comando[1]  

main()