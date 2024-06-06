import random

# PARA fazerSetUpDoJogo, devemos pegar ler arquivo .txt com as palavras e dicas.
# Chamamos a função de escolherPalavra
def fazerSetUpDoJogo(palavrasUsadas):
    arq = open('jogo.txt')
    palavras = arq.readlines()
    arq.close()
    escolherPalavra(palavras, palavrasUsadas)

# PARA escolherPalavra, usamos o random na lista para sortear a palavra. 
# Enquanto tiver 'D:' na palavra e enquanto estiver na lista palavrasUsadas, continua sorteando
# Quando encontrar a palavra, chamamos a função acharDicas com a lista e a palavra 
# Retorna a palavra sem o 'P:' e sem o '\n'
def escolherPalavra(palavras, palavrasUsadas):
    palavra = random.choice(palavras)
    while 'D:' in palavra and palavra in palavrasUsadas:                         
        palavra = random.choice(palavras)
    acharDicas(palavras, palavra)

# PARA acharDicas, passamos pela lista até achar a palavra. 
# Chamamos o guardarDicas com a lista de palavras e o index da palavra encontrada
def acharDicas(palavras, palavra):
    for i in range(len(palavras)):
        if(palavras[i] == palavra):
            guardarDicas(palavras, i)

# PARA guardarDicas, procuramos as palavras com 'D:' a partir do index da palavra sorteado recebido
# Retorna o array de dicas
def guardarDicas(palavras, index):
    palavra = palavras[index][2:].strip()
    dicas = []
    k = index + 1
    while 'D:' in palavras[k]:
        dicas.append(palavras[k][2:].strip())
        k += 1
    iniciarJogo(dicas, palavra)

def iniciarJogo(dicas, palavra):
    dicasAtualizadas = sortearDica(dicas)
    dicasAtualizadas = entregarDica(dicasAtualizadas)
    print(dicasAtualizadas)

def sortearDica(dicas):
    indexDasDicas = len(dicas)
    indexSorteado = random.randint(1, indexDasDicas)
    print('Dicas: ', dicas.pop(indexSorteado))
    return dicas

def entregarDica(dicas):
    if len(dicas != 0): sortearDica(dicas) 
    else: print('Você já usou todas as suas dicas')

fazerSetUpDoJogo([])