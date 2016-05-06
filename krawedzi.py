import generowanie

def krawedzi(n,tab,kraw):
    for i in range(n):
        pom=[]
        for j in range(n):
            if tab[i][j]==1:
                pom.append(i)
                pom.append(j)
                kraw.append(pom)
            pom=[]

if __name__ == "__main__":
    n=10
    tab=[]
    generowanie.generate(n,tab)
    print(tab)
    kraw=[]
    krawedzi(n,tab,kraw)
    print(kraw)
