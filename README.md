# Solve Tic Tac Toe
#### using Minimax

Für die Imlementierung der Minimax Funktion werden einige Methoden benötigt:

 -WIP-
1. 
2.
...
###### So sieht der Algorhitmus zur Bestimmung des Besten Zuges in einer Beliebigen Stellung dann folgendermaßen aus:
// Bild folgt
#
-WIP-


## Fragen:
#
#




#### Wie wird ein Node modelliert, wie sieht die State-Evaluationsfunktion aus?
#
###### Die Nodemodellierung findet hier nur explizit durch die States statt. Dabei wird nicht gespeichert Welche Züge in welcher Reihenfolge gespielt wurden.
###### Stattdessen Gibt es das Aktuelle Board welches als State angesehen werden kann. 
###### Für die State-Evaluationsfunktion habe ich die Methode bewerteStellung(board) implementiert:
- Die Methode wird nur aufgerufen sofern ein Terminal State erreicht wurde bzw sofern das Spiel zuende ist
- Das Board (Aktueller State) wird übergeben
- Der Sieger wird ermittelt und abhängig davon wird entweder -1 (Kreis gewinnt), 0 (unentschieden) oder 1 (Kreuz gewinnt) zurückgegeben.

#
#
#
#




#### Ist ein Minimax noch optimal, wenn ein Gegenspieler nicht optimal spielt?
#
###### Selbst wenn der Gegenspieler nicht optimal spielt ist der Minimax an sich immernoch optimal. In anderen Worten wählt der Minimax-Algorithmus immer den für sich sichersten Weg um zu Gewinnen ohne Risiken einzugehen. Dabei wird jedoch nicht beachtet, dass durch einen Suboptimalen Zug des Gegenspielers, der Algorithmus eventuell eine Sofortige Gewinnchance übersieht und stattdessen einen Längeren Weg zum Sieg wählt.
###### Das bedeutet, dass der Minimax den ersten sicheren Weg priorisiert, den er findet um zu gewinnen, anstelle von dem schnellsten Zielführenden Zug.
###### Dies liegt daran, dass der Algorithmus eine Tiefensuche von jedem Zug bis zum Terminal-State nacheinander durchführt. Dabei bewertet er Zustände anhand des Sichersten Weges und sucht nicht explizit nach dem kürzesten Weg. Eine alternative Herangehensweise, wie etwa eine Breitensuche, könnte helfen, den schnellsten und sichersten Weg zu finden.
#
#
#
#
#### Wie müsste man den Minimax anpassen, wenn es mehr als 2 Spieler gibt?
#
###### Der aktuelle Minimax-Algorithmus basiert darauf, dass es nur zwei Spieler gibt: einen Maximierenden und einen Minimierenden Spieler. Für Spiele mit mehr als zwei Spielern (z. B. 3 Spieler) ist dieses Prinzip nicht direkt anwendbar, da es keine klaren Gegenspielerrollen mehr gibt. Statt einer einzelnen Bewertung des Spielfelds müsste es daher eine separate Bewertung für jeden Spieler geben.
###### Die Evaluationsfunktion müsste so angepasst werden, dass sie bei n Spielern die Gewinnchancen jedes einzelnen Spielers unabhängig voneinander bewertet. Der eigene Wert würde maximiert, während die Werte der Gegner minimiert werden, um deren Gewinnchancen zu blockieren. Dies erfordert, dass die Evaluationsfunktion bei n Spielern auch n Bewertungen gleichzeitig liefert.
###### Ein Problem bei der Anwendung des typischen Minimax wäre jedoch, dass Gegenspieler möglicherweise nicht immer optimale Züge machen, um ihre eigene Gewinnchance zu maximieren. Stattdessen könnten sie suboptimale Züge spielen, um einen stärkeren Spieler zu blockieren, selbst wenn dies auf Kosten ihrer eigenen Siegchancen geht. Dies würde zusätzliche Anpassungen am Algorithmus erfordern. Eine möglichkeit wäre die Implementierung einer Breitensuche um Blockaden zu ermitteln.
#
#
#
#
#
#
