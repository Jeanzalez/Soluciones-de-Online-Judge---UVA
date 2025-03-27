from sys import stdin

def main():
    contCases=0
    numCase = int(stdin.readline())
    while(numCase!=contCases):
        contCases+=1
        CantJugadores=int(stdin.readline())
        dicEstampillas={}
        listaGeneral=[]
        for i in range(CantJugadores):
            estampilla=stdin.readline().strip()
            estampilla=estampilla.split()
            listaGeneral.append(0)
            for k in range(1,len(estampilla)):
                if(estampilla[k] not in dicEstampillas):
                    dicEstampillas[estampilla[k]]=set()
                    dicEstampillas[estampilla[k]].add(i)
                else:
                    dicEstampillas[estampilla[k]].add(i)
        contEstampillasUnicas=0
        for clave in dicEstampillas:
            if(len(dicEstampillas[clave])==1):
                contEstampillasUnicas+=1
                posicion=list(dicEstampillas[clave])
                listaGeneral[posicion[0]]+=1
        print("Case "+str(contCases)+":", end='')
        for k in range(len(listaGeneral)):
            resultado=float(listaGeneral[k])
            resultado=(resultado/contEstampillasUnicas)*100
            print(' {:.6f}%'.format(resultado), end='')
        print("")

main()