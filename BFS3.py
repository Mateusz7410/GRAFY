import nastepniki
import krawedzi
import generowanie
import macierz
import time

def BFS_sasiedztwa(n,tab,bfs):
    pom=[0]*n
    for i in range(n):
        for j in range(n):
            if tab[j][i]==1:
                pom[i]+=1
    q=[]
    for i in range(n):
        if pom[i]==0:
            q.append(i)
    while q:
        tmp=q[0]
        bfs.append(q.pop(0))
        for i in range(n):
            if tab[tmp][i]==1:
                pom[i]-=1
                if pom[i]==0:
                    q.append(i)


def BFS_nastepniki(n,nast,bfs):
    pom=[0]*n
    for i in range(n):
        for j in range(len(nast[i])):
            pom[nast[i][j]]+=1
    q = []
    for i in range(n):
        if pom[i] == 0:
            q.append(i)
    while q:
        tmp=q[0]
        bfs.append(q.pop(0))
        for i in range(len(nast[tmp])):
            pom[nast[tmp][i]]-=1
            if pom[nast[tmp][i]]==0:
                q.append(nast[tmp][i])

def BFS_krawedzi(n,kraw,bfs):
    pom=[0]*n
    for i in range(len(kraw)):
        pom[kraw[i][1]]+=1
    q = []
    for i in range(n):
        if pom[i] == 0:
            q.append(i)
    while q:
        tmp = q[0]
        bfs.append(q.pop(0))
        for i in range(len(kraw)):
            if kraw[i][0]==tmp:
                pom[kraw[i][1]]-=1
                if pom[kraw[i][1]]==0:
                    q.append(kraw[i][1])

def BFS_macierz(n,macie,bfs,npb):
    pom=[0]*n
    for i in range(n):
        if npb[i][1] != (-1):
            pom[i] += 1
            j = npb[i][1]
            while -macie[i][j] != j:
                j = -macie[i][j]
                pom[i] += 1
    q = []
    for i in range(n):
        if pom[i] == 0:
            q.append(i)
    while q:
        tmp = q[0]
        bfs.append(q.pop(0))
        if npb[tmp][0]!=(-1):
            j = npb[tmp][0]
            pom[j]-=1
            if pom[j]==0:
                q.append(j)
            while macie[tmp][j] != j:
                j = macie[tmp][j]
                pom[j] -= 1
                if pom[j]==0:
                    q.append(j)

if __name__ == "__main__":
    '''n=3000
    tab=[]
    generowanie.generate(n,tab)
    print(tab)'''

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

    '''nast = []
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
    print(bfs)'''

    print("BFS \n\n\n")
    plik = open("plikBFS.csv", "w")
    for i in range(200, 3001, 200):
        n = i
        tab = []
        generowanie.generate(n, tab)
        bfs = []
        start = time.time()
        BFS_sasiedztwa(n,tab,bfs)
        wynik = time.time() - start
        plik.write("bfs_sasiedztwa;{};{}\n".format(i, wynik))
        print(bfs)

        bfs = []
        nast = []
        nastepniki.nastepniki(n, tab, nast)
        start = time.time()
        BFS_nastepniki(n, nast, bfs)
        wynik = time.time() - start
        plik.write("bfs_nastepniki;{};{}\n".format(i, wynik))
        print(bfs)

        bfs = []
        kraw = []
        krawedzi.krawedzi(n, tab, kraw)
        start = time.time()
        BFS_krawedzi(n, kraw, bfs)
        wynik = time.time() - start
        plik.write("bfs_krawedzie;{};{}\n".format(i, wynik))
        print(bfs)


        nast = []
        macierz.nastepniki(n, tab, nast)

        pop = []
        macierz.poprzedniki(n, tab, pop)

        incy = []
        macierz.incydencji(n, nast, pop, incy)

        bfs = []
        macie = []
        npb = []
        macierz.macierz(n, nast, pop, incy, macie, npb)
        start = time.time()
        BFS_macierz(n, macie, bfs, npb)
        wynik = time.time() - start
        plik.write("bfs_macierz;{};{}\n".format(i, wynik))
        print(bfs)

    plik.close()