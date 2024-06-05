import funcoes                                       # importa arquivo funcoes.py onde deixamos as funções do jogo

arq = open('jogo.txt')                     # abre o arquivo .txt com as palavras e as dicas

palavras = arq.readlines()                           # lê as linhas do arq em lista
palavra = funcoes.escolhePalavra(palavras)           # escolhe a palavra da lista enviada como parâmetro
dicas = funcoes.guardaDicas(palavras, palavra, 2)    # envia a lista, a palavra escolhida e a qtd de dicas. recebe dicas em lista.

letrasUsadas = ['']                                  # onde vamos guardar as letras já usadas
letrasErradas = ['']                                 # onde vamos guardar as letras usadas que não estão na palavra

arq.close()                                          # fecha o arquivo .txt

arrLetras = ['' for aux in range(len(palavra))]
for i in range(len(palavra)):
    arrLetras[i] = palavra[i].upper()
codigo = ['_ ' for aux in range(len(arrLetras))]     # cria os _ _ _ _ _ _

# Condições para continuar o jogo
palavraDecifrada = True
timer = funcoes.countdown(180)

print("Cibele Gameleira - RA: 1680972411009 \nGabriela Freitas - RA: 1680972411001 \nLetícia Nascimento - RA: 1680972411037");

print("Jogo[X] \nDicas[X] \nControle de tempo[X] \n")

print("Bem vindo(a) a um jogo da forca inovador. Eseja preparado(a) para esse desafio!")

print ("Antes de jogar, você precisa saber de algumas regras: \n")
print("- Você terá 7 vidas para acertar uma palavra;")
print("- As palavras não contém acentuação;")
print("- Você pode pedir dicas sobre as palavras, mas cuidado, elas custam uma vida;")
print("- Toda palavra tem duas dicas disponíveis;")
print("- Se suas vidas acabarem antes de adivinhar a palavra, você perde o jogo;")
print(" - Você terá um timer de de 3 minutos para jogar, se seu tempo acabar antes de acertar a palavra, você perde o jogo")
print("- Perdendo ou ganhando, você sempre pode jogar de novo.")



while (palavraDecifrada and timer):
    entrada = input('\nDigite uma letra ou peça por uma dica: ').upper()

    # Validações
    while(not entrada.isalpha() or (len(entrada) != 1 and entrada != 'DICA')):
        print('Entrada inválida. Digite uma letra por vez.')
        entrada = input().upper()

    if(entrada == 'DICA'):
        print(entrada)
    else:
        addArrLetrasUsadas = True
        entradaErrada = True
        palavraDecifrada = True
        # Checa se a letra já foi usada
        for i in range(len(letrasUsadas)):
            if(letrasUsadas[i] == entrada):
                print(f'A letra {entrada} já foi usada')
                addArrLetrasUsadas = False
                break
        
        for j in range(len(arrLetras)):
            if(arrLetras[j] == entrada):
                codigo[j] = arrLetras[j]
                entradaErrada = False
            if(codigo[j] == '_'):
                palavraDecifrada = False
        
        # Caso a entradaErrada = True, significa que nenhuma letra da palavra bate com a entrada. Guarda em array
        if(entradaErrada):
            letrasErradas.append(entrada)
        
        # Adiciona a letra apenas se ela não estiver já no array
        if(addArrLetrasUsadas):
            letrasUsadas.append(entrada)
        
        # Mostra letras erradas
        print('Letras erradas: ', end = '')
        for k in range(len(letrasErradas)):
            if(k == len(letrasErradas) - 1):
                print(f'{letrasErradas[k]}')
            else:
                print(f'{letrasErradas[k]}, ', end='')
        
        # Mostra a palavra
        for l in range(len(codigo)):
            if(l == len(codigo) - 1):
                print(codigo[l])
            else:
                print(f'{codigo[l]}', end='')

print('Fim de jogo!')