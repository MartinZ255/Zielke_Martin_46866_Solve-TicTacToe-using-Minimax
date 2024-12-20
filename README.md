# Solve Tic Tac Toe using Minimax

##### Das Spielbrett (board) wird hier als 2D-Liste implementiert mit '_' als Standartwerte gefüllt welche ein leeres 3x3 Feld repräsentiert. Dieses wird fortlaufend während des Spieles verwendet und verändert.

Für die Implementierung der Minimax Funktion werden zusätzlich einige Methoden benötigt:

1. spielZuende(board): bool
   ##### Diese Methode nimmt ein board an und prüft dann, ob es noch mögliche Züge gibt oder ob ein Spieler gewonnen hat. In dem Fall wäre ein Terminal State erreicht und es wird zurückgegeben, ob das Spiel vorbei ist (True) oder nicht (False).
   ##### ![spielZuende](https://github.com/user-attachments/assets/2c17a129-b233-439b-9038-c35caa968d93)
#

2. bewerteStellung(board): -1, 0 oder 1
   ##### Diese Methode ist sehr ähnlich wie die Methode spielZuende(board) aufgebaut. Der Unterschied liegt nur darin, dass hier der konkrete Gewinner ermittelt wird. Hier wird aus diesem Grund auch nicht überprüft, ob die Felder belegt sind oder nicht, sondern nur, ob die Gewinnbedingungen erfüllt sind. Als Rückgabewert erhält man eine -1 (Kreis gewinnt), 0 (Unentschieden) oder eine 1 (Kreuz gewinnt).  
#

3. werIstDran(board): String 'x' oder 'o'
   ##### Die Methode nimmt ein Board und zählt die Kreuze und Kreise durch. Wenn es gleich viele Kreise wie Kreuze gibt, ist Kreuz dran. Wenn es ein Kreuz mehr gibt, ist Kreis dran. Der Rückgabewert ist entweder ein 'x' oder ein 'o'. 
   #### ![werIstDran](https://github.com/user-attachments/assets/10e7520f-0798-4563-93fe-7a656d4eace6)


#

4. moeglicheZuege(board): zug[]
   ##### Die Methode geht jedes Feld von board durch und prüft, ob es leer ist. Im Falle eines leeren Feldes wird es einer Liste angefügt. Dies wird für jedes Feld wiederholt. Im Anschluss wird dann die gesamte Liste zurückgegeben.
   #### ![moeglicheZuege](https://github.com/user-attachments/assets/48b9d8e3-201d-4783-9829-0b50ef2bad5c)


#
   
5. zukunftsBoard(board,zug): board[][]
   ##### Diese Methode nimmt ein board und erweitert diesen um einen Zug. Dafür wird zuerst eine Kopie des aktuellen Spielfeldes angelegt. Die werIstDran(board) Methode wird dann verwendet, um den aktuellen Spieler zu ermitteln. Anschließend wird der Zug ausgelesen und gespielt. Die Kopie des Spielfeldes wird dann zurückgegeben.  
   #### ![zukunftsBoard](https://github.com/user-attachments/assets/cf035b7c-dc12-4e0e-921d-d2385e19f738)
#

## minimax(board): -1, 0 oder 1
##### Der Algorhitmus minimax(board) zur Bestimmung des Besten Zuges in einer beliebigen Stellung dann folgendermaßen aus:
#### ![minimax](https://github.com/user-attachments/assets/004a8812-d603-41cd-819f-de1e488529d1)

#

## Fragen:
#
#




#### Wie wird ein Node modelliert, wie sieht die State-Evaluationsfunktion aus?
#
###### Die Nodemodellierung findet hier nur explizit durch die States statt. Dabei wird nicht gespeichert, welche Züge in welcher Reihenfolge gespielt wurden.
###### Stattdessen gibt es das aktuelle Board, welches als State angesehen werden kann. 
###### Für die State-Evaluationsfunktion habe ich die Methode bewerteStellung(board) implementiert:
- Die Methode wird nur aufgerufen, sofern ein Terminal State erreicht wurde bzw sofern das Spiel zuende ist
- Das Board (Aktueller State) wird übergeben
- Der Sieger wird ermittelt und abhängig davon wird entweder -1 (Kreis gewinnt), 0 (unentschieden) oder 1 (Kreuz gewinnt) zurückgegeben.

#
#
#
#




#### Ist ein Minimax noch optimal, wenn ein Gegenspieler nicht optimal spielt?
#
###### Selbst wenn der Gegenspieler nicht optimal spielt, ist der Minimax an sich immernoch optimal. In anderen Worten wählt der Minimax-Algorithmus immer den für sich sichersten Weg, um zu gewinnen, ohne Risiken einzugehen. Dabei wird jedoch nicht beachtet, dass durch einen suboptimalen Zug des Gegenspielers, der Algorithmus eventuell eine sofortige Gewinnchance übersieht und stattdessen einen längeren Weg zum Sieg wählt.
###### Das bedeutet, dass der Minimax den ersten sicheren Weg priorisiert, den er findet, um zu gewinnen, anstelle von dem schnellsten zielführenden Zug.
###### Dies liegt daran, dass der Algorithmus eine Tiefensuche von jedem Zug bis zum Terminal-State nacheinander durchführt. Dabei bewertet er Zustände anhand des sichersten Weges und sucht nicht explizit nach dem kürzesten Weg. Eine alternative Herangehensweise, wie etwa eine Breitensuche, könnte helfen, den schnellsten und sichersten Weg zu finden.
#
#
#
#
#### Wie müsste man den Minimax anpassen, wenn es mehr als 2 Spieler gibt?
#
###### Der aktuelle Minimax-Algorithmus basiert darauf, dass es nur zwei Spieler gibt: einen maximierenden und einen minimierenden Spieler. Für Spiele mit mehr als zwei Spielern (z. B. 3 Spieler) ist dieses Prinzip nicht direkt anwendbar, da es keine klaren Gegenspielerrollen mehr gibt. Statt einer einzelnen Bewertung des Spielfelds müsste es daher eine separate Bewertung für jeden Spieler geben.
###### Die Evaluationsfunktion müsste so angepasst werden, dass sie bei n Spielern die Gewinnchancen jedes einzelnen Spielers unabhängig voneinander bewertet. Der eigene Wert würde maximiert, während die Werte der Gegner minimiert werden, um deren Gewinnchancen zu blockieren. Dies erfordert, dass die Evaluationsfunktion bei n Spielern auch n Bewertungen gleichzeitig liefert.
###### Ein Problem bei der Anwendung des typischen Minimax wäre jedoch, dass Gegenspieler möglicherweise nicht immer optimale Züge machen, um ihre eigene Gewinnchance zu maximieren. Stattdessen könnten sie suboptimale Züge spielen, um einen stärkeren Spieler zu blockieren, selbst wenn dies auf Kosten ihrer eigenen Siegchancen geht. Dies würde zusätzliche Anpassungen am Algorithmus erfordern. Eine Möglichkeit wäre die Implementierung einer Breitensuche, um Blockaden zu ermitteln.
#
#
#
#
#
##### Quellen:
###### Folienskript aus der Vorlesung AI
###### Spanning Tree, Minimax: How Computers Play Games, 2023, 5:13-8:42 https://www.youtube.com/watch?v=SLgZhpDsrfc
