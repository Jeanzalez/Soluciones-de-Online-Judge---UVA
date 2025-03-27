from sys import stdin

tree = []
marcados = []


def build (a, v, l, r):
    global tree, marcados
    if(l == r): tree[v] = create_value(a[l])
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1 , l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = combine(tree[ v + 1 ], tree[ v + 2 * ( m - l + 1 )])

def query(v, L, R, l, r):
    ans = None
    if(l > r): ans = inv_value()
    elif(l==L and r==R): ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans=combine(query(v + 1, L, m, l, min(r, m)), query( v + 2 * ( m - L + 1 ), m + 1, R, max( l, m + 1), r))
    return ans


def push(v, v1, v2):
    if marcados[v]:
        tree[v1] = tree[v2] = tree[v]
        marcados[v1] = marcados[v2] = True
        marcados[v] = False

def combine(p1, p2):
    return p1 + p2

def create_value(h):
    if(h==1):return 1
    else: return 0

def inv_value(): return 0

def update(v, L, R, l, r, h):
    if l <= r:
        if l == L and r == R: tree[v] = h; marcados[v] = True
        else:
            m = L + ((R - L) >> 1)
            push(v, v+1, v+2 * (m-L+1))
            update(v + 1, L, m, l, min(r, m), h)
            update(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h)


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
        repeticionesComandos = int(stdin.readline().rstrip())
        print(f'Case {contCasos}: ')
        for i in range(repeticionesComandos):
            q=0
            linea=stdin.readline().rstrip().split()
            Letra = linea[0]
            l=int(linea[1])
            r=int(linea[2])
            if(Letra == "F"):
                update(0, 0, len(listaNumeros) - 1, l, r, 1)
            elif(Letra == "E"):
                update(0, 0, len(listaNumeros) - 1, l, r, 0)
            elif(Letra == "I"):
                pass
            elif(Letra == "S"):
                respuesta = query(0,0,len(listaNumeros)-1,l,r)
                q+=1
                print(f'Q{q}: {respuesta}')
        casos=casos - 1
        contCasos+=1

main()


