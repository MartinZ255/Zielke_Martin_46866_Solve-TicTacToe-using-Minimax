board = [['_', '_', '_'] for _ in range(3)] #Leeres 3x3 Feld ( '_' == leer, 'x' || 'o' == belegt)

#board[0] = ['o','x','o']
#board[1] = ['x','x','o']
#board[2] = ['x','o','x']

#Gibt True zurück wenn ein Spieler gewonnen hat oder keine Züge mehr gespielt werden können
#Hier wird NICHT bestimmt wer gewonne hat, sondern ob ein Spieler gewonne hat bzw das Spiel zuende ist
def spielZuende(board): 

    leeresFeldVorhanden = False #Falls einer der beiden Bool-Werte True ist, ist das Spiel Vorbei
    spielerGewinnt = False 

    if board[0][0] == board[1][1] == board[2][2]  != '_' or board[2][0] == board[1][1] == board[0][2] != '_': # Diagonaler Sieg
            spielerGewinnt = True
    for reihe in range(3): #Reihen- und Spaltensiege werden hier geprüft
        if board[reihe][0] == board[reihe][1] == board[reihe][2] != '_' or board[0][reihe] == board[1][reihe] == board[2][reihe] != '_': 
            spielerGewinnt = True
        for spalte in range(3): # Hier wird geprüft ob das Board nicht vollständig belegt ist
            if board[reihe][spalte] == '_':
                leeresFeldVorhanden = True
    if leeresFeldVorhanden == False or spielerGewinnt == True:
        return True
    return False




#gibt -1 wenn MIN('o') gewinnt, 0 wenn es unentschieden ist und 1 wenn MAX('x') gewinnt zurück
#Das heißt hier wird der Gewinner zurückgegeben.
def bewerteStellung(board): 

    minGewinnt = False
    maxGewinnt = False

    #Diagonaler Sieg für jeweils 'x' oder 'o' prüfen
    if board[0][0] == board[1][1] == board[2][2]  == 'x' or board[2][0] == board[1][1] == board[0][2] == 'x': 
        maxGewinnt = True
    if board[0][0] == board[1][1] == board[2][2]  == 'o' or board[2][0] == board[1][1] == board[0][2] == 'o':
        minGewinnt = True
    #Reihen- oder Spaltensieg für beide Spieler prüfen
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'x' or board[0][i] == board[1][i] == board[2][i] == 'x':
            maxGewinnt = True
        if board[i][0] == board[i][1] == board[i][2] == 'o' or board[0][i] == board[1][i] == board[2][i] == 'o':
            minGewinnt = True
    if minGewinnt:
        return -1
    if maxGewinnt:
        return 1
    return 0



#gibt 'x' oder 'o' zurück abhängig wer in der aktuellen Stellung dran ist.
#Das wird gemacht indem die Anzahl an Kreuzen und Kreisen gezählt werden. Wenn es gleichviele Kreuze wie Kreise gibt ist Kreuz dran.
#Alternativ gibt es einen Kreuz mehr was bedeutet, dass Kreis dran ist.
def werIstDran(board): 
    minAnzahl = 0
    maxAnzahl = 0
    for reihe in range(3):
        for spalte in range(3):
            if board[reihe][spalte] == 'x':
                maxAnzahl = maxAnzahl+1
            if board[reihe][spalte] == 'o':
                minAnzahl = minAnzahl+1
    if maxAnzahl == minAnzahl:
        return 'x'
    return 'o'



# Gibt alle möglichen züge in einer liste aus
# Jedes Feld wird durchgegangen und zu einer 2D-Liste hinzugefügt falls es leer ist.
def moeglicheZuege(board): 
    zuege = []
    for reihe in range(3):
        for spalte in range(3):
            if board[reihe][spalte] == '_':
                zuege.append([reihe,spalte])
    return zuege


#Gibt die zukünftige Stellung als 2D-Liste aus.
# Ein Board und ein Zug wird übergeben
# Das Board wird um den gegebenen Zug erweitert und wieder zurückgegeben
def zukunftsBoard(board, zug): 
    neuesBoard = [reihe[:] for reihe in board]
    if werIstDran(board) == 'x':
        neuesBoard[zug[0]][zug[1]] = 'x'
    else:
        neuesBoard[zug[0]][zug[1]] = 'o'
    return neuesBoard



#bewertet alle Züge und gibt entweder den Maximalen oder den Minimalen wert abhängig vom aktuellen Spieler aus
def minimax(board): 

    if spielZuende(board): # Falls das spiel zuende ist
        return bewerteStellung(board) # wird das Ergebnis ermittelt. Gilt hier als Rekursionsbremse

    if werIstDran(board) == 'x': #Maximierender Spieler ist dran
        wertung = -999 #Tiefster wert vordefiniert um diesen zu Maximieren
        neuewertung = -999 #Dieser wert wird für jeden Zug 
        for zug in moeglicheZuege(board): # alle möglichen Züge in einer Stellung werde durchgegangen
            neuewertung = minimax(zukunftsBoard(board,zug)) #Die Methode wird erneut (Rekursiv) aufgerufen.
            #die möglichen züge werden einzeln gespielt und übergeben. Davon wird dann die Wertung ermittelt (-1, 0 oder 1)
            if neuewertung > wertung: #Hier wird die größte Wertung geprüft(maximierung) und evtl. gespeichert.
                wertung = neuewertung
        return wertung

    if werIstDran(board) == 'o': #Minimierender Spieler ist dran
        wertung = 999 #Höchster wert vordefiniert um diesen zu Minimieren
        neuewertung = 999
        for zug in moeglicheZuege(board): # alle möglichen Züge in einer Stellung werde durchgegangen
            neuewertung = minimax(zukunftsBoard(board,zug)) #Die Methode wird erneut (Rekursiv) aufgerufen.
            #die möglichen züge werden einzeln gespielt und übergeben. Davon wird dann die Wertung ermittelt (-1, 0 oder 1)
            if neuewertung < wertung: #Hier wird die kleinste Wertung geprüft(maximierung) und evtl. gespeichert.
                wertung = neuewertung
        return wertung



# Rückgabe des besten Zugs nach Minimax
# Diese Funktion ist eine Kopie der Minimax Methode nur ist hier der Rückgabe wert der Zug anstelle der Wertung.
# Hier hätte alternativ eine 2D-Liste verwendet werden können um beide Elemente aufeinmal zu übergeben.
def findeBestenZug(board): 
    aktuellerSpieler = werIstDran(board)
    if aktuellerSpieler == 'x':
        besteWertung = -999
    else:
        besteWertung = 999

    besterZug = None

    for zug in moeglicheZuege(board):
        neueWertung = minimax(zukunftsBoard(board, zug))

        if aktuellerSpieler == 'x':
            if neueWertung > besteWertung:
                besteWertung = neueWertung
                besterZug = zug
        else:
            if neueWertung < besteWertung:
                besteWertung = neueWertung
                besterZug = zug

    return besterZug


#Ausgabe des Boards in angenehmer Formatierung
def boardAusgeben(board):
    print ("   0 1 2")
    print("0  " + board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("1  " + board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("2  " + board[2][0] + "|" + board[2][1] + "|" + board[2][2])



#Spielschleife beginnt hier. Es ist immer Spieler vs AI oder AI vs Spieler
spieler = input("Wähle zwischen x oder o:")
while spieler not in ["x","o"]: # Solange eine nicht akzeptierte Eingabe stattfindet wird die Eingabe wiederholt
    spieler = input("'x' oder 'o':")

while spielZuende(board) == False: #Solange das Spiel läuft


    if spieler == 'x': # der Spieler spielt mit 'x'
        boardAusgeben(board)

        spalte = input("in welcher Spalte willst du dein '" + spieler + "' setzen?:")
        while spalte not in ["0","1","2"]:
            spalte = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe

        reihe = input("in welcher Reihe willst du dein '" + spieler + "' setzen?:")
        while reihe not in ["0","1","2"]:
            reihe = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe


        while [int(reihe),int(spalte)] not in moeglicheZuege(board): #Falls ein unmöglicher Zug gespielt wurde. Das heißt ein Feld wurde gewählt welches bereits gewählt wurde
            print("Das Feld ist bereits belegt!")
            spalte = input("in welcher Spalte willst du dein '" + spieler + "' setzen?:")
            while spalte not in ["0", "1", "2"]:
                spalte = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe

            reihe = input("in welcher Reihe willst du dein '" + spieler + "' setzen?:")
            while reihe not in ["0", "1", "2"]:
                reihe = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe


        board = zukunftsBoard(board,[int(reihe),int(spalte)]) #Der Spieler macht seinen Zug nach erfolgreicher Eingabe
        board = zukunftsBoard(board,findeBestenZug(board)) #Die AI macht seinen Zug
        
        
    if spieler == 'o': # der Spieler spielt mit 'o' 
    
        board = zukunftsBoard(board, findeBestenZug(board)) #Die AI macht seinen zug zuerst weil dieser dann als 'x' spielt
        boardAusgeben(board)
        if(spielZuende(board) == False): #Falls das spiel noch nicht vorbei ist -> Nötig da 'o' sonst noch einen Zug spielen kann da die AI zuerst seinen zug spielt

            spalte = input("in welcher Spalte willst du dein '" + spieler + "' setzen?:")
            while spalte not in ["0", "1", "2"]:
                spalte = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe

            reihe = input("in welcher Reihe willst du dein '" + spieler + "' setzen?:")
            while reihe not in ["0", "1", "2"]:
                reihe = input("Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:") #Erneute Eingabe bei nicht akzeptierter Eingabe



            while [int(reihe), int(spalte)] not in moeglicheZuege(board):  # Falls ein unmöglicher Zug gespielt wurde. Das heißt ein Feld wurde gewählt welches bereits gewählt wurde
                print("Das Feld ist bereits belegt!")
                spalte = input("in welcher Spalte willst du dein '" + spieler + "' setzen?:")
                while spalte not in ["0", "1", "2"]:
                    spalte = input(
                        "Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:")  # Erneute Eingabe bei nicht akzeptierter Eingabe

                reihe = input("in welcher Reihe willst du dein '" + spieler + "' setzen?:")
                while reihe not in ["0", "1", "2"]:
                    reihe = input(
                        "Mögliche Eingaben sind 0, 1 oder 2. Versuchen sie es erneut:")  # Erneute Eingabe bei nicht akzeptierter Eingabe


            board = zukunftsBoard(board,[int(reihe),int(spalte)]) #Der Spieler macht seinen Zug nach erfolgreicher Eingabe

#Ab hier ist das Spiel zuende, Der Gewinner wird ermittelt und wird ausgegeben
gewinner = bewerteStellung(board)
if gewinner == -1:
    print("")
    print("")
    print("o hat gewonnen")
    print("")
    boardAusgeben(board)
if gewinner == 0:
    print("")
    print("")
    print ("Unentschieden")
    print("")
    boardAusgeben(board)
if gewinner == 1:
    print("")
    print("")
    print("x hat gewonnen")
    print("")
    boardAusgeben(board)