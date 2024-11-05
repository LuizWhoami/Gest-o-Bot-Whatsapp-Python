from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import requests
from selenium.webdriver.common.action_chains import ActionChains


#API 
agent = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'}

#CHAVE 
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/C0JCTUr8erzNuCmSF0KrNCJD68hJv8xg" ,  headers=agent)
sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()




dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')
sleep(10)

def bot():
    try:
        
        bolinha = driver.find_element(By.CLASS_NAME,'x7h3shv')
        bolinha = driver.find_elements(By.CLASS_NAME,'x7h3shv')
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.driver(ActionChains)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        sleep(1)
        
        
        contato = driver.find_element(By.XPATH, contato_cliente)
        contato_final = contato.text
        print(contato_final)
        sleep(2)
        
        #msg cliente
        
        msg = driver.find_elements(By.CLASS_NAME, msg_cliente)
        msg = [e.text for e in msg]
        men = msg[-1]
        print(men)
        sleep(1
        
        usuario = ['binckplink@gmail.com']
        
        #envio
        resposta = requests.get('http://localhost/bot_chat1/index.php?', params={'msg': men, 'telefone': contato_final, 'usuario': usuario})
        resposta = resposta.text
        texto = driver.find_element(By.XPATH, caixa_msg)
        texto.click()
        sleep(1)
        texto.send_keys(resposta, Keys.ENTER)

        #fechando contato
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        print('Procurando mensagens')
        #entao vou tentar isso aqui
while True:
    bot()