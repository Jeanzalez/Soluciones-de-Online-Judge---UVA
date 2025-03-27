from sys import stdin


def binarySearch(list,low,hi,B):
    while(low < hi):
        acu=0
        mid = (low + hi) // 2
        for i in range(len(list)):
            acu+=((list[i]+mid -1)//mid)
        if(acu<=B):
            hi = mid
        else:
            low = mid + 1
    ans=low
    return ans

def main():
    comando = stdin.readline().strip()
    N, B = map(int, comando.split())
    while(N!=-1 and B!=-1):
        list=[]
        poblacion=stdin.readline().strip()
        while(poblacion!=""):
            list.append(int(poblacion))
            poblacion=stdin.readline().strip()
        Respuesta=binarySearch(list,1,sum(list),B)
        print(Respuesta)
        comando = stdin.readline().strip()
        N, B = map(int, comando.split())
          
main()