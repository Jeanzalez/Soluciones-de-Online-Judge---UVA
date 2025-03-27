from sys import stdin

PadreFalso = 0
dicPadres = {}


def make_set(x):
    global PadreFalso
    PadreFalso += 1
    dicPadres[x] = PadreFalso
    return {'p': PadreFalso, 'rango': 0, 'valor': x}

# Union
def union(conjuntos, p, q):
    link(find_set(conjuntos, p), find_set(conjuntos, q))

def link(p, q):
    if p['rango'] > q['rango']:
        q['p'] = p['valor']
    else:
        p['p'] = q['valor']
        if p['rango'] == q['rango']:
            q['rango'] += 1


def find_set(conjuntos, x):
    if conjuntos[x]['valor'] != conjuntos[conjuntos[x]['p']]['valor']:
        conjuntos[x]['p'] = find_set(conjuntos, conjuntos[x]['p'])['valor']
    return conjuntos[x]


def move(conjuntos, p, q):
    conjunto_p = find_set(conjuntos, p)
    conjunto_q = find_set(conjuntos, q)
    if conjunto_p['valor'] != conjunto_q['valor']:
        conjunto_p['p'] = conjunto_q['valor']

def main():
    global PadreFalso
    numero=stdin.readline().rstrip().split(" ")
    n = int(numero[0])
    conjuntos = {}
    PadreFalso=n
    for i in range(1, n+1):
        conjuntos[i] = make_set(i)
    for i in range(int(numero[1])):
        comando=stdin.readline().rstrip().split(" ")
        opcion=int(comando[0])
        p=None
        q=None
        if(opcion==1):
            p=int(comando[1])
            q=int(comando[2])
            union(conjuntos,p,q)
        elif(opcion==2):
            p=int(comando[1])
            q=int(comando[2])
            move(conjuntos,p,q)
        elif(opcion==3):
            pass
            #p=int(comando[1])
            #move(conjuntos,p,q)
    print(conjuntos)
    
main()