import animationPacman

def showResult(quantityAvaliable, quantityErrors): 
    if(quantityAvaliable > 0):
        animationPacman.showError(quantityAvaliable, quantityErrors)
    elif(quantityAvaliable == 0):
        animationPacman.showGameOver();
    else:
        animationPacman.showRight(quantityAvaliable, quantityErrors)

showResult(1,6)