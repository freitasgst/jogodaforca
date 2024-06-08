import random, time, sys, os

# Variáveis GLOBAIS
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

palavrasUsadas = []                        # onde vamos guardar as palavras usadas para que o jogador possa sempre ter palavras quando jogar novamente
dicas = []                                 # onde vamos guardar as dicas da rodada
dicasSorteadas = []
matrizDeTroca = [
    ['A', 'Á', 'À', 'Â', 'Ã'], 
    ['E', 'É', 'Ê', ' ', ' '], 
    ['I', 'Í', ' ', ' ', ' '], 
    ['O', 'Ó', 'Ò', 'Ô', 'Õ'], 
    ['U', 'Ú', ' ', ' ', ' '], 
    ['C', 'Ç', ' ', ' ', ' ']
]
arrLetrasParaTela = []                     # array para mostrar a palavra gramaticamente correta na tela
arrLetrasParaEntrada = []                  # array para comparar entrada com palavra ignorando acentos e ç
codigo = []                                # array para mostrar a palavra como _ _ _ _ _ _ _
letrasUsadas = []                          # onde vamos guardar todas as letras já usadas na rodada
letrasErradas = []                         # onde vamos guardar só as letras usadas na rodada que não estão na palavra
recados = ['']
duracao = 180                              # duração das rodadas
controleDeTempoInicial = []                # array para guardar os tempos iniciais para calcular duração da rodada para saber se o jogador perdeu ou não
controleDeTempoFinal = []                  # array para guardar os tempos finais para calcular duração da rodada para mostrar no board de status no final
resultados = []                            # array para guardar se é vitória ou derrota para mostrar no board de status no final

# PARA fazerSetUpDoJogo, devemos limpar as variáveis do jogo anterior.
# Chamamos a função de lerArquivoComPalavras
def fazerSetUpDoJogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    dicas.clear()
    dicasSorteadas.clear()
    arrLetrasParaTela.clear()
    arrLetrasParaEntrada.clear()
    codigo.clear()
    letrasUsadas.clear()
    letrasErradas.clear()
    lerArquivoComPalavras()

# PARA lerArquivoComPalavras, devemos abrir o arquivo .txt com as palavras e dicas e guardar essa informação em uma lista. 
# Chamamos a função de escolherPalavra
def lerArquivoComPalavras():
    arq = open('jogo.txt', encoding='utf-8')
    palavras = arq.readlines()
    arq.close()
    escolherPalavra(palavras, palavrasUsadas)

# PARA escolherPalavra, usamos o random na lista para sorteio. 
# Enquanto tiver 'D:' na palavra e enquanto estiver na lista palavrasUsadas, continua sorteando
# Quando encontrar a palavra, chamamos a função acharDicas com a lista e a palavra 
def escolherPalavra(palavras, palavrasUsadas):
    palavra = random.choice(palavras)
    while 'D:' in palavra or palavra[2:].strip() in palavrasUsadas:                         
        palavra = random.choice(palavras)
    acharDicas(palavras, palavra)

# PARA acharDicas, passamos pela lista até achar a palavra. 
# Chamamos o guardarDicas com a lista de palavras e o index da palavra encontrada
def acharDicas(palavras, palavra):
    for i in range(len(palavras)):
        if(palavras[i] == palavra):
            guardarDicas(palavras, i)

# PARA guardarDicas, procuramos as palavras com 'D:' a partir do index da palavra sorteado recebido
# Chamamos a função de guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas
def guardarDicas(palavras, index):
    k = index + 1
    while(k != len(palavras)):
        while 'D:' in palavras[k]:
            dicas.append(palavras[k][2:].strip())
            k += 1
        break
    guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavras[index])

# PARA guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas, tiramos 'P:' e a '\n'
# Chamamos a função setUpTelaInicialDoJogo
def guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavraBruta):
    palavra = palavraBruta[2:].strip()
    palavrasUsadas.append(palavra)
    setUpTelaInicialDoJogo(palavra)

def setUpTelaInicialDoJogo(palavra):
    controleDeTempoInicial.append(time.time())
    for i in range(len(palavra)):
        arrLetrasParaTela.append(palavra[i].upper())
        trocarLetrasParaCriarArrLetrasParaEntrada(palavra[i].upper())
        codigo.append('_ ')
    definirPalavraParaEntrada()

def trocarLetrasParaCriarArrLetrasParaEntrada(letra):
    for linha in range(len(matrizDeTroca)):
        for coluna in range(len(matrizDeTroca[linha])):
            if letra == matrizDeTroca[linha][coluna]:
                    letra = matrizDeTroca[linha][0]
    arrLetrasParaEntrada.append(letra)

def definirPalavraParaEntrada():
    novaPalavra = ''.join(arrLetrasParaEntrada)
    desenharTelaInicialDoJogo(novaPalavra)

def desenharTelaInicialDoJogo(palavra):
    sortearDica()
    for l in range(len(codigo)):
        if(l == len(codigo) - 1): print(codigo[l])
        else: print(f'{codigo[l]}', end='')
    mostrarDicasNaTela()
    jogo(palavra)

def sortearDica():
    indexDasDicas = len(dicas) - 1
    indexSorteado = random.randint(0, indexDasDicas)
    dicasSorteadas.append(dicas.pop(indexSorteado))

def mostrarDicasNaTela():
    if(len(dicasSorteadas) != 0):
        for i in range(len(dicasSorteadas)):
            print('Dica: ', dicasSorteadas[i])

def jogo(palavra):
    timer = controlarTempo(time.time())
    while(len(letrasErradas) < 7):
        entrada = pedirAcaoJogador(palavra)
        setUpParaRedesenharTela(entrada)
    definirDerrota(timer)

def pedirAcaoJogador(palavra):
    entrada = validarEntrada(palavra)
    if(entrada == 'DICA'):
        # FUNÇÃO PARA TIRAR VIDA
        checarSeAindaHáDicasParaEntregar()
    elif(entrada == palavra): definirVitoria()
    else:
        checarSeLetraJaFoiUsada(entrada)
    return entrada

def validarEntrada(palavra):
    entrada = input('\nDigite uma letra ou peça por uma dica: ').upper()
    novaEntrada = trocarEntradaParaJogo(entrada)
    while(not entrada.isalpha() or (len(entrada) != 1 and (entrada != 'DICA' and novaEntrada != palavra))):
        entrada = input('\nEntrada inválida: ').upper()
        novaEntrada = trocarEntradaParaJogo(entrada)
    return novaEntrada

def trocarEntradaParaJogo(entrada):
    arrTemporarioParaNovaEntrada = ['' for aux in range(len(entrada))]
    for i in range(len(entrada)):
        arrTemporarioParaNovaEntrada[i] = entrada[i]
        for linha in range(len(matrizDeTroca)):
            for coluna in range(len(matrizDeTroca[linha])):
                if entrada[i] == matrizDeTroca[linha][coluna]:
                    arrTemporarioParaNovaEntrada[i] = matrizDeTroca[linha][0]
    return ''.join(arrTemporarioParaNovaEntrada)

def checarSeAindaHáDicasParaEntregar():
    if (len(dicas) != 0): 
        sortearDica() 
        mostrarDicasNaTela()
    else: 
        print('Você já usou todas as suas dicas')

def checarSeLetraJaFoiUsada(entrada):
    adicionaLetraJaUsada = True
    if (len(letrasUsadas) == 0):
        letrasUsadas.append(entrada)
        adicionaLetraJaUsada = False
    else:
        for i in range(len(letrasUsadas)):
            if(letrasUsadas[i] == entrada): 
                adicionaLetraJaUsada = False
                recados[0] = f'A letra {entrada} já foi usada'
                break
    if adicionaLetraJaUsada: letrasUsadas.append(entrada)
    definirSeEntradaExisteNaPalavra(entrada)

def definirSeEntradaExisteNaPalavra(entrada):
    entradaErrada = True
    for i in range(len(arrLetrasParaEntrada)):
        if(entrada == arrLetrasParaEntrada[i]):
            entradaErrada = False
            break
    if entradaErrada: adicionarLetraNoArrayDeLetrasErradas(entrada)

def adicionarLetraNoArrayDeLetrasErradas(entrada):
    adicionaLetraErrada = True
    if(len(letrasErradas) == 0): 
        letrasErradas.append(entrada)
        adicionaLetraErrada = False
    else:
        for i in range(len(letrasErradas)):
            if(entrada == letrasErradas[i]): 
                adicionaLetraErrada = False
                break
    if adicionaLetraErrada: 
        letrasErradas.append(entrada)
        # FUNÇÃO PARA TIRAR VIDA

def setUpParaRedesenharTela(entrada): 
    os.system('cls' if os.name == 'nt' else 'clear')
    for j in range(len(arrLetrasParaTela)):
        if(arrLetrasParaEntrada[j] == entrada):
            codigo[j] = arrLetrasParaTela[j]
    redesenharTela()
    recados[0] = ''

def redesenharTela(): 
    mostrarRecadosNaTela()
    mostrarListaDeLetrasErradas()
    mostrarCodigoAtualizado()
    mostrarDicasNaTela()
    checarSeCodigoFoiResolvido()

def mostrarRecadosNaTela():
    print(recados[0])

def mostrarListaDeLetrasErradas():
    if(len(letrasErradas) != 0):
        print('Letras erradas: ', end = '')
        for k in range(len(letrasErradas)):
            if(k == len(letrasErradas) - 1): 
                print(f'{letrasErradas[k]}')
            else: 
                print(f'{letrasErradas[k]}, ', end='')

def mostrarCodigoAtualizado():
    for l in range(len(codigo)):
        if(l == len(codigo) - 1): print(codigo[l])
        else: print(f'{codigo[l]}', end='')

def checarSeCodigoFoiResolvido():
    palavraDecifrada = True
    for m in range(len(codigo)):
        if(codigo[m] == '_ '): palavraDecifrada = False
    if palavraDecifrada : definirVitoria()

def controlarTempo(agora): 
    index = len(controleDeTempoInicial) - 1
    duracao = controleDeTempoInicial[index] - agora
    return duracao

def definirVitoria():
    mensagem = f'{GREEN}Parabéns, você ganhou!{RESET}\U0001F601'
    resultados.append(1)
    print(mensagem, '\n')
    setUpParaDesenharTelaDeFimDeJogo()

def definirDerrota(timer):
    resultados.append(0)
    resposta = ''.join(arrLetrasParaTela)
    if(timer > duracao): mensagem = f'{RED}Sinto muito, o tempo acabou.{RESET} A palavra era {resposta}.\U0001F61E'
    else: mensagem = f'{RED}Sinto muito, as vidas acabaram.{RESET} A palavra era {resposta}.\U0001F61E'
    print(mensagem, '\n')
    setUpParaDesenharTelaDeFimDeJogo()

def setUpParaDesenharTelaDeFimDeJogo():
    time.sleep(2)
    controleDeTempoFinal.append(time.time())
    for i in range(len(palavrasUsadas)):
        print('i', i)
        mins, secs = divmod(round(controleDeTempoFinal[i] - controleDeTempoInicial[i]), 60) 
        mensagem = f'{i+1}ª rodada - {palavrasUsadas[i]} - {mins:02d}:{secs:02d}'
        desenharTelaDeFimDeJogo(mensagem)

def desenharTelaDeFimDeJogo(mensagem):
    for i in range(len(palavrasUsadas)):
        if(resultados[i] == 1): print(GREEN + mensagem + RESET)
        else: print(RED + mensagem + RESET)
    input('Pressione ENTER para continuar')
    decisaoDoUsuarioParaFimDeJogo()
    
def decisaoDoUsuarioParaFimDeJogo():
    novoJogo = validarNovoJogo()
    if(novoJogo == 'Y'): fazerSetUpDoJogo() 
    else: sys.exit()

def validarNovoJogo():
    novoJogo = input('Deseja jogar novamente? [Y/n]: ').upper()
    while(novoJogo != 'Y' and novoJogo != 'N'):
        novoJogo = input('Código inválido. Digite Y para jogar novamente ou N para sair: ').upper()
    return novoJogo