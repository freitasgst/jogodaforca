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
    ['E', 'É', 'Ê'], 
    ['I', 'Í'], 
    ['O', 'Ó', 'Ò', 'Ô', 'Õ'], 
    ['U', 'Ú'], 
    ['C', 'Ç']
]
arrLetrasParaTela = []                     # array para mostrar a palavra gramaticamente correta na tela
arrLetrasParaEntrada = []                  # array para comparar entrada com palavra ignorando acentos e ç
codigo = []                                # array para mostrar a palavra como _ _ _ _ _ _ _
letrasUsadas = []                          # onde vamos guardar todas as letras já usadas na rodada
letrasErradas = []                         # onde vamos guardar só as letras usadas na rodada que não estão na palavra
vidas = []                                 # onde vamos guardar perda de vidas
recados = ['']                             # onde guardamos qualquer mensagem pro jogador; necessário devido ao cls
duracao = 180                              # duração das rodadas
controleDeTempoInicial = []                # array para guardar os tempos iniciais para calcular duração da rodada para saber se o jogador perdeu ou não
controleDeTempoFinal = []                  # array para guardar os tempos finais para calcular duração da rodada para mostrar no board de status no final
resultados = []                            # array para guardar se é vitória ou derrota para mostrar no board de status no final

# PARA fazerSetUpDoJogo, devemos limpar as variáveis do jogo anterior, 
# mantendo apenas os arrays de controle de tempo, resultados e palavras usadas, que serão usadas para a tela final e validação de palavra sorteada.
# Chamamos a função de lerArquivoComPalavras
def fazerSetUpDoJogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    if(len(recados) != 0): recados[0] = ''
    dicas.clear()
    dicasSorteadas.clear()
    arrLetrasParaTela.clear()
    arrLetrasParaEntrada.clear()
    codigo.clear()
    vidas.clear()
    letrasUsadas.clear()
    letrasErradas.clear()
    lerArquivoComPalavras()

# PARA lerArquivoComPalavras, devemos abrir o arquivo .txt com as palavras e dicas e guardar essa informação em uma lista. 
# Chamamos a função de checarSeAindaHaPalavras, enviando a essa lista como parâmetro
def lerArquivoComPalavras():
    arq = open('jogo.txt', encoding='utf-8')
    palavras = arq.readlines()
    arq.close()
    checarSeAindaHaPalavras(palavras)

# PARA checarSeAindaHaPalavras, contamos quantas palavras 'P:' há na lista.
# Se esse número for igual a quantidade de palavras na variável, então sai do jogo
# Caso contrário, chamamos escolherPalavra, enviando-a a lista
def checarSeAindaHaPalavras(palavras):
    contador = 0
    for i in range(len(palavras)):
        palavraDisponibilizada = palavras[i]
        if 'P:' in palavraDisponibilizada:
            contador += 1
    if(contador == len(palavrasUsadas)):
        print(BLUE + 'Sinto muito. Acabaram-se as palavras.\U0001F61F' + RESET)
        time.sleep(3)
        sys.exit()
    escolherPalavra(palavras)

# PARA escolherPalavra, usamos o random na lista para sorteio. 
# Enquanto tiver 'D:' na palavra e enquanto estiver na lista palavrasUsadas, continua sorteando
# Quando encontrar a palavra, chamamos a função acharDicas com a lista e a palavra 
def escolherPalavra(palavras):
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

# PARA guardarDicas, guardamos as palavras com 'D:' a partir do index da palavra sorteada recebido em um array de dicas
# Quando encontrar um 'P:', chamamos a função de guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas
def guardarDicas(palavras, index):
    k = index + 1
    while 'D:' in palavras[k]:
        dicas.append(palavras[k][2:].strip())
        k += 1
        if(k == len(palavras)): break                                   # Necessário para k não ficar out of range caso a palavra sorteada tenha sido a última da lista
    guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavras[index])

# PARA guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas, tiramos 'P:' e a '\n'
# Chamamos a função setUpTelaInicialDoJogo, enviando-a a palavra tratada
def guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavraBruta):
    palavra = palavraBruta[2:].strip()
    palavrasUsadas.append(palavra)
    setUpTelaInicialDoJogo(palavra)

# PARA setUpTelaInicialDoJogo, começamos "dando início ao cronômetro", salvando o tempo no array de tempos iniciais
# Salvamos as letras originais da palavra em um array e o mesmo número de letras de '_ ' em outro
# Com cada letra, chamamos a função de trocarLetrasParaCriarArrLetrasParaEntrada
# No final, chamamos definirPalavraParaEntrada
def setUpTelaInicialDoJogo(palavra):
    controleDeTempoInicial.append(time.time())
    for i in range(len(palavra)):
        arrLetrasParaTela.append(palavra[i].upper())
        trocarLetrasParaCriarArrLetrasParaEntrada(palavra[i].upper())
        codigo.append('_ ')
    definirPalavraParaEntrada()

# PARA trocarLetrasParaCriarArrLetrasParaEntrada passamos pela matriz e, 
# se alguma letra da palavra sorteada for acentuada, trocamos pela letra na posição 0 daquela linha
# Salvamos as letras "tratadas" em um array
def trocarLetrasParaCriarArrLetrasParaEntrada(letra):
    for linha in range(len(matrizDeTroca)):
        for coluna in range(len(matrizDeTroca[linha])):
            if letra == matrizDeTroca[linha][coluna]:
                    letra = matrizDeTroca[linha][0]
    arrLetrasParaEntrada.append(letra)

# PARA definirPalavraParaEntrada, juntamos as letras do array com letras sem acentos. 
# Chamamos a função desenharTelaInicialDoJogo enviando a nova palavra (palavra sorteada sem acentos)
def definirPalavraParaEntrada():
    novaPalavra = ''.join(arrLetrasParaEntrada)
    desenharTelaInicialDoJogo(novaPalavra)

# PARA desenharTelaInicialDoJogo, precisamos chamar função de sortearDica para sortear a dica inicial, 
# Mostrar recados existentes, listas de letras erradas, o array codigo, com _ _ _s, e as dicas já existentes (que deve ser apenas uma)
# Por ser a tela inicial, os recados e letras erradas devem estar vazios, mas o colocamos para manter sempre o mesmo espaço entre as linhas
# Ao fim, chamamos a função jogo, enviando a nova palavra
def desenharTelaInicialDoJogo(palavra):
    sortearDica()
    mostrarRecadosNaTela()
    mostrarListaDeLetrasErradas()
    for l in range(len(codigo)):
        if(l == len(codigo) - 1): print(codigo[l])
        else: print(f'{codigo[l]}', end='')
    mostrarDicasNaTela()
    jogar(palavra)

# PARA sortearDica, sorteamos um número aleatório de 0 a tamanho do array - 1. Esse vai ser o índice da dica na lista. 
# Usamos o .pop() para alterar o array de dicas, tirando a dica já sorteada, e guardando-a no array de dicas sorteadas
def sortearDica():
    indexDasDicas = len(dicas) - 1
    indexSorteado = random.randint(0, indexDasDicas)
    dicasSorteadas.append(f'Dica: {dicas.pop(indexSorteado)}')

# PARA mostrarDicasNaTela, percorremos o array com um for dando print nas dicas, apenas se o array não estiver vazio
def mostrarDicasNaTela():
    if(len(dicasSorteadas) != 0):
        for i in range(len(dicasSorteadas)):
            print(dicasSorteadas[i])

# PARA jogar, pegamos o tempo da jogada para chamar a função controlarTempo() e ver a duração do jogo até agora (timer)
# Enquanto o array com vidas tiver o tamanho menor que 7 e o timer for menor que a duração, nós vamos
# 1. Pedir uma ação para o usuário 2. Gravar mais uma vez o tempo da rodada para a duração 3. Chamar a função de setUpParaRedesenharTela
# Quando sair do while, chamamos a função de definirDerrota com o timer como parâmetro
def jogar(palavra):
    timer = controlarTempo(time.time())
    while(len(vidas) < 7 and timer < duracao):
        entrada = pedirAcaoDoJogador(palavra)
        timer = controlarTempo(time.time())
        setUpParaRedesenharTela(entrada)
    definirDerrota(timer)

# PARA pedirAcaoDoJogador, validamos uma entrada (input) chamando a função validarEntrada, enviando a palavra sorteada sem acentos como parâmetro
# Se a entrada validada for um a str 'DICA', chamamos a função checarSeAindaHáDicasParaEntregar
# Se for a entrada, depois de transformada em entrada sem acentos, for igual a palavra, depois de transformada em palavra sem acento, chamamos definirVitoria() 
# Se for outra opção, chamamos a função checarSeLetraJaFoiUsada
# Independente do que for, a função retorna a entrada validada, a qual será guardada em uma variável na função jogar para que essa possa envia-la como parâmetro para setUpParaRedesenharTela
def pedirAcaoDoJogador(palavra):
    entrada = validarEntrada(palavra)
    if(entrada == 'DICA'): checarSeAindaHáDicasParaEntregar()
    elif(entrada == palavra): definirVitoria()
    else: checarSeLetraJaFoiUsada(entrada)
    return entrada

# PARA validarEntrada, o usuário pede input do
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
    mensagem = 'Você já usou todas as suas dicas'
    if (len(dicas) != 0): 
        tirarVida() # FUNÇÃO PARA TIRAR VIDA
        sortearDica() 
        mostrarDicasNaTela()
    else: 
        addAvisoDeDicasJaUsadas = True
        for i in range(len(dicasSorteadas)):
            if(dicasSorteadas[i] == mensagem):
                addAvisoDeDicasJaUsadas = False
                break
        if(addAvisoDeDicasJaUsadas):
            dicasSorteadas.append(mensagem)

def tirarVida():
    vidas.append(0)

def checarSeLetraJaFoiUsada(entrada):
    adicionaLetraJaUsada = True
    if (len(letrasUsadas) == 0):
        letrasUsadas.append(entrada)
        adicionaLetraJaUsada = False
    else:
        for i in range(len(letrasUsadas)):
            if(letrasUsadas[i] == entrada): 
                adicionaLetraJaUsada = False
                if(len(recados) != 0): recados[0] = (f'A letra {entrada} já foi usada')
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
        tirarVida() # FUNÇÃO PARA TIRAR VIDA

def setUpParaRedesenharTela(entrada): 
    os.system('cls' if os.name == 'nt' else 'clear')
    for j in range(len(arrLetrasParaTela)):
        if(arrLetrasParaEntrada[j] == entrada):
            codigo[j] = arrLetrasParaTela[j]
    redesenharTela()
    if(len(recados) != 0): recados[0] = ''

def redesenharTela(): 
    mostrarRecadosNaTela()
    mostrarListaDeLetrasErradas()
    mostrarCodigoAtualizado()
    mostrarDicasNaTela()
    checarSeCodigoFoiResolvido()

def mostrarRecadosNaTela():
    if(len(recados) != 0): print(recados[0])

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
    duracao = round(agora - controleDeTempoInicial[index])
    return duracao

def definirVitoria():
    mensagem = f'{GREEN}Parabéns, você ganhou!{RESET}\U0001F601'
    resultados.append(1)
    print(mensagem, '\n')
    desenharTelaDeFimDeJogo()

def definirDerrota(timer):
    resultados.append(0)
    resposta = ''.join(arrLetrasParaTela)
    if(timer > duracao): mensagem = f'{RED}Sinto muito, o tempo acabou.{RESET} A palavra era {resposta}.\U0001F61E'
    else: mensagem = f'{RED}Sinto muito, as vidas acabaram.{RESET} A palavra era {resposta}.\U0001F61E'
    print(mensagem, '\n')
    desenharTelaDeFimDeJogo()

def desenharTelaDeFimDeJogo():
    controleDeTempoFinal.append(time.time())
    for i in range(len(palavrasUsadas)):
        mensagem = f'{i+1}ª rodada - {palavrasUsadas[i]} - {calcularTempoDaRodada(i)}'
        if(resultados[i] == 1): print(GREEN + mensagem + RESET)
        else: print(RED + mensagem + RESET)
    decisaoDoUsuarioParaFimDeJogo()

def calcularTempoDaRodada(i):
    duracao = controleDeTempoFinal[i] - controleDeTempoInicial[i]
    mins = round(duracao / 60)
    secs = round(duracao % 60)
    return f'{mins:02d}:{secs:02d}'
    
def decisaoDoUsuarioParaFimDeJogo():
    time.sleep(1)
    novoJogo = validarNovoJogo()
    if(novoJogo == 'Y'): fazerSetUpDoJogo() 
    else: sys.exit()

def validarNovoJogo():
    novoJogo = input('Deseja jogar novamente? [Y/n]: ').upper()
    while(novoJogo != 'Y' and novoJogo != 'N'):
        novoJogo = input('Código inválido. Digite Y para jogar novamente ou N para sair: ').upper()
    return novoJogo