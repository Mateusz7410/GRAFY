import generowanie

def nastepniki(n,tab,nast):
    for i in range(n):
        pom = []
        for j in range(n):
            if tab[i][j]==1:
                pom.append(j)
        nast.append(pom)

def poprzedniki(n,tab,pop):
    for i in range(n):
        pom = []
        for j in range(n):
            if tab[j][i] == 1:
                pom.append(j)
        pop.append(pom)

def incydencji(n,nast,pop,incy):
    for i in range(n):
        pom=[]
        for j in range(n):
            if ((j not in nast[i]) and (j not in pop[i])):
                pom.append(j)
        incy.append(pom)


def macierz(n,nast,pop,incy,macie,npb):
    for i in range(n):
        pom = []
        for j in range(n):
            pom.append(0)
        macie.append(pom)

    for i in range(n):
        pom = []
        for j in range(3):
            pom.append(0)
        npb.append(pom)

    for i in range(n):
        if len(nast[i])==0:
            npb[i][0] = -1
        elif len(nast[i])==1:
            npb[i][0]=nast[i][0]
            macie[i][nast[i][0]]=nast[i][0]
        elif len(nast[i])!=0:
            npb[i][0]=nast[i][0]
            for j in range(len(nast[i])-1):
                macie[i][nast[i][j]]=nast[i][j+1]
            macie[i][nast[i][j+1]] = nast[i][j+1]

        if len(pop[i]) == 0:
            npb[i][1] = -1
        elif len(pop[i]) == 1:
            npb[i][1] = pop[i][0]
            macie[i][pop[i][0]] = pop[i][0]*(-1)
        elif len(pop[i]) != 0:
            npb[i][1] = pop[i][0]
            for j in range(len(pop[i]) - 1):
                macie[i][pop[i][j]] = pop[i][j + 1]*(-1)
            macie[i][pop[i][j + 1]] = pop[i][j + 1]*(-1)

        if len(incy)==0:
            npb[i][2]= -1
        if len(incy[i]) == 1:
            npb[i][2] = incy[i][0]
            macie[i][incy[i][0]] = incy[i][0]+n
        elif len(incy[i]) != 0:
            npb[i][2] = incy[i][0]
            for j in range(len(incy[i]) - 1):
                macie[i][incy[i][j]] = incy[i][j + 1]+n
            macie[i][incy[i][j + 1]] = incy[i][j + 1]+n



if __name__ == "__main__":
    n=5
    tab=[]
    generowanie.generate(n,tab)
    print(tab)

    nast = []
    nastepniki(n, tab, nast)
    print(nast)

    pop=[]
    poprzedniki(n,tab,pop)
    print(pop)

    incy=[]
    incydencji(n,nast,pop,incy)
    print(incy)

    macie=[]
    npb=[]

    macierz(n,nast,pop,incy,macie,npb)
    print(macie)
    print(npb)

