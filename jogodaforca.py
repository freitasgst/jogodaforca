import funcoes, sys

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
    funcoes.fazerSetUpDoJogo()
else:
    sys.exit()
