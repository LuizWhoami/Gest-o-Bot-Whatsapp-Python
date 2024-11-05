from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import pyautogui
import pandas as pd
import pyperclip
import csv
import sqlite3

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')
sleep(3)
pyautogui.click(1188, 269)
sleep(30)

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/p').click()
nome12 = ['Dvison']
pyautogui.write(nome12[0])
pyautogui.hotkey('Enter')
def pergunta():
    pyautogui.write("*#### -- BARBEARIA LS -- ####*")
    pyautogui.hotkey('Shift', 'Enter')
    pyautogui.write("Ola *{}*".format(nome12[0]))
    pyautogui.hotkey('Shift', 'Enter')
    pyautogui.write("*(1)* Armazenar  lucro")
    pyautogui.hotkey('Shift', 'Enter')
    pyautogui.write("*(4)* Verificar lucro")
    pyautogui.hotkey('Shift', 'Enter')
    pyautogui.write("*#### -- BARBEARIA LS -- ####*")
    pyautogui.hotkey('Enter')
pergunta()

sleep(2)
def bot1():
    try:
        msg = driver.find_elements(By.CLASS_NAME, "_akbu")
        msg = [e.text for e in msg]
        men = msg[-1]
        print(men)
        df = pd.DataFrame({men})
        df.to_csv('salvo.csv', index=False)
        with open('salvo.csv', 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for row in leitor:
                sleep(2)
            if row == ['1']:
                pyautogui.write("*Informe* *Nome*")
                pyautogui.hotkey('shift', 'Enter')
                pyautogui.write('*3* - Dvison')
                pyautogui.hotkey('Enter')
                sleep(2)
            if row == ['3']:
                pyautogui.write('*Informe o valor*')
                pyautogui.hotkey('Enter')
            if row == ['25']:
                dv = ['Dvison']
                valor25 = ['25']
                for conn1 in range(1):
                    conn1 = sqlite3.connect("gestao.db")
                    cursor1 = conn1.cursor()
                    cursor1.executemany("INSERT INTO clientes (nome, valor) VALUES (?,?)", zip(dv, valor25))
                    conn1.commit()
                    conn1.close()
                    pyautogui.write('_armazenado_')
                    pyautogui.hotkey('Enter')
                    sleep(4)
                    pergunta()
            if row == ['10']:
                dv = ['Dvison']
                valor10 = ['10']
                for conn1 in range(1):
                    conn1 = sqlite3.connect("gestao.db")
                    cursor1 = conn1.cursor()
                    cursor1.executemany("INSERT INTO clientes (nome, valor) VALUES (?,?)", zip(dv, valor10))
                    conn1.commit()
                    conn1.close()
                    pyautogui.write('_armazenado_')
                    pyautogui.hotkey('Enter')
                    sleep(4)
                    pergunta()
            if row == ['15']:
                dv = ['Dvison']
                valor15 = ['15']
                for conn1 in range(1):
                    conn1 = sqlite3.connect("gestao.db")
                    cursor1 = conn1.cursor()
                    cursor1.executemany("INSERT INTO clientes (nome, valor) VALUES (?,?)", zip(dv, valor15))
                    conn1.commit()
                    conn1.close()
                    pyautogui.write('_armazenado_')
                    pyautogui.hotkey('Enter')
                    sleep(4)
                    pergunta()
            if row == ['35']:
                dv = ['Dvison']
                valor35 = ['35']
                for conn1 in range(1):
                    conn1 = sqlite3.connect("gestao.db")
                    cursor1 = conn1.cursor()
                    cursor1.executemany("INSERT INTO clientes (nome, valor) VALUES (?,?)", zip(dv, valor35))
                    conn1.commit()
                    conn1.close()
                    pyautogui.write('_armazenado_')
                    pyautogui.hotkey('Enter')
                    sleep(4)
                    pergunta()
            if row == ['40']:
                dv = ['Dvison']
                valor40 = ['40']
                for conn1 in range(1):
                    conn1 = sqlite3.connect("gestao.db")
                    cursor1 = conn1.cursor()
                    cursor1.executemany("INSERT INTO clientes (nome, valor) VALUES (?,?)", zip(dv, valor40))
                    conn1.commit()
                    conn1.close()
                    pyautogui.write('_armazenado_')
                    pyautogui.hotkey('Enter')
                    sleep(4)
                    pergunta()
            if row == ['4']:
                for conn in range(1):
                    conn = sqlite3.connect('gestao.db')
                    df = pd.read_sql_query("SELECT * FROM clientes", conn)
                    df.to_string('teste.csv', index=False)
                    conn.close()
                    pyperclip.copy(df)
                    pyautogui.hotkey('Ctrl', 'v')
                    pyautogui.hotkey('Enter')
    except:
        print('Procurando')
while True:
    bot1()