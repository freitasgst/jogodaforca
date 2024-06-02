animation1PacMan = r' __________  '
animation2PacMan = r'/    X  X  \ '
animation3PacMan = r'|          | '
animation4PacMan = r'|     /\/\/  '
animation5PacMan = r'|    /       '
animation6PacMan = r'|    \       '
animation7PacMan = r'|     \/\/\  '
animation8PacMan = r'|          | '
animation9PacMan = r'\__________/ '

matriz = [[animation1PacMan],[animation2PacMan], [animation3PacMan], [animation4PacMan], [animation5PacMan], [animation6PacMan], [animation7PacMan], [animation8PacMan], [animation9PacMan]]

def showHungryPacman():
    for i in range(len(matriz)):
        print(matriz[i][0])

showHungryPacman()
 
