import animationPacman

def showResult(quantityAvaliable, quantityErrors): 
    if(quantityAvaliable > 0 and quantityErrors > 0):
        animationPacman.showError(quantityAvaliable, quantityErrors)
    elif(quantityAvaliable == 7 and quantityErrors == 0):
        animationPacman.showPositonPacman(quantityAvaliable, quantityErrors)
    elif(quantityAvaliable == 0):
        animationPacman.showGameOver()
    else:
        animationPacman.showRight(quantityAvaliable, quantityErrors)