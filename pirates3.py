from sys import stdin

tree = []
marcados = []


def build (a, v, l, r):
    global tree, marcados
    if(l == r): tree[v] = a[l]
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1 , l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = 2

def query_pos(v, l, r, pos):
    ans = None
    if l == r: ans = tree[v]
    else:
        m = l + ((r - l) >> 1)
        push(v, v + 1, v + 2 * (m - l + 1))
        if pos <= m : 
            ans= query_pos(v + 1, l, m, pos)
        else:
            ans= query_pos(v + 2 * (m - l + 1), m + 1, r, pos)
    return ans

def update(v, L, R, l, r, h):
    if l <= r:
        if l == L and r == R: tree[v] = h; marcados[v] = True
        else:
            m = L + ((R - L) >> 1)
            push(v, v+1, v+2 * (m-L+1))
            update(v + 1, L, m, l, min(r, m), h)
            update(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h)

def push(v, v1, v2):
    if marcados[v]:
        tree[v1] = tree[v2] = tree[v]
        marcados[v1] = marcados[v2] = True
        marcados[v] = False



def main():
    global tree, marcados
    casos=int(stdin.readline().rstrip())
    contCasos=1
    while(casos!=0):
        listaNumeros = []
        linea=int(stdin.readline().rstrip())
        for i in range(linea):
            repeticiones = int(stdin.readline().rstrip())
            cadena = stdin.readline().rstrip()
            for j in range(repeticiones):
                for num in cadena:
                    listaNumeros.append(int(num))
        tree = [None for _ in range(len(listaNumeros) * 2)]
        marcados = [ False for _ in range(len(listaNumeros) * 2)]
        build(listaNumeros, 0, 0, len(listaNumeros) - 1)
        for i in range (2*len(listaNumeros)):
            print(str(tree[i]) + " ", end= ' ')
        update(0, 0, len(listaNumeros) - 1, 0, 3, 1)
        print()
        for i in range (2*len(listaNumeros)):
            print(str(tree[i]) + " ", end= ' ')
        print()
        print(listaNumeros)
        print()
        valor = query_pos(0, 0, len(listaNumeros) - 1, 0)
        valor2 = query_pos(0, 0, len(listaNumeros) - 1, 1)
        print(valor, valor2)
        print()
        for i in range (2*len(listaNumeros)):
            print(str(tree[i]) + " ", end= ' ')
        #print(f'Case {contCasos}: {Respuesta}')
        casos=casos - 1
        contCasos+=1

main()


