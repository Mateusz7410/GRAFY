Zadanie trzecie (Algorytmy grafowe)

Termin zaliczenia zadania + wykres - ; sprawozdanie mailem z wykresami (pdf)- 
Wygeneruj spójny skierowany graf acykliczny o n wierzcho³kach
- wspó³czynnik nasycenia ³ukami w grafie powinien byæ równy 50% (czyli 50% z n(n-1)/2)
- naj³atwiej jest utworzyæ graf acykliczny skierowany poprzez wype³nienie odpowiedni¹ liczb¹ jedynek górnego trójk¹ta macierzy s¹siedztwa
Graf jest reprezentowany poprzez macierz s¹siedztwa, listê nastêpników oraz tabelê krawêdzi. Dla chêtnych równie¿ macierz grafu.
Zaimplementuj dwa algorytmy sortowania topologicznego dla ka¿dej z reprezentacji zgodnie z algorytmem przeszukiwania:
* w g³¹b - etykietowanie wierzcho³ków pre- i postorder 
* wszerz - wyszukiwanie wierzcho³ków bez krawêdzi wejœciowych, usuwanie ich nastêpników, powtarzanie iteracji
- dokonaj pomiaru czasu dzia³ania algorytmów dla ka¿dej reprezentacji grafu 
- ogólne idee algorytmów, maj¹ byæ takie same dla ró¿nych reprezentacji grafu, ró¿nice wynikaj¹ z innej z³o¿onoœci wyszukiwania nastêpników w grafie
- nie nale¿y przekszta³caæ ka¿dej reprezentacji np. w liste nastêpników, a nastepnie sortowaæ
- nie nale¿y upraszczaæ algorytmów ze wzglêdu na przygotowanie danych wejœciowych (np. macierz s¹siedztwa jest górnotrójk¹tna i tylko tam sprawdzamy czy s¹ ³uki)
Pomiary czasu przedstaw na wykresie t=f(n), dla 10 ró¿nych wartoœci n
W sprawozdaniu, oprócz wykresów:
- dla ka¿dej z badanych reprezentacji grafu podaj z³o¿onoœæ: pamiêciow¹, znalezienia pojedynczej krawêdzi oraz znalezienia wszystkich nastêpników wierzcho³ka
- oszacuj z³o¿onoœæ obliczeniow¹ algorytmów sortowania topologicznego (jak siê zmienia w zale¿noœci od reprezentacji grafu i z czego to wynika)
- które grafy mo¿na sortowaæ topologiczne?