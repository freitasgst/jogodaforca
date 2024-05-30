todasPalavras = "advogado afta algarismo almanaque alquimia amendoim amnésia amplificar ampulheta ansioso aplaudir asterisco barulhento basquetebol beneficente berimbau bicarbonato bugiganga bumerangue burocracia caatinga cacto calibrado camuflagem candelabro catalisador cérebro cicatriz cleptomaníaco coincidência companhia consciente crepúsculo cronologia destruído diretriz dobradiça ecossistema embaixador empecilho entretido entrevista enxaqueca enxerido escombro espinafre estetoscópio exceção excêntrico excepcional flexível frustrado gargantilha glândula gnomo grampeador hamster helicóptero hemisfério herdeiro idolatrada influência insignificância interruptor invertebrado iogurte lantejoula licenciado losango madrasta magnético marimbondo mesclar meteorologia microfone microscópio milionário mordaz necrosar oscilação paralisado pedágio perturbar piripaque pneumonia poliomielite presságio privilégio prodígio psicanálise quadriciclo quermesse quinquilharia reciclar reflorescer reivindicar retrovisor ritmo seborreia sensatez serelepe serpentina simplório sobrevivente supérfluo suscetível termômetro travesseiro trilogia universidade universo vangloriar ventilador xilindró xadrez ziguezague zodíaco zumbido"
palavras = todasPalavras.split(' ')

arq = open('/media/angte/DADOS/Gabi/Estudos de Tecnologia/Cursos 2024/FATEC/ILP200 - Programação I/1_Provas/jogo.txt', 'w')
arqParaTeste = open('/media/angte/DADOS/Gabi/Estudos de Tecnologia/Cursos 2024/FATEC/ILP200 - Programação I/1_Provas/jogoParaTestes.txt', 'w')

for i in range(len(palavras)):
    arq.write(f'P:{palavras[i]}\n')

for i in range(5):
    arqParaTeste.write(f'P:{palavras[i]}\n')

arq.close()
arqParaTeste.close()