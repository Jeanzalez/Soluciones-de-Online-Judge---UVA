from sys import stdin

def zapatos(cantPares,lista):
    dic={}
    for i in range(len(lista)):
        if(lista[i] in dic):
            dic[lista[i]].append(i)
        else:
            dic[lista[i]]=[]
            dic[lista[i]].append(i)
    swap=0
    for j in range(len(lista)-1):
        posicion=lista[j]
        if(lista[j]==lista[j-1] and j-1!=-1):
            pass
        elif(lista[j]!=lista[j+1]):
            pos_left,pos_right= dic[posicion][0], dic[posicion][1]
            if(pos_left!=j):
                posMover=lista[j+1]
                pos_Mover_left,pos_Mover_right= dic[posMover][0], dic[posMover][1]
                if(pos_Mover_left==j+1):
                    dic[posMover][0]=pos_left
                    lista[pos_left] = posMover
                else:
                    dic[posMover][1]=pos_right
                    lista[posMover[1]] = pos_right
                dic[posicion][0]=j+1
                lista[j+1] = lista[j]
                swap+=1
            elif(pos_right!=j+1):
                posMover=lista[j+1]
                pos_Mover_left,pos_Mover_right= dic[posMover][0], dic[posMover][1]
                if(pos_Mover_left==j+1):
                    dic[posMover][0]=pos_right
                    lista[pos_right] = posMover
                else:
                    dic[posMover][1]=pos_right
                    lista[posMover[1]] = pos_right
                dic[posicion][1]=j+1
                lista[j+1] = lista[j]
                swap+=1
    return swap



def main():
    cantCasos=0
    casos = int(stdin.readline())
    while(cantCasos!=casos):
        comando = stdin.readline().strip()
        lista=list(map(int,comando.split()))
        cantPares=lista[0]
        lista.pop(0)
        print(zapatos(cantPares,lista))
        cantCasos+=1


main()