import funcoes, sys                         # importa nosso arquivo de funções e o módulo do python sys

CYAN  = "\033[1;36m"
RESET = "\033[0;0m"

# Desenho da tela inicial
print(f"\n{CYAN}Jogo da Forca{RESET} \n")

print("Nome: Cibele Gameleira - RA: 1680972411009 \nNome: Gabriela Freitas - RA: 1680972411001 \nNome: Letícia Nascimento - RA: 1680972411037\n")

print("Jogo[X] \nDicas[X] \nControle de tempo[X] \n")

print("Bem vindo(a) a um jogo da forca inovador. Esteja preparado(a) para esse desafio!")

print("Antes de jogar, você precisa saber de algumas instruções: \n")
print("- Você terá 7 vidas e 3 minutos para acertar cada palavra;")
print("- Você pode pedir dicas sobre as palavras, mas atenção: elas custam uma vida;")
print("- Toda palavra tem uma ou mais dicas disponíveis;")
print("- Se você descobrir a palavra, pode digitar ela inteira ao invés de só uma letra;")
print("- Mas cuidado: se seu palpite estiver incorreto, você perde uma vida")
print("- Se você digitar a letra errada, perde uma vida;")
print("- Se suas vidas ou o tempo do jogo acabar antes de você adivinhar a palavra, você perde a rodada;")
print("- Se você acertar a palavra antes do tempo do jogo acabar, você ganha a rodada;")
print("- Perdendo ou ganhando, você sempre pode jogar e se divertir novamente.\n")

# Pede ação do jogador, para que a contagem de tempo comece apenas quando o jogador estiver preparado
inicio = input('Pronto para começar? [Y/n]: ').upper()
while(inicio != 'Y' and inicio != 'N'):
    inicio = input('Comando inválido. Digite Y para começar ou N para sair do jogo: ').upper()

if(inicio == 'Y'):
    funcoes.fazerSetUpDoJogo()
else:
    sys.exit()
