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

Programa
git add [nome do arquivo] ou git add . (se for todos) 
git stage -> para ver quais arquivos estamos enviando
git commit -m "mensagem explicativa da mudança"
git branch -M "nome da branch com a mudança que vai fazer"
git remote add [nome da branch] git@github.com:freitasgst/jogodaforca.git
git push -u [nome da branch]