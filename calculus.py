from sys import stdin

def calculus(cadenaNueva, listaNumeros):
    stack = []
    ans = None
    lista_Nueva=[]
    #cantSuma=0
    #cantResta=0
    for i in range(len(cadenaNueva)):
        if(cadenaNueva[i] == "(" and cadenaNueva[i-1] == "+"):
            stack.append("+")
        elif(cadenaNueva[i] == "(" and cadenaNueva[i-1] == "-"):
            stack.append("-")
        elif(len(stack) >= 1 and stack[-1] == "-" and cadenaNueva[i] == "+"):
            lista_Nueva.append("-")
        elif(len(stack) >= 1 and stack[-1] == "-" and cadenaNueva[i] == "-"):
            lista_Nueva.append("+")
        elif(len(stack) >= 1 and stack[-1] == "+" and cadenaNueva[i] == "+"):
            lista_Nueva.append("+")
        elif(len(stack) >= 1 and stack[-1] == "+" and cadenaNueva[i] == "-"):
            lista_Nueva.append("-")
        elif(cadenaNueva[i] == ")" and len(stack) >= 1):
            stack.pop()
        elif(cadenaNueva[i] == "+"):
            stack.append("+")
        elif(cadenaNueva[i] == "-"):
            stack.append("-")
    return lista_Nueva 

def main():
    caso = 1
    cantCasos = int(stdin.readline().rstrip())
    while(cantCasos!= 0):
        cadena = stdin.readline().rstrip()
        cadenaNueva = []
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