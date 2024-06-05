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

def jogo(palavra, dicas, num_dicas):
    # Começa o jogo
    agora = datetime.datetime.now().second
    t = 180

    letrasUsadas = []                                               # onde vamos guardar as letras já usadas
    letrasErradas = []                                              # onde vamos guardar as letras usadas que não estão na palavra
    controlador_dicas = 0                                           # usamos essa variável para controlar a quantidade de dicas
    
    arrLetras = ['' for aux in range(len(palavra))]
    for i in range(len(palavra)):
        arrLetras[i] = palavra[i].upper()                           # separa cada letra da palavra e põe na lista
    codigo = ['_ ' for aux in range(len(arrLetras))]                # cria os _ _ _ _ _ _

    for l in range(len(codigo)):
        if(l == len(codigo) - 1):
            print(codigo[l])
        else:
            print(f'{codigo[l]}', end='')                           # desenha os _ _ _ _ _ _ iniciais na tela

    # Condições para continuar vivo
    duracao = 0
    palavraDecifrada = False
    # timer = funcoes.countdown(180)

    while(not palavraDecifrada and duracao <= t):
        entrada = input('\nDigite uma letra ou peça por uma dica: ').upper()
        addArrLetras = True                                                     # boolean para saber se a entrada já consta no array de letras usadas
        entradaErrada = True                                                    # boolean para controlar se a entrada deve ser adicionada ao array de letras erradas
        palavraDecifrada = True                                                 # boolean para saber se o jogo terminou

        # Validações
        while(not entrada.isalpha() or (len(entrada) != 1 and entrada != 'DICA')):
            entrada = input('\nEntrada inválida. Digite uma letra por vez: ').upper()

        if(entrada == 'DICA'):
            if(controlador_dicas < num_dicas):
                print('Dica: ', dicas[controlador_dicas])
                controlador_dicas += 1
            else:
                print('Você já usou todas as suas dicas')
        else:
            # Checa se a letra já foi usada
            for i in range(len(letrasUsadas)):
                if(letrasUsadas[i] == entrada):
                    print(f'A letra {entrada} já foi usada')
                    addArrLetras = False
                    break
            
            # Se a entrada estiver no arrLetras, a coloque no array codigo em mesma posição
            for j in range(len(arrLetras)):
                if(arrLetras[j] == entrada):
                    codigo[j] = arrLetras[j]
                    entradaErrada = False
            
            # Checa se todos os elementos da lista codigo foram trocados
            # Se não, é porque a palavra ainda não foi adivinhada
            for m in range(len(codigo)):
                if(codigo[m] == '_ '):
                    palavraDecifrada = False
            
            # Adiciona a letra apenas se ela não estiver já no array
            if(addArrLetras):
                letrasUsadas.append(entrada)
                # Caso a entradaErrada = True, significa que nenhuma letra da palavra bate com a entrada. 
                # Guarda essa letra em array e chama função que tira vida
                if(entradaErrada):
                    letrasErradas.append(entrada)
            
            # Mostra letras erradas
            if(len(letrasErradas) != 0):
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

            tempo = datetime.datetime.now().second
            duracao = tempo - agora

    defineFim(palavraDecifrada, palavra, duracao)

def defineFim(resultado, resposta, duracao):
    mensagem = ''
    if(resultado):
        mensagem = 'Parabéns, você ganhou!\U0001F601'
    else:
        if(duracao > 10):
            mensagem = f'Sinto muito, o tempo acabou. A palavra era {resposta}.\U0001F61E'
        else:
            mensagem = f'Sinto muito, as vidas acabaram. A palavra era {resposta}.\U0001F61E'
    return print(mensagem, '\n')