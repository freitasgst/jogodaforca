import funcoes

arq = open('jogoParaTestes.txt')
palavras = arq.readlines()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in palavras:
    print(f'{i.strip()}')

arq.close()

palavra = funcoes.escolhePalavra(palavras)
print(funcoes.guardaDicas(palavra))

funcoes.countdown(180)