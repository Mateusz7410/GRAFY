import random
def generate(n,tab):
    for i in range(n):
        pom=[]
        for j in range(n):
            pom.append(0)
        tab.append(pom)
    tmp = int((n * (n - 1)) / 4)
    for i in range(n-1):
        tab[i][n-1]=1
        tmp-=1
    while tmp!=0:
        i=random.randint(0,n-2)
        j=random.randint(i+1,n-1)
        if tab[i][j]==0:
            tab[i][j]=1
            tmp-=1


if __name__ == "__main__":
    n=6
    tab=[]
    generate(n,tab)
    print(tab)