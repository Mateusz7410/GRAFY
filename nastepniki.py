import generowanie

def nastepniki(n,tab,nast):
    for i in range(n):
        pom = []
        for j in range(n):
            if tab[i][j]==1:
                pom.append(j)
        nast.append(pom)

if __name__ == "__main__":
    n=10
    tab=[]
    generowanie.generate(n,tab)
    nast=[]
    nastepniki(n,tab,nast)
    print(nast)