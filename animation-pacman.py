animation1Pacman = r' __________  '
animation2Pacman = r'/    X  X  \ '
animation3Pacman = r'|          | '
animation4Pacman = r'|     /\/\/  '
animation5Pacman = r'|    /       '
animation6Pacman = r'|    \       '
animation7Pacman = r'|     \/\/\  '
animation8Pacman = r'|          | '
animation9Pacman = r'\__________/ '
animation10Pacman = r'|      ___ |'
animation11Pacman = r'|     /___\|'
animation12Pacman = r'|     \___/|'
animation13Pacman = r'|          |'
animation14Pacman = r'/   X  X   \ '
animation16Pacman = r'|    /  __   '
animation17Pacman = r'|    \ |__|  '
animationFood1 = r' __'
animationFood2 = r'|__|'


def showGoodPacman():
    goodPacman = [[animation1Pacman],
                  [animation2Pacman],
                [animation3Pacman],
                [animation10Pacman],
                [animation11Pacman],
                [animation12Pacman],
                [animation13Pacman],
                [animation8Pacman],
                [animation9Pacman]]
    
    for i in range(len(goodPacman)):
        print(goodPacman[i][0])


def showHungryPacman():
    hungryPackman = [[animation1Pacman], 
          [animation2Pacman], 
          [animation3Pacman], 
          [animation4Pacman], 
          [animation5Pacman], 
          [animation6Pacman], 
          [animation7Pacman], 
          [animation8Pacman], 
          [animation9Pacman]]
    
    for i in range(len(hungryPackman)):
        print(hungryPackman[i][0])

def showEatingPacman():
    hungryPackman = [[animation1Pacman], 
          [animation2Pacman], 
          [animation3Pacman], 
          [animation4Pacman], 
          [animation16Pacman], 
          [animation17Pacman], 
          [animation7Pacman], 
          [animation8Pacman], 
          [animation9Pacman]]
      
    for i in range(len(hungryPackman)):
        print(hungryPackman[i][0])

showGoodPacman()
showHungryPacman()
showEatingPacman()