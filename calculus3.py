from sys import stdin

def calculus(cadenaNueva, listaNumeros):
    stack = []
    ans = 0
    cantSuma=1
    cantResta=0
    signo="+"
    for i in range(1,len(cadenaNueva)):
        IteradorCaracteres = cadenaNueva[i]
        if IteradorCaracteres == "x" and signo == "-":
            cantResta += 1
        elif IteradorCaracteres == "x" and signo == "+":
            cantSuma += 1
        elif IteradorCaracteres == "(":
            stack.append(signo)
        elif IteradorCaracteres == ")":
            signo = stack.pop()
        elif IteradorCaracteres == "+":
            if len(stack) != 0 and stack[-1] == "-":
                signo = "-"
            else:
                signo = "+"
        elif IteradorCaracteres == "-":
            if len(stack) == 0 or stack[-1] != "-":
                signo = "-"
            else:
                signo = "+"
    k = 0
    while cantResta != 0:
        if k >= len(listaNumeros):
            break
        numero = listaNumeros[k]
        ans -= numero
        k += 1
        cantResta -= 1
    while cantSuma != 0:
        if k >= len(listaNumeros):
            break
        numero = listaNumeros[k]
        ans += numero
        k += 1
        cantSuma -= 1
    return ans

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        cadena = stdin.readline().rstrip()
        cadenaNueva = ["+"]
        for i in range(len(cadena)):
            cadenaNueva.append(cadena[i])
        cantNumeros = int(stdin.readline().rstrip())
        listaNumeros = list(map(int, stdin.readline().rstrip().split()))
        listaNumeros.sort()
        respuesta = calculus(cadenaNueva, listaNumeros)
        print(respuesta)
        caso += 1
        cantCasos-=1
main()