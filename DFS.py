import nastepniki
import krawedzi
import generowanie
import macierz
import time


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


def DFS_sasiedztwa(n, tab, dfs, start):
    s = Stack()
    s.push(start)
    odwiedzone = [False] * n
    while False in odwiedzone:
        while not (s.isEmpty()):
            v1 = s.peek()
            s.pop()
            if odwiedzone[v1] == False:
                odwiedzone[v1] = True
                for i in range(n):
                    if tab[v1][i] == 1 and odwiedzone[i] == False:
                        s.push(i)
                dfs.append(v1)
        if False in odwiedzone:
            s.push(odwiedzone.index(False))

def DFS_nastepniki(n, nast, dfs, start):
    s = Stack()
    s.push(start)
    odwiedzone = [False] * n
    while False in odwiedzone:
        while not (s.isEmpty()):
            v1 = s.peek()
            s.pop()
            if odwiedzone[v1] == False:
                odwiedzone[v1] = True
                for i in nast[v1]:
                    if odwiedzone[i] == False:
                        s.push(i)
                dfs.append(v1)
        if False in odwiedzone:
            s.push(odwiedzone.index(False))


def DFS_krawedzie(n, kraw, dfs, start):
    s = Stack()
    s.push(start)
    odwiedzone = [False] * n
    while False in odwiedzone:
        while not (s.isEmpty()):
            v1 = s.peek()
            s.pop()
            if odwiedzone[v1] == False:
                odwiedzone[v1] = True
                for i in range(len(kraw)-1):
                    if kraw[i][0] == v1:
                        s.push(kraw[i][1])
                dfs.append(v1)
        if False in odwiedzone:
            s.push(odwiedzone.index(False))



if __name__ == "__main__":
    print("DFS \n\n\n")
    n = 10
    tab = []
    generowanie.generate(n, tab)
    dfs = []
    DFS_sasiedztwa(n, tab, dfs, 0)
    print(dfs)
    dfs = []
    nast = []
    nastepniki.nastepniki(n, tab, nast)
    DFS_nastepniki(n, nast, dfs, 0)
    print(dfs)
    dfs = []
    kraw = []
    krawedzi.krawedzi(n,tab,kraw)
    DFS_krawedzie(n, kraw, dfs, 0)
    print(dfs)