# Jogo da Forca

## Preparar a pasta

1. Instalar o git -> Windows: http://git-scm.com/download/win
2. Instalar o github cli -> Windows: npm install gh
3. No terminal: gh auth login e seguir os passos que ele segue
3. Clonar o repositório na sua máquina
    1. Clicar no botão verde e baixar o .zip, ou 
    2. no terminal com git clone https://github.com/freitasgst/jogodaforca.git
3. Abrir a pasta no VSCode e, no terminal do VSCode:
    1. git config --global user.name "seu nome de usuário do github"
    2. git config --global user.email "seu email no github"

Se quiserem seguir tutorial: https://www.youtube.com/watch?v=_hZf1teRFNg&ab_channel=DevSuperior

## Workflow

### Criar uma branch
Para adicionarmos funções novas

1. git pull origin main
2. git branch [nome da função, da feature nova, curto]
3. git checkout [nome da branch que vai trabalhar]
4. Trabalhar aqui nesse branch

### Alterando o projeto
O trabalho em si

5. git add [nome do arquivo] ou git add . (se for todos) 
    1. git status -> para ver quais arquivos estamos enviando (tem que estar vermelho antes de add e verde depois)
6. git commit -m "mensagem explicativa da mudança, mais detalhada"
    1. git status -> não estaria mais lá
7. git push origin [nome da branch]

### Criar um pull request
Qualquer código de uma deve ser testado pelas outras duas

8. ir na pasta do trabalho lá no github, vai ter um botão verde de create pull request
9. comparar o código, dá para comentar nas linhas
    #### Testes
    Antes de aceitar o pull request, devemos testar!
    1. no VSCode: git pull
    2. Testar querendo quebrar o negócio mesmo
10. aceitar apertando merge
11. deletar o branch

Mais: 
https://www.youtube.com/playlist?list=PLcoYAcR89n-qbO7YAVj5S0alABLis_QVU

https://docs.github.com/en/get-started/using-github/github-flow

### Para formular as funções
## Regras
1. Nomes óbvios e descritivos em camelCase
2. Devem ser pequenas (o ideal seria, no máximo, de 4 linhas)
3. Deve fazer apenas uma coisa
4. Não deve ser possível retirar qualquer linha da função e colocá-la em outra sem ser apenas uma reformulação
5. Obviamente transparente
6. Deve contar uma história
7. Cada função deve levar você à próxima em uma “ordem atraente”
8. Ler o código de cima para baixo
9. Quanto aos parâmetros:
    a. Quanto à quantidade:
        * 0 → ideal
        * 1 e 2 → ok
        * 3 → evitar situações se possível
        * 4 + → não
    b. Evitar parâmetros lógicos
10. Evitar repetições

## Descrições
# Exemplo
“TO RenderPageWithSetupsAndTeardowns, verificamos se a página é de teste, se for, incluímos setups e teardowns. Em ambos os casos, exibimos a página em HTML” (pág. 36)
Com base no livro Código Limpo, do Robert C. Martin

TO → PARA

### Canal de organização
Usaremos o Trello