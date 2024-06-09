import time

YELLOW = "\033[1;33m"
RED   = "\033[1;31m"  
RESET  = "\033[0;0m"

animation1Pacman  = YELLOW + r' __________  ' + RESET
animation2Pacman  = YELLOW + r'/    X  X  \ ' + RESET
animation3Pacman  = YELLOW + r'|          | ' + RESET
animation4Pacman  = YELLOW + r'|     /\/\/  ' + RESET
animation5Pacman  = YELLOW + r'|    /      __ ' + RESET
animation6Pacman  = YELLOW + r'|    \     |__|' + RESET
animation7Pacman  = YELLOW + r'|     \/\/\  ' + RESET
animation8Pacman  = YELLOW + r'|          | ' + RESET
animation9Pacman  = YELLOW + r'\__________/ ' + RESET
animation10Pacman = YELLOW + r'|  //  ___ |' + RESET
animation11Pacman = YELLOW + r'|    //___\|' + RESET
animation12Pacman = YELLOW + r'|    \\___/|' + RESET
animation13Pacman = YELLOW + r'|          |' + RESET
animation14Pacman = YELLOW + r'/    ^  ^  \ ' + RESET
animation16Pacman = YELLOW + r'|    /  __   ' + RESET
animation17Pacman = YELLOW + r'|    \ |__|  ' + RESET
animation18Pacman = YELLOW + r'|          |' + RESET
animation19Pacman = YELLOW + r'|     \____|' + RESET
animation20Pacman = YELLOW + r'|          |' + RESET
animation21Pacman = YELLOW + r'|          |' + RESET
animation22Pacman = YELLOW + r'|      ____|' + RESET
animation23Pacman = YELLOW + r'|          |' + RESET
animation24Pacman = YELLOW + r'|   (_) ___|' + RESET
animation25Pacman = YELLOW + r'|      /   |' + RESET
animation26Pacman = YELLOW + r'|          |'

animation1GameOver = RED + r' ____                        ___                ' + RESET
animation2GameOver = RED + r'/ ___|  ___ _ __ ___   ___  / _ \__   _____ _ __' + RESET
animation3GameOver = RED + r'| |  _ / _ |  _   _ \ / _ \| | | \ \ / / _ \ __|' + RESET
animation4GameOver = RED + r'| |_| | (_|| | | | | |  __/| |_| |\ V /  __/ |  ' + RESET
animation5GameOver = RED + r'\_____|\___|_| |_| |_|\___| \___/  \_/ \___|_|  ' + RESET

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
    print('\n')

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
