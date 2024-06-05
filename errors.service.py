import animationPacman

def showResult(isError, quantityAvaliable, quantityErrors): 
    if(isError == True):
        animationPacman.showError(quantityAvaliable, quantityErrors)
    else:
        animationPacman.showRight(quantityAvaliable, quantityErrors)

showResult(True,0,7)