import time

animation1Pacman = r' __________  '
animation2Pacman = r'/    X  X  \ '
animation3Pacman = r'|          | '
animation4Pacman = r'|     /\/\/  '
animation5Pacman = r'|    /      __ '
animation6Pacman = r'|    \     |__|'
animation7Pacman = r'|     \/\/\  '
animation8Pacman = r'|          | '
animation9Pacman = r'\__________/ '
animation10Pacman = r'|  //  ___ |'
animation11Pacman = r'|    //___\|'
animation12Pacman = r'|    \\___/|'
animation13Pacman = r'|          |'
animation14Pacman = r'/    ^  ^  \ '
animation16Pacman = r'|    /  __   '
animation17Pacman = r'|    \ |__|  '
animation18Pacman = r'|          |'
animation19Pacman = r'|     \____|'
animation20Pacman = r'|          |'
animation21Pacman = r'|          |'
animation22Pacman = r'|      ____|'
animation23Pacman = r'|          |'
animation24Pacman = r'|   (_) ___|'
animation25Pacman = r'|      /   |'
animation26Pacman = r'|          |'
animation1GameOver = r' ____                        ___                '              
animation2GameOver = r'/ ___|  ___ _ __ ___   ___  / _ \__   _____ _ __'
animation3GameOver = r'| |  _ / _ |  _   _ \ / _ \| | | \ \ / / _ \ __|'
animation4GameOver = r'| |_| | (_|| | | | | |  __/| |_| |\ V /  __/ |  ' 
animation5GameOver = r'\_____|\___|_| |_| |_|\___| \___/  \_/ \___|_|  '

animationFood1 = r' __'
animationFood2 = r'|__|'

  
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
    time.sleep(2)

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
    time.sleep(2)

def showGoodPacman():
    goodPacman = [[animation1Pacman],
                  [animation14Pacman],
                [animation3Pacman],
                [animation10Pacman],
                [animation11Pacman],
                [animation12Pacman],
                [animation13Pacman],
                [animation8Pacman],
                [animation9Pacman]]
    
    for i in range(len(goodPacman)):
        print(goodPacman[i][0])
    time.sleep(2)

def showHappyPacman():
    goodPacman = [[animation1Pacman],
                  [animation2Pacman],
                [animation3Pacman],
                [animation18Pacman],
                [animation19Pacman],
                [animation20Pacman],
                [animation21Pacman],
                [animation8Pacman],
                [animation9Pacman]]
    
    for i in range(len(goodPacman)):
        print(goodPacman[i][0])
    time.sleep(2)

def showPositonPacman(quantityFood, quantityShit):
    food = ['\U0001F354', '\U0001F354', '\U0001F354', '\U0001F354', '\U0001F354', '\U0001F354', '\U0001F354']
    shit = ['\U0001F4A9', '\U0001F4A9', '\U0001F4A9', '\U0001F4A9', '\U0001F4A9', '\U0001F4A9', '\U0001F4A9']
    packman = "\n" + animation1Pacman + "\n" + animation2Pacman + "\n" + animation3Pacman + "\n" + animation18Pacman + "\n" + animation22Pacman + "\n" +animation20Pacman + "\n" + animation21Pacman + "\n" + animation8Pacman + "\n" + animation9Pacman + "\n"

    for _ in range(quantityShit):
        food.pop(0)
    for _ in range(quantityFood):
        shit.pop(0)
    print('=====================================================================================================')
    print("      ".join(shit),  packman, "\n" ,"       ".join(food), '\n',f'Quantidade de tentativas restantes: {quantityFood}\n', f'Quantidade de erros: {quantityShit} \n')
    print('=====================================================================================================')
 
def showSadPacman():
    goodPacman = [[animation1Pacman],
                  [animation2Pacman],
                [animation3Pacman],
                [animation23Pacman],
                [animation24Pacman],
                [animation25Pacman],
                [animation26Pacman],
                [animation8Pacman],
                [animation9Pacman]]
    
    for i in range(len(goodPacman)):
        print(goodPacman[i][0])
    time.sleep(2)

def showGameOver(): 
    gameOver = [[animation1GameOver],
                  [animation2GameOver],
                [animation3GameOver],
                [animation4GameOver],
                [animation5GameOver]]
    
    for i in range(len(gameOver)):
        print(gameOver[i][0])
    time.sleep(2)

def showError(quantityAvaliable, quantityErrors):  
    if(quantityAvaliable > 0):
        showHungryPacman()
        showEatingPacman()
        showGoodPacman()
        showHappyPacman()
        showPositonPacman(quantityAvaliable, quantityErrors)
    else:
        showGameOver()

def showRight(quantityAvaliable, quantityErrors):  
    showSadPacman()
    showPositonPacman(quantityAvaliable, quantityErrors)
