from sys import stdin

def calculo(cadenaNueva, listaNumeros):
    pila = []
    resultado = 0
    cantSuma = 1
    cantResta = 0
    signo = "+"
    for i in range(1, len(cadenaNueva)):
        if cadenaNueva[i] == 'x':
            if signo == '+':
                cantSuma += 1
            else:
                cantResta += 1
        elif cadenaNueva[i] == '(':
            pila.append(signo)
        elif cadenaNueva[i] == ')':
            signo = pila.pop()
        elif cadenaNueva[i] in '+-':
            signo = cadenaNueva[i]
            if pila and pila[-1] == '-':
                signo = '+' if signo == '-' else '-'

    k = 0
    while cantResta != 0:
        if k >= len(listaNumeros):
            break
        numero = listaNumeros[k]
        resultado -= numero
        k += 1
        cantResta -= 1
    while cantSuma != 0:
        if k >= len(listaNumeros):
            break
        numero = listaNumeros[k]
        resultado += numero
        k += 1
        cantSuma -= 1
    return resultado

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while cantCasos != 0:
        cadena = stdin.readline().rstrip()
        cadenaNueva = ["+"]
        for i in range(len(cadena)):
            cadenaNueva.append(cadena[i])
        cantNumeros = int(stdin.readline().rstrip())
        listaNumeros = list(map(int, stdin.readline().rstrip().split()))
        listaNumeros.sort()
        respuesta = calculo(cadenaNueva, listaNumeros)
        print(respuesta)
        caso += 1
        cantCasos -= 1
main()
