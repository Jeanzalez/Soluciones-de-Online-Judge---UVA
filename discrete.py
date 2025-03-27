from sys import stdin

def atraparLadron(posicionInicialLadron, u, v):
    posicionInicialPolicia=(0,0)
    velocidadPolicia=(0,0)
    tiempo=0
    while(posicionInicialPolicia[0] < posicionInicialLadron[0] or posicionInicialPolicia[1] < posicionInicialLadron[1]):
        posicionInicialLadron=(posicionInicialLadron[0]+u,posicionInicialLadron[1]+v)
        xPrimaPolicia=posicionInicialPolicia[0]+velocidadPolicia[0]+1
        yPrimaPolicia=posicionInicialPolicia[1]+velocidadPolicia[1]+1
        velocidadPolicia=(xPrimaPolicia-posicionInicialPolicia[0],yPrimaPolicia-posicionInicialPolicia[1])
        posicionInicialPolicia=(xPrimaPolicia,yPrimaPolicia)
        tiempo+=1
    return(tiempo)


def main():
    comando=stdin.readline().strip()
    comando=list(map(int,comando.split()))
    while(len(comando)!=0):
        posicionInicialLadron=(comando[0],0)
        u=comando[1]
        v=comando[2]
        print(atraparLadron(posicionInicialLadron, u, v))
        comando=stdin.readline().strip()
        comando=list(map(int,comando.split()))

main()