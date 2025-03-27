from sys import stdin



def main():
    numero=stdin.readline().rstrip().split(" ")
    conjuntos = []
    for i in range(1, int(numero[0])+1):
        conjuntos.append(set([i]))
    for i in range(int(numero[1])):
        comando=stdin.readline().rstrip().split(" ")
        opcion=int(comando[0])
        if(opcion==1):
            p = int(comando[1])
            q = int(comando[2])
            conjunto_p = None
            conjunto_q = None
            for conjunto in conjuntos:
                if p in conjunto:
                    conjunto_p = conjunto
                if q in conjunto:
                    conjunto_q = conjunto
            if conjunto_p != conjunto_q:
                conjunto_p.update(conjunto_q)
                conjuntos.remove(conjunto_q)
        elif(opcion==2):
            p = int(comando[1])
            q = int(comando[2])
            for conjunto in conjuntos:
                if p in conjunto:
                    conjunto_p = conjunto
                if q in conjunto:
                    conjunto_q = conjunto
            if conjunto_p != conjunto_q:
                conjunto_p.remove(p)
                conjunto_q.add(p)
        elif(opcion == 3):
            p = int(comando[1])
            conjunto_p = None
            for conjunto in conjuntos:
                if p in conjunto:
                    conjunto_p = conjunto
            cantidad_elementos = len(conjunto_p)
            suma_elementos = sum(conjunto_p)
            print(cantidad_elementos ,suma_elementos)

main()