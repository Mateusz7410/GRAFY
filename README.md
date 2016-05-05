Zadanie trzecie (Algorytmy grafowe)

Termin zaliczenia zadania + wykres - ; sprawozdanie mailem z wykresami (pdf)- 
Wygeneruj sp�jny skierowany graf acykliczny o n wierzcho�kach
- wsp�czynnik nasycenia �ukami w grafie powinien by� r�wny 50% (czyli 50% z n(n-1)/2)
- naj�atwiej jest utworzy� graf acykliczny skierowany poprzez wype�nienie odpowiedni� liczb� jedynek g�rnego tr�jk�ta macierzy s�siedztwa
Graf jest reprezentowany poprzez macierz s�siedztwa, list� nast�pnik�w oraz tabel� kraw�dzi. Dla ch�tnych r�wnie� macierz grafu.
Zaimplementuj dwa algorytmy sortowania topologicznego dla ka�dej z reprezentacji zgodnie z algorytmem przeszukiwania:
* w g��b - etykietowanie wierzcho�k�w pre- i postorder 
* wszerz - wyszukiwanie wierzcho�k�w bez kraw�dzi wej�ciowych, usuwanie ich nast�pnik�w, powtarzanie iteracji
- dokonaj pomiaru czasu dzia�ania algorytm�w dla ka�dej reprezentacji grafu 
- og�lne idee algorytm�w, maj� by� takie same dla r�nych reprezentacji grafu, r�nice wynikaj� z innej z�o�ono�ci wyszukiwania nast�pnik�w w grafie
- nie nale�y przekszta�ca� ka�dej reprezentacji np. w liste nast�pnik�w, a nastepnie sortowa�
- nie nale�y upraszcza� algorytm�w ze wzgl�du na przygotowanie danych wej�ciowych (np. macierz s�siedztwa jest g�rnotr�jk�tna i tylko tam sprawdzamy czy s� �uki)
Pomiary czasu przedstaw na wykresie t=f(n), dla 10 r�nych warto�ci n
W sprawozdaniu, opr�cz wykres�w:
- dla ka�dej z badanych reprezentacji grafu podaj z�o�ono��: pami�ciow�, znalezienia pojedynczej kraw�dzi oraz znalezienia wszystkich nast�pnik�w wierzcho�ka
- oszacuj z�o�ono�� obliczeniow� algorytm�w sortowania topologicznego (jak si� zmienia w zale�no�ci od reprezentacji grafu i z czego to wynika)
- kt�re grafy mo�na sortowa� topologiczne?