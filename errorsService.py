import animationPacman

# PARA mostrarResultados, recebemos a quantidade de vidas e a de erros como parâmetros. 
# Se o jogador ainda tenha vidas, mas tem erros também, chamamos a função de mostrarErros no arquivo de animationPacman. 
# Se ele tiver todas as vidas, mostramos apenas a posição do pacman com todas as vidas ainda. Se a quantidade for zero, ele mostra o 'game over'
def showResult(quantityAvaliable, quantityErrors): 
    if(quantityAvaliable > 0 and quantityErrors > 0):
        animationPacman.showError(quantityAvaliable, quantityErrors)
    elif(quantityAvaliable == 7 and quantityErrors == 0):
        animationPacman.showPositonPacman(quantityAvaliable, quantityErrors)
    elif(quantityAvaliable == 0):
        animationPacman.showGameOver()