from sys import stdin

def calculus(cadenaNueva, listaNumeros):
    stack = []
    ans = 0
    cantSuma=1
    cantResta=0
    signo="+"
    for i in range(1,len(cadenaNueva)):
        temp=[cadenaNueva[i]]
        if(cadenaNueva[i] == "("):
            if(cadenaNueva[i-1] == "+"):
                stack.append("+")
                #cantSuma+=1
            else:
                stack.append("-")
                #cantResta+=1
        elif(len(stack)>=1 and stack[-1]=="+" and cadenaNueva[i] == "-"):
            cantResta+=1
        elif(len(stack)>=1 and stack[-1]=="-" and cadenaNueva[i] == "+"):
            cantResta+=1
        elif(len(stack)>=1 and stack[-1]=="+" and cadenaNueva[i] == "+"):
            cantSuma+=1
        elif(len(stack)>=1 and stack[-1]=="-" and cadenaNueva[i] == "-"):
            cantSuma+=1
            signo="+"
        elif(cadenaNueva[i] == ")"):
            stack.pop()
        elif(cadenaNueva[i] == "+" and cadenaNueva[i+1] != "("):
            cantSuma+=1
        elif(cadenaNueva[i] == "-" and cadenaNueva[i+1] != "(" ):
            cantResta+=1
        elif(cadenaNueva[i] == "x" and cadenaNueva[i-1] == "(" and  stack[-1]=="-"):
            cantResta+=1
    k=0
    while(cantResta!=0):
        numero=listaNumeros[k]
        ans += -(numero)
        k+=1
        cantResta-=1
    while(cantSuma!=0):
        numero=listaNumeros[k]
        ans += +(numero)
        k+=1
        cantSuma-=1
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