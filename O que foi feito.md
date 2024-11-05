
Fiz o mapa do que iria seguir:

exemplo: bot whatsapp, o bot vai abrir e mandar mensagem para todos que me eviar algo

em seguida procurei as bibliotecas que irei utilizar, verificando os documentos oficiais da biblioteca, as mais comuns para bot's e automações é selenium e pyautogui

estou utilizando o vscode para compilar os codigos por sua interatividade e facilidade de uso

criei uma pasta do projeto, abrir o vscode inserir a pasta(do projeto) no vscode, em seguida criei um arquivo .py, logo a pós abri o terminal do vscode (verifique se o terminal está na pasta do projeto) insira o seguinte comando, [ python -m venv .venv] o primeiro venv é do nome que vc quer chamar, eu chamo de venv pq é uma venv.

o que é uma venv?

ele é nada mais que um ambiente virtual, é como se vc tivesse uma área só para executar aquele projeto.

que agora será o proximo passo, irá inserir o seguinte comando [ source ./venv/bin/activate ] caso esteja no windows o source é [ (nome da venv/Scripts/activate)]

pronto venv ativada, vamos continuar

iremos ir no terminal novamente e instalar o selenium [ pip install selenium]

em seguida importei as bibliotecas do selenium:
[ from selenium import webdriver]
[from selenium.webdriver.common.keys import Keys]
[from selenium.webdriver.common.by import By]
[from time import sleep]
[from selenium.webdriver.chrome.options import Options ]

fiz a estrutura inicial que seria abrir o google na pagina do whatsapp
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
sleep(60)
driver.close()

