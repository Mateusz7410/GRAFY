import nastepniki
import krawedzi
import generowanie
import macierz
import time
import sys
sys.setrecursionlimit(1000000000)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def DFS_s(n, odw, tab, v1):
    if odw[v1] == False:
        odw[v1] = True
        for i in range(n):
            if tab[v1][i] == 1 and odw[i] == False:
                DFS_s(n, odw, tab, i)
    print(v1)


def DFS_sasiedztwa(n, tab, start):
    v1 = start
    odwiedzone = [False] * n
    while False in odwiedzone:
        DFS_s(n, odwiedzone, tab, v1)
        if False in odwiedzone:
            v1 = odwiedzone.index(False)

def DFS_n(n, odw, nast, v1):
    if odw[v1] == False:
        odw[v1] = True
        for i in nast[v1]:
            if  odw[i] == False:
                DFS_n(n, odw, nast, i)
    print(v1)

def DFS_nastepniki(n, nast, start):
    v1 = start
    odwiedzone = [False] * n
    while False in odwiedzone:
        DFS_n(n, odwiedzone, nast, v1)
        if False in odwiedzone:
            v1 = odwiedzone.index(False)

def DFS_k(n, odw, kraw, v1):
    if odw[v1] == False:
        odw[v1] = True
        for i in range(len(kraw)):
            if kraw[i][0] == v1 and odw[kraw[i][1]] == False:
                DFS_k(n, odw, kraw, kraw[i][1])
    print(v1)



def DFS_krawedzie(n, kraw, start):
    v1 = start
    odwiedzone = [False] * n
    while False in odwiedzone:
        DFS_k(n, odwiedzone, kraw, v1)
        if False in odwiedzone:
            v1 = odwiedzone.index(False)





if __name__ == "__main__":
    '''#tab = [[0,1,0,0,1,0,0,0], [0,0,0,0,0,0,1,0], [0,0,0,0,1,1,0,0], [0,0,0,0,0,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0]]
    fp = open("dfs2.csv", "r")
    tab = []
    n = 14
    generowanie.generate(n, tab)
    start = time.time()
    DFS_sasiedztwa(len(tab), tab, 0)
    print(time.time()-start)
    nast = []
    start = time.time()
    nastepniki.nastepniki(len(tab), tab, nast)
    DFS_nastepniki(len(nast), nast,0)
    print(time.time()-start)
    start = time.time()
    kraw = []
    krawedzi.krawedzi(len(tab), tab, kraw)
    DFS_krawedzie(n, kraw, 0)
    print(time.time() - start)'''
    print("DFS \n\n\n")
    plik = open("dfs2_bezgenerowania.csv", "w")
    for i in range(200, 3001, 200):
        n = i
        start = time.time()
        tab = []
        generowanie.generate(n, tab)
        wynik = time.time() - start
        plik.write("Generowanie;{};{}\n".format(i, wynik))
        dfs = []
        start = time.time()
        DFS_sasiedztwa(n, tab, 0)
        wynik = time.time() - start
        plik.write("dfs_sasiedztwa;{};{}\n".format(i, wynik))
        print(dfs)
        dfs = []
        nast = []
        nastepniki.nastepniki(n, tab, nast)
        start = time.time()
        DFS_nastepniki(n, nast, 0)
        wynik = time.time() - start
        plik.write("dfs_nastepniki;{};{}\n".format(i, wynik))
        print(dfs)
        dfs = []
        kraw = []
        krawedzi.krawedzi(n, tab, kraw)
        start = time.time()
        DFS_krawedzie(n, kraw, 0)
        wynik = time.time() - start
        plik.write("dfs_krawedzie;{};{}\n".format(i, wynik))
        print(dfs)
    plik.close()