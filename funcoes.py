import random, time, sys, os, errorsService, animationPacman

RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

palavrasUsadas = []                        # onde vamos guardar as palavras usadas para que o jogador possa sempre ter palavras quando jogar novamente
dicas = []                                 # onde vamos guardar as dicas da rodada
dicasSorteadas = []                        # onde vamos guardar as dicas que ficam na tela
matrizDeTroca = [
    ['A', 'Á', 'À', 'Â', 'Ã'], 
    ['E', 'É', 'Ê'], 
    ['I', 'Í'], 
    ['O', 'Ó', 'Ò', 'Ô', 'Õ'], 
    ['U', 'Ú'], 
    ['C', 'Ç']
]
arrLetrasParaTela = []                     # array para mostrar a palavra gramaticamente correta na tela
arrLetrasParaEntrada = []                  # array para comparar entrada com palavra ignorando acentos e ç, ou seja, a palavra para a mecânica de jogo
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
    arq = open('jogo.txt', 'r', encoding='utf-8')
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
        print(CYAN + 'Sinto muito. Acabaram-se as palavras.\U0001F61F' + RESET)
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
    '''
    palavra = random.choice(palavras)
    checarSeJaFoiUsado = False
    for dado in palavrasUsadas:
        if (dado == palavra): 
            checarSeJaFoiUsado = True
            break
    while(palavra[0:2] == 'D:' or checarSeJaFoiUsado):
        palavra = random.choice(palavras)
        checarSeJaFoiUsado = False
        for dado in palavrasUsadas:
            if (dado == palavra): 
                checarSeJaFoiUsado = True
                break
    '''

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
    if len(dicas) == 0: dicas.append('Não existem dicas para essa palavra')
    guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavras[index])

# PARA guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas, tiramos 'P:' e a '\n'
# Chamamos a função setUpTelaInicialDoJogo, enviando-a a palavra tratada
def guardarPalavraQueSeraUsadaEmArrDePalavrasUsadas(palavraBruta):
    palavra = palavraBruta[2:].strip()
    palavrasUsadas.append(palavra)
    setUpTelaInicialDoJogo(palavra)

# PARA setUpTelaInicialDoJogo, iniciamos o cronômetro ao salvar o tempo no array de tempos iniciais
# Salvamos as letras originais da palavra em um array e o mesmo número de letras de '_ ' em outro, chamado código
# Com cada letra, chamamos a função de trocarLetrasParaCriarArrLetrasParaEntrada e no final, chamamos definirPalavraParaEntrada
def setUpTelaInicialDoJogo(palavra):
    controleDeTempoInicial.append(time.time())
    for i in range(len(palavra)):
        arrLetrasParaTela.append(palavra[i].upper())
        trocarLetrasParaCriarArrLetrasParaEntrada(palavra[i].upper())
        codigo.append('_ ')
    definirPalavraParaEntrada()

# PARA trocarLetrasParaCriarArrLetrasParaEntrada passamos pela matriz de troca e, se alguma letra da palavra sorteada for acentuada, trocamos pela letra na posição 0 daquela linha
# Salvamos as letras "tratadas" em um array. 
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

# PARA desenharTelaInicialDoJogo, precisamos sortear a dica inicial, e mostrar: o pacman com 7 vidas, recados existentes, lista de letras erradas, os _ _ _ _, e a dica inicial sorteada
# Por ser a tela inicial, os recados e as letras erradas devem estar vazios, mas o colocamos para manter sempre o mesmo espaço entre as linhas
# Ao fim, chamamos a função jogo, enviando a "palavra tratada"
def desenharTelaInicialDoJogo(palavra):
    sortearDica()
    errorsService.showResult(7, 0)
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
    if dicas[0] == 'Não existem dicas para essa palavra': 
        dicasSorteadas.append(CYAN + 'Não existem dicas para essa palavra' + RESET)
    else:
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
# 1. Pedir uma ação para o usuário 2. Gravar mais uma vez o tempo da rodada para a duração 3. Chamar a função de fazer set up para redesenhar a tela
# Quando sair do while, chamamos a função de definirDerrota com o timer como parâmetro
def jogar(palavra):
    timer = controlarTempo(time.time())                 # temos que criar a variável antes do while poder usá-la como condição
    while(len(vidas) < 7 and timer < duracao):     
        entrada = pedirAcaoDoJogador(palavra)
        timer = controlarTempo(time.time())
        fazerSetUpParaRedesenharTela(entrada)
    definirDerrota(timer)

# PARA pedirAcaoDoJogador, validamos a entrada (input) chamando a função validarEntrada, enviando a palavra sorteada sem acentos como parâmetro
# Se a entrada validada for a str 'DICA', ela vê se é uma palavra com dicas. Se sim, chamamos a função checarSeAindaHáDicasParaEntregar
# Se a entrada, depois de transformada em entrada sem acentos, for igual a palavra, depois de transformada em palavra sem acento, chamamos definirVitoria() 
# Se for outra opção, chamamos a função checarSeLetraJaFoiUsada
# Independente do que for, a função retorna a entrada validada, a qual será guardada em uma variável em jogar(), para que possa enviá-la como parâmetro para a nova tela (redesenhada pós ação do usuário)
def pedirAcaoDoJogador(palavra):
    entrada = validarEntrada(palavra)
    if(entrada == 'DICA'): 
        checaSeExistiamDicasParaAPalavraNoInicioDoJogo = True
        if(len(dicas) != 0 and dicas[0] == 'Não existem dicas para essa palavra'): checaSeExistiamDicasParaAPalavraNoInicioDoJogo = False
        if(checaSeExistiamDicasParaAPalavraNoInicioDoJogo): checarSeAindaHaDicasParaEntregar()
    elif(entrada == palavra): definirVitoria()
    else: checarSeLetraJaFoiUsada(entrada)
    return entrada

# PARA validarEntrada, primeiro nós trocamos os caracteres especiais caso existam. 
# Uma vez que ela está como ser usada em jogo, checamos se a entrada é um caractere, e não um digito; e, se for caractere, checamos se é uma letra, um pedido de dica ou um chute
# Esta função retorna a "nova entrada" (letra sem acento ou ç) para a função de pedir ação do jogador, que a usará para ver se ela está na palavra, se há dicas ou se o jogador acertou em seu chute
def validarEntrada(palavra):
    entrada = input('\nDigite uma letra ou peça por uma dica: ').upper()
    novaEntrada = trocarEntradaParaJogo(entrada)
    while(not entrada.isalpha() or (len(entrada) != 1 and (entrada != 'DICA' and novaEntrada != palavra))):
        if(len(entrada) == len(palavra) and (entrada != 'DICA' and novaEntrada != palavra)):                        # optamos por só tirar a vida dele caso ele digite algo do mesmo tamanho da palavra. Se não for esse o caso, não é um chute válido
            tirarVida()
            redesenharTela()
            print(CYAN + '\nPalavra errada, você perdeu uma vida.\U0001F61F' + RESET)
        entrada = input('\nEntrada inválida, digite apenas uma letra ou peça por uma dica ou escreva a palavra correta: ').upper()
        novaEntrada = trocarEntradaParaJogo(entrada)
    return novaEntrada

# PARA trocarEntradaParaJogo, percorremos pela entrada (str). A cada iteração desse for, guardamos a letra da entrada em um array temporário e percorremos pela matriz procurando se alguma das letras da entrada consta nele
# Se sim, mandamos para o array temporário a letra sem o acento ou cedilha. Se não, continua como a letra original da entrada, já salva lá
# Essa função retorna para validarEntrada uma str da palavra nova sem acentos ou cedilha, ao dar juntando com '' os elementos do array temporário
def trocarEntradaParaJogo(entrada):
    arrTemporarioParaNovaEntrada = ['' for aux in range(len(entrada))]              # 'entrada' nem sempre é uma letra, mas pode ser um chute
    for i in range(len(entrada)):
        arrTemporarioParaNovaEntrada[i] = entrada[i]
        for linha in range(len(matrizDeTroca)):
            for coluna in range(len(matrizDeTroca[linha])):
                if entrada[i] == matrizDeTroca[linha][coluna]:
                    arrTemporarioParaNovaEntrada[i] = matrizDeTroca[linha][0]
    return ''.join(arrTemporarioParaNovaEntrada)

# PARA checarSeAindaHaDicasParaEntregar, checamos se a lista de dicas está "zerada". 
# Se não estiver, tira a vida, sorteia uma nova dica e a mostra na tela. Se estiver, caso não tenha a mensagem de falta de ficas no array ainda, a adiciona
def checarSeAindaHaDicasParaEntregar():
    mensagem = CYAN + 'Você já usou todas as suas dicas' + RESET
    if (len(dicas) != 0): 
        tirarVida() 
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

# PARA tirarVida, adicionamos um elemento no array de vidas e limpamos o terminal para chamar a animação do pacman
def tirarVida():
    vidas.append(0)
    os.system('cls' if os.name == 'nt' else 'clear')                # usa o módulo os para checar qual o sistema operacional. Por exemplo: se for Windows, o comando é 'cls'; se for Linux, é 'clear'
    errorsService.showResult(7 - len(vidas), len(vidas))            # parâmetros: quantidade de vidas existentes (total - tamanho do array) e de erros (tamanho do array)
    time.sleep(1)

# PARA checarSeLetraJaFoiUsada, checamos o array de letras usadas com uma booleana de controle. Se ele estiver vazio, adicionamos a entrada direto e mudamos a boolean para False, para não anexar duas vezes. 
# Se não estiver vazio, passamos por ele com for e, se o elemento de alguma das iterações for igual à entrada, mudamos a boolean de controle para false. 
# Se após essas checagens a boolean ainda for True, gravamos a mensagem de letra repetida no array de recados. De qualquer modo, chamamos a função que define se a entrada existe na palavra
def checarSeLetraJaFoiUsada(entrada):
    adicionaLetraJaUsada = True
    if (len(letrasUsadas) == 0):
        letrasUsadas.append(entrada)
        adicionaLetraJaUsada = False
    else:
        for i in range(len(letrasUsadas)):
            if(letrasUsadas[i] == entrada): 
                adicionaLetraJaUsada = False
                if(len(recados) != 0): recados[0] = (CYAN + f'A letra {entrada} já foi usada' + RESET)
                break
    if adicionaLetraJaUsada: letrasUsadas.append(entrada)
    definirSeEntradaExisteNaPalavra(entrada)

# PARA definirSeEntradaExisteNaPalavra, criamos uma boolean de controle como True. Se a entrada for igual a qualquer elemento do array de letras já tratadas sem acento ou cedilha, então é porque o jogador acertou e mudamos a boolean para False e saímos do loop.
# Se a boolean for True ainda, chamamos a função de adicionar entrada no array de letras erradas
def definirSeEntradaExisteNaPalavra(entrada):
    entradaErrada = True
    for i in range(len(arrLetrasParaEntrada)):
        if(entrada == arrLetrasParaEntrada[i]):
            entradaErrada = False
            break
    if entradaErrada: adicionarEntradaNoArrayDeLetrasErradas(entrada)

# PARA adicionarEntradaNoArrayDeLetrasErradas, verificamos se a entrada já está no array de letras erradas com uma boolean de controle. 
# Se não encontrar a entrada na lista de letras erradas, a adicionamos e chamamos a função de tirar vida
def adicionarEntradaNoArrayDeLetrasErradas(entrada):
    adicionaLetraErrada = True
    if(len(letrasErradas) != 0): 
        for i in range(len(letrasErradas)):
            if(entrada == letrasErradas[i]): 
                adicionaLetraErrada = False
                break
    if adicionaLetraErrada: 
        letrasErradas.append(entrada)
        tirarVida()

# PARA fazerSetUpParaRedesenharTela, primeiro limpamos o terminal, depois mostramos o pacman na posição parada com o feedback de vidas e erros e redesenhamos o código na tela
# Com um for que roda a quantidade de letras que há na tela (ou na entrada, ou no código), vemos se a entrada é igual a alguma das letras no array de letras para conferir com a entrada (sem acentou ou cedilha). Se for, '_ ' naquela mesma posição no código e substituída pela letra na mesma posição no array de letras para a tela
# Depois disso redesenhamos a tela e limpamos o array de recados
def fazerSetUpParaRedesenharTela(entrada): 
    os.system('cls' if os.name == 'nt' else 'clear')
    animationPacman.showPositonPacman(7 - len(vidas), len(vidas))
    for j in range(len(arrLetrasParaTela)):
        if(arrLetrasParaEntrada[j] == entrada):
            codigo[j] = arrLetrasParaTela[j]
    redesenharTela()
    if(len(recados) != 0): recados[0] = ''

# PARA redesenharTela, mostramos: os recados, a lista de letras erradas, o código atualizado e as dicas já "abertas" na tela
# Por fim, chamamos a função de checar se o código foi resolvido
def redesenharTela(): 
    mostrarRecadosNaTela()
    mostrarListaDeLetrasErradas()
    mostrarCodigoAtualizado()
    mostrarDicasNaTela()
    checarSeCodigoFoiResolvido()

# PARA mostrarRecadosNaTela, mostramos o primeiro elemento, uma vez que os recados se sobreescrevem
def mostrarRecadosNaTela():
    if(len(recados) != 0): print(recados[0])

# PARA mostrarListaDeLetrasErradas, percorremos pelo array de letras usadas quando não está vazio e colocamos cada letra uma ao lado da outra, até a última. 
def mostrarListaDeLetrasErradas():
    if(len(letrasErradas) != 0):
        print('Letras erradas: ', end = '')
        for k in range(len(letrasErradas)):
            if(k == len(letrasErradas) - 1): 
                print(f'{letrasErradas[k]}')
            else: 
                print(f'{letrasErradas[k]}, ', end='')

# PARA mostrarCodigoAtualizado, damos print em cada elemento um ao lado do outro
def mostrarCodigoAtualizado():
    for l in range(len(codigo)):
        if(l == len(codigo) - 1): print(codigo[l])
        else: print(f'{codigo[l]}', end='')

# PARA checarSeCodigoFoiResolvido, usamos uma boolean para controle. Percorremos o array do código e, caso ainda haja elementos '_ ', é porque ainda há letras para decifrar e mudamos a boolean de True para False. 
# Caso a boolean ainda fique como True após esse loop, definimos a Vitoria
def checarSeCodigoFoiResolvido():
    palavraDecifrada = True
    for m in range(len(codigo)):
        if(codigo[m] == '_ '): palavraDecifrada = False
    if palavraDecifrada : definirVitoria()

# PARA controlarTempo, recebemos o tempo atual após cada ação do usuário e retornamos para a função jogar a o tempo decorrido até então, para ser usado como: 
# validador do while e para ser enviado como parâmetro para a tela de derrota, caso precise
def controlarTempo(agora): 
    index = len(controleDeTempoInicial) - 1
    duracao = round(agora - controleDeTempoInicial[index])
    return duracao

# PARA definirVitoria, limpamos o terminal, salvamos 1 no array de resultados, mostramos mensagem de vitória e chamamos a função de desenhar a tela final do jogo
def definirVitoria():
    os.system('cls' if os.name == 'nt' else 'clear')
    mensagem = f'{GREEN}Parabéns, você ganhou!{RESET}\U0001F601'
    resultados.append(1)
    print(mensagem, '\n')
    animationPacman.showWin()
    desenharTelaDeFimDeJogo()

# PARA definirDerrota, limpamos o terminal, salvamos 0 no array de resultados e vemos por que o jogador perdeu
# Se por tempo (parâmetro de timer recebido superou a duração estabelecida para o jogo), mostramos uma mensagem de tempo. Se não, de que as vidas acabaram. Em ambas as mensagem, mostramos a resposta. 
# Mostramos imagem de game over e chamamos a função de desenhar tela de fim de jogo
def definirDerrota(timer):
    os.system('cls' if os.name == 'nt' else 'clear')
    resultados.append(0)
    resposta = ''.join(arrLetrasParaTela)
    if(timer > duracao):
        mensagem = f'{RED}Sinto muito, o tempo acabou.{RESET} A palavra era {resposta.upper()}.\U0001F61E'
    else: 
        mensagem = f'{RED}Sinto muito, as vidas acabaram.{RESET} A palavra era {resposta.upper()}.\U0001F61E'
    print(mensagem, '\n')
    time.sleep(1) 
    animationPacman.showGameOver()
    desenharTelaDeFimDeJogo()

# PARA desenharTelaDeFimDeJogo, salvamos o tempo de agora no array de tempos finais. 
# Entramos em um loop que passa pelas listas de palavras usadas, criando uma tela com os resultados das rodadas desse jogo: nº da rodada, resposta e chamamos para calcular tempo de cada uma dessas rodadas
# Usamos os 1s e 0s do array de resultados para escrever a linha em verde ou vermelho no terminal. Pedimos pela decisão do jogador de continuar ou não. 
def desenharTelaDeFimDeJogo():
    controleDeTempoFinal.append(time.time())
    for i in range(len(palavrasUsadas)):
        mensagem = f'{i+1}ª rodada - {palavrasUsadas[i]} - {calcularTempoDaRodada(i)}'
        if(resultados[i] == 1): print(GREEN + mensagem + RESET)
        else: print(RED + mensagem + RESET)
    pedirDecisaoDoUsuarioParaFimDeJogo()

# PARA calcularTempoDaRodada, subtraímos o tempo inicial do final daquela posição. O arredondamento para inteiros da divisão desse número por 60 são os minutos; o resto, os segundos. Damos o return do cronômetro mm:ss.
def calcularTempoDaRodada(i):
    duracao = controleDeTempoFinal[i] - controleDeTempoInicial[i]
    mins = round(duracao / 60)
    secs = round(duracao % 60)
    return f'{mins:02d}:{secs:02d}'

# PARA pedirDecisaoDoUsuarioParaFimDeJogo, esperamos um pouco e então chamamos uma função que irá validar a entrada do jogador. 
# Se ele digitou que sim, chamamos função de fazer setup do início do jogo. Se digitou que não, agradecemos, esperamos um pouco, e saímos do terminal pelo sistema operacional. 
def pedirDecisaoDoUsuarioParaFimDeJogo():
    time.sleep(1)
    novoJogo = validarNovoJogo()
    if(novoJogo == 'Y'): fazerSetUpDoJogo() 
    else:
        print("Obrigado pela participação. Até logo!")
        time.sleep(2)
        sys.exit()

# PARA validarNovoJogo, perguntamos se ele deseja jogar novamente até que a entrada dele seja sim ou não
def validarNovoJogo():
    novoJogo = input('Deseja jogar novamente? [Y/n]: ').upper()
    while(novoJogo != 'Y' and novoJogo != 'N'):
        novoJogo = input('Código inválido. Digite Y para jogar novamente ou N para sair: ').upper()
    return novoJogo

#######################################################################################