import time 
import random

arq = open('jogoParaTestes.txt')
palavras = arq.readlines()

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def escolhePalavra(palavras):
    palavra = random.choice(palavras)
    while 'D:' in palavra:                          # mesma coisa que while(palavra.find('D:') != -1):
        palavra = random.choice(palavras)
    return palavra.strip()

def guardaDicas(palavra):
    for i in range(len(palavras)):
        if(palavras[i].strip() == palavra):
            dica_1 = palavras[i+1].strip()
            dica_2 = palavras[i+2].strip()
    return [dica_1, dica_2]