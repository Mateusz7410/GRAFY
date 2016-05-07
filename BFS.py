import nastepniki
import krawedzi
import generowanie
import macierz
import time

def BFS_sasiedztwa(n,tab,bfs):
    pom=[]
    for i in range(n):
        pom.append(0)
    for i in range(n):
        for j in range(n):
            if tab[j][i]==1:
                pom[i]+=1
    tmp=n
    while tmp!=0:
        for i in range(n-1,-1,-1):
            if pom[i]==0:
                pom[i]=-1
                bfs.append(i)
                tmp-=1
                for j in range(n):
                    if tab[i][j]==1:
                        pom[j]-=1

def BFS_nastepniki(n,nast,bfs):
    pom = []
    for i in range(n):
        pom.append(0)
    for i in range(n):
        for j in range(len(nast[i])):
            pom[nast[i][j]]+=1
    tmp=n
    while tmp != 0:
        for i in range(n - 1, -1, -1):
            if pom[i] == 0:
                pom[i] = -1
                bfs.append(i)
                tmp -= 1
                for j in range(len(nast[i])):
                    pom[nast[i][j]]-=1

def BFS_krawedzi(n,kraw,bfs):
    pom = []
    for i in range(n):
        pom.append(0)
    for i in range(len(kraw)):
        pom[kraw[i][1]]+=1
    tmp = n
    while tmp != 0:
        for i in range(n-1,-1,0):
            if pom[i] == 0:
                pom[i] = -1
                bfs.append(i)
                tmp -= 1
                for j in range(len(kraw)):
                    if kraw[j][0]==i:
                        pom[kraw[j][1]]-=1

def BFS_macierz(n,macie,bfs,npb):
    pom = []
    for i in range(n):
        pom.append(0)
    for i in range(n):
        if npb[i][0] != (-1):
            pom[npb[i][0]] += 1
            j = npb[i][0]
            while macie[i][j] != j:
                j = macie[i][j]
                pom[j] += 1
    #print(pom)
    print(macie)
    print(npb)
    tmp = 0
    while tmp != n:
        for i in range(n):
            if pom[i] == 0:
                pom[i] = -1
                bfs.append(i)
                tmp += 1
                if npb[i][0]!=(-1):
                    pom[npb[i][0]]-=1
                    j=npb[i][0]
                    while macie[i][j]!=j:
                        j=macie[i][j]
                        pom[j]-=1

if __name__ == "__main__":
    n=3000
    tab=[]
    generowanie.generate(n,tab)
    print(tab)

    '''bfs=[]
    start = time.clock()
    BFS_sasiedztwa(n,tab,bfs)
    stop = time.clock()
    print(stop-start)
    print(bfs)'''

    '''bfs=[]
    nast=[]
    nastepniki.nastepniki(n,tab,nast)
    start = time.clock()
    BFS_nastepniki(n,nast,bfs)
    stop = time.clock()
    print(stop - start)
    print(bfs)'''

    '''bfs=[]
    kraw=[]
    krawedzi.krawedzi(n,tab,kraw)
    start = time.clock()
    BFS_krawedzi(n,kraw,bfs)
    stop = time.clock()
    print(stop - start)
    print(bfs)'''

    nast = []
    macierz.nastepniki(n, tab, nast)
    #print(nast)

    pop = []
    macierz.poprzedniki(n, tab, pop)
    #print(pop)

    incy = []
    macierz.incydencji(n, nast, pop, incy)
    #print(incy)

    bfs = []
    macie = []
    npb = []
    macierz.macierz(n,nast,pop,incy,macie,npb)
    #print(macie)
    start = time.clock()
    BFS_macierz(n, macie, bfs,npb)
    stop = time.clock()
    print(stop - start)
    print(bfs)