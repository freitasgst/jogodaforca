import funcoes                                                  # importa arquivo funcoes.py onde deixamos as funções do jogo
import datetime, sys

arq = open('jogo.txt', encoding='utf-8')                                          # abre o arquivo .txt com as palavras e as dicas
t = 180

palavras = arq.readlines()                                      # lê as linhas do arq em lista
palavra = funcoes.escolhePalavra(palavras)                      # escolhe a palavra da lista enviada como parâmetro

dicas = funcoes.guardaDicas(palavras, palavra)                  # envia a lista, a palavra escolhida e a qtd de dicas. recebe dicas em lista.
num_dicas = len(dicas)

arq.close()                                                     # fecha o arquivo .txt

letrasUsadas = []                                               # onde vamos guardar as letras já usadas
letrasErradas = []                                              # onde vamos guardar as letras usadas que não estão na palavra
controlador_dicas = 0                                           # usamos essa variável para controlar a quantidade de dicas

# Desenho da tela inicial
print("Nome: Cibele Gameleira - RA: 1680972411009 \nNome: Gabriela Freitas - RA: 1680972411001 \nNome: Letícia Nascimento - RA: 1680972411037")

print("Jogo[X] \nDicas[X] \nControle de tempo[X] \n")

print("Bem vindo(a) a um jogo da forca inovador. Esteja preparado(a) para esse desafio!")

print("Antes de jogar, você precisa saber de algumas regras: \n")
print("- Você terá 7 vidas para acertar uma palavra;")
print("- As palavras não contém acentuação;")
print("- Você pode pedir dicas sobre as palavras, mas cuidado, elas custam uma vida;")
print("- Toda palavra uma ou mais dicas disponíveis;")
print("- Se suas vidas acabarem antes de adivinhar a palavra, você perde o jogo;")
print("- Perdendo ou ganhando, você sempre pode jogar de novo.\n")

# Pede ação do jogador, para que a contagem de tempo comece apenas quando o jogador estiver preparado
inicio = input('Pronto para começar? [Y/n]: ').upper()
while(inicio != 'Y' and inicio != 'N'):
    inicio = input('Comando inválido. Digite Y para começar ou N para sair do jogo: ').upper()

if(inicio == 'Y'):
    # Começa o jogo
    agora = datetime.datetime.now().second
    
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

    while(not palavraDecifrada and duracao <= t and len(letrasErradas) < 7):
        entrada = input('\nDigite uma letra ou peça por uma dica: ').upper()
        addArrLetras = True                                                     # boolean para saber se a entrada já consta no array de letras usadas
        entradaErrada = True                                                    # boolean para controlar se a entrada deve ser adicionada ao array de letras erradas
        palavraDecifrada = True                                                 # boolean para saber se o jogo terminou

        # Validações
        while(not entrada.isalpha() or (len(entrada) != 1 and entrada != 'DICA')):
            entrada = input('\nEntrada inválida. Digite uma letra por vez: ').upper()

        if(entrada == 'DICA'):
            if(controlador_dicas < num_dicas):
                palavraDecifrada = False
                controlador_dicas += 1
            else:
                print('Você já usou todas as suas dicas')
            print('Dica: ', dicas[controlador_dicas])
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

    funcoes.defineFim(palavraDecifrada, palavra, duracao)
    novoJogo = input('Deseja jogar novamente? [Y/n]: ').upper()
    while(novoJogo != 'Y' and novoJogo != 'N'):
        novoJogo = input('Código inválido. Digite Y para jogar novamente e N para sair: ').upper()
    if(novoJogo == 'Y'):
        # chama funcao de jogo
        print('chama funcao de jogo')
        
    else:
        sys.exit()
else:
    sys.exit()
