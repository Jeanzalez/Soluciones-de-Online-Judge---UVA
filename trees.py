from sys import stdin

def tree(n, mem):
    if n in mem: 
        ans=mem[n]
    else:
        if n<=1: 
            ans = n
        else:
            ans = tree(n - 1, mem) + tree(n - 2, mem)
        mem[n] = ans
    return ans


def main():
    rama = int(stdin.readline())
    while(rama!=0):
        print(tree(rama,{}))
        rama=int(stdin.readline())
main()
