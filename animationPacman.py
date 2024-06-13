import time, os

lifes = 7

YELLOW = "\033[1;33m"
RED   = "\033[1;31m"  
RESET  = "\033[0;0m"
GREEN = "\033[0;32m"

# Variáveis com os desenhos dos frames do pacmas
animation1Pacman  = YELLOW + r' __________  ' + RESET
animation2Pacman  = YELLOW + r'/    X  X  \ ' + RESET
animation3Pacman  = YELLOW + r'|          | ' + RESET
animation4Pacman  = YELLOW + r'|     /\/\/  ' + RESET
animation5Pacman  = YELLOW + r'|    /      __ ' + RESET
animation6Pacman  = YELLOW + r'|    \     |__|' + RESET                 # hungry
animation7Pacman  = YELLOW + r'|     \/\/\  ' + RESET
animation8Pacman  = YELLOW + r'|          | ' + RESET
animation9Pacman  = YELLOW + r'\__________/ ' + RESET
animation10Pacman = YELLOW + r'|  //  ___ |' + RESET
animation11Pacman = YELLOW + r'|    //___\|' + RESET                    # good
animation12Pacman = YELLOW + r'|    \\___/|' + RESET
animation13Pacman = YELLOW + r'|          |' + RESET
animation14Pacman = YELLOW + r'/    ^  ^  \ ' + RESET
animation16Pacman = YELLOW + r'|    /  __   ' + RESET
animation17Pacman = YELLOW + r'|    \ |__|  ' + RESET                   # eating
animation18Pacman = YELLOW + r'|          |' + RESET
animation19Pacman = YELLOW + r'|     \____|' + RESET                    # happy
animation20Pacman = YELLOW + r'|          |' + RESET
animation21Pacman = YELLOW + r'|          |' + RESET
animation22Pacman = YELLOW + r'|      ____|' + RESET                    # position
animation23Pacman = YELLOW + r'|          |' + RESET
animation24Pacman = YELLOW + r'|       ___|' + RESET
animation25Pacman = YELLOW + r'|      /   |' + RESET                    # sad
animation26Pacman = YELLOW + r'|          |'
animation1GameOver = RED + r' ____                        ___                ' + RESET
animation2GameOver = RED + r'/ ___|  ___ _ __ ___   ___  / _ \__   _____ _ __' + RESET
animation3GameOver = RED + r'| |  _ / _ |  _   _ \ / _ \| | | \ \ / / _ \ __|' + RESET
animation4GameOver = RED + r'| |_| | (_|| | | | | |  __/| |_| |\ V /  __/ |  ' + RESET
animation5GameOver = RED + r'\_____|\___|_| |_| |_|\___| \___/  \_/ \___|_|  ' + RESET

animation1WIN = GREEN + r'__        __ _ __   _ ' + RESET
animation2WIN = GREEN + r'\ \      / /| || \ | |' + RESET
animation3WIN = GREEN + r' \ \ /\ / / | ||  \| |' + RESET
animation4WIN = GREEN + r'  \ V  V /  | || |\  |' + RESET
animation5WIN = GREEN + r'   \/\/\/   |_||_| \_|' + RESET
animationFood1 = r' __'
animationFood2 = r'|__|'

# PARA mostrarPacmanComFome, criamos uma matriz com os desenhos que compõem a imagem do pacman abrindo a boca para um hambúrguer. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, limpamos o terminal, para que a animação ficasse sobreposta
def showHungryPacman():
    hungryPacman = [[animation1Pacman], 
                     [animation2Pacman], 
                     [animation3Pacman], 
                     [animation4Pacman], 
                     [animation5Pacman], 
                     [animation6Pacman], 
                     [animation7Pacman], 
                     [animation8Pacman], 
                     [animation9Pacman]]
    
    showImage(hungryPacman)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# PARA mostrarPacmanComendo, criamos uma matriz com os desenhos que compõem a imagem do pacman mastigando o hamburguer. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, limpamos o terminal
def showEatingPacman():
    hungryPacman = [[animation1Pacman], 
          [animation2Pacman], 
          [animation3Pacman], 
          [animation4Pacman], 
          [animation16Pacman], 
          [animation17Pacman], 
          [animation7Pacman], 
          [animation8Pacman], 
          [animation9Pacman]]
      
    showImage(hungryPacman)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# PARA mostrarPacmanBom, criamos uma matriz com os desenhos que compõem a imagem do pacman fechando a boca. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, limpamos o terminal
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
    
    showImage(goodPacman)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# PARA mostrarPacmanFeliz, criamos uma matriz com os desenhos que compõem a imagem do pacman sorrindo. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, limpamos o terminal
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
    
    showImage(goodPacman)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# PARA mostrarPosicaoPacman, criamos um array com 7 emojis de hamburguer e um com 7 de cocô, além de uma variável que junta as strings do pacman neutro com um enter entre elas.
# O valor de quantidade de vidas é usado como loop para tirar o elemento da posição 0 com pop do array de hamburgueres. Mesma coisa com o de cocô.
# Com o print, colocamos as comidas juntadas com espaços em cima, o pacman neutro, e os cocôs embaixo
def showPositonPacman(quantityFood, quantityShit):
    food = ['\U0001F354' for aux in range(lifes)]
    shit = ['\U0001F4A9' for aux in range(lifes)]
    pacman = "\n" + animation1Pacman + "\n" + animation2Pacman + "\n" + animation3Pacman + "\n" + animation18Pacman + "\n" + animation22Pacman + "\n" +animation20Pacman + "\n" + animation21Pacman + "\n" + animation8Pacman + "\n" + animation9Pacman + "\n"
    for _ in range(quantityShit):
        food.pop(0)
    for _ in range(quantityFood):
        shit.pop(0)
    print('=====================================================================================================')
    print("      ".join(food),  pacman, "\n" ,"       ".join(shit), '\n',f'Quantidade de tentativas restantes: {quantityFood}\n', f'Quantidade de erros: {quantityShit} \n')
    print('=====================================================================================================')

# PARA mostrarGameOver, criamos uma matriz com os desenhos que compõem a imagem das palavras game over. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, damos um espaço para a tela de fim de jogo
def showGameOver(): 
    gameOver = [[animation1GameOver],
                [animation2GameOver],
                [animation3GameOver],
                [animation4GameOver],
                [animation5GameOver]]
    
    showImage(gameOver)
    time.sleep(1)
    print('\n')

# PARA mostrarVitória, criamos uma matriz com os desenhos que compõem a imagem das palavras win. 
# Com o mostrarImagem, damos print em cada um deles, um embaixo do outro, formando assim a figura e, depois de um segundo, damos um espaço para a tela de fim de jogo
def showWin(): 
    win = [[animation1WIN],
           [animation2WIN],
           [animation3WIN],
           [animation4WIN],
           [animation5WIN]]
    
    showImage(win)
    time.sleep(1)
    print('\n')

# PARA mostrarErro, chamamos as funções mostrarPacmanComFome, mostrarPacmanComendo, mostrarPacmanBem e mostrarPacmanFeliz como keyframes da animação
# Chamamos a função mostrarPosicaoPacman com a quantidade de vidas e de erros. 
def showError(quantityAvaliable, quantityErrors):  
    if(quantityAvaliable > 0):
        showHungryPacman()
        showEatingPacman()
        showGoodPacman()
        showHappyPacman()
        showPositonPacman(quantityAvaliable, quantityErrors)
    else:
        showGameOver()

# RECEBE COMO PARAMETRO UMA MATRIZ BIDIMENSIONAL PARA EXIBIR UMA IMAGEM. ESSA FUNCAO IRA PERCORRER AS LINHAS DA MATRIZ E EXIBIR
# O CONTEUDO DA COLUNA DA POSICAO ZERO. SERVE PARA QUALQUER TIPO DE EXIBICAO DE MATRIZ COM VALORES APENAS NO INDICE ZERO
def showImage(image): 
    for i in range(len(image)):
        print(image[i][0])