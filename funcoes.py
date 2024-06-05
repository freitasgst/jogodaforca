import time, datetime 
import random

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = f'{mins:02d}:{secs:02d}'
        # return print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        return print(timer) 
        # return True
    #print('fim de jogo')
    return False

def escolhePalavra(palavras):
    palavra = random.choice(palavras)
    while 'D:' in palavra:                          # mesma coisa que while(palavra.find('D:') != -1):
        palavra = random.choice(palavras)
    return palavra[2:].strip()                      # tira o 'P:' antes de retornar a palavra e tira o '\n'

def guardaDicas(palavras, palavra, qtd):
    dicas = ['' for aux in range(qtd)]
    for i in range(len(palavras)):
        if(palavras[i].strip() == f'P:{palavra}'):
            for j in range(len(dicas)):
                k = i + 1 + j
                dicas[j] = palavras[k][2:].strip()
    return dicas

def defineFim(resultado, resposta, duracao):
    mensagem = ''
    if(resultado):
        mensagem = 'Parabéns, você ganhou!'
    else:
        if(duracao > 10):
            mensagem = f'Sinto muito, o tempo acabou. A palavra era {resposta}.'
        else:
            mensagem = f'Sinto muito, as vidas acabaram. A palavra era {resposta}.'
    return print(mensagem, '\n')