import nastepniki
import krawedzi
import generowanie
import macierz
import time

def BFS_sasiedztwa(n,tab,bfs):
    q=[]
    for i in range(n):
        pom=True
        for j in range(n):
            if tab[j][i]==1:
                pom=False
        if pom:
            q.append(i)

    while len(q)!=0:
        pom2=q[0]
        bfs.append(q.pop(0))
        for i in range(n):
            if tab[pom2][i]==1:
                tab[pom2][i]=0
                pom=True
                for j in range(n):
                    if tab[j][i]==1:
                        pom=False
                if pom:
                    q.append(i)

def BFS_nastepniki(n,nast,bfs):
    q = []
    for i in range(n):
        q.append(i)
    for i in range(n):
        for j in range(len(nast[i])):
            if nast[i][j] in q:
                q.remove(nast[i][j])

    while len(q) != 0:
        pom2 = q[0]
        bfs.append(q.pop(0))
        for i in range(len(nast[pom2])):
            pom=nast[pom2][i]
            nast[pom2][i]=-1
            k=True
            for j in range(n):
                if pom in nast[j]:
                    k=False
                    break
            if k:
                q.append(pom)

def BFS_krawedzi(n,kraw,bfs):
    q = []
    for i in range(n):
        q.append(i)
    for i in range(len(kraw)):
        if kraw[i][1] in q:
            q.remove(kraw[i][1])

    while len(q) != 0:
        pom2 = q[0]
        bfs.append(q.pop(0))
        for i in range(len(kraw)):
            if kraw[i][0]==pom2:
                pom=kraw[i][1]
                kraw[i][0]=kraw[i][1]=-1
                k=True
                for j in range(len(kraw)):
                    if pom==kraw[j][1]:
                        k=False
                        break
                if k:
                    q.append(pom)




if __name__ == "__main__":
    n=100
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
    print(nast)
    start = time.clock()
    BFS_nastepniki(n,nast,bfs)
    stop = time.clock()
    print(stop - start)
    print(bfs)'''

    bfs=[]
    kraw=[]
    krawedzi.krawedzi(n,tab,kraw)
    start = time.clock()
    BFS_krawedzi(n,kraw,bfs)
    stop = time.clock()
    print(stop - start)
    print(bfs)

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