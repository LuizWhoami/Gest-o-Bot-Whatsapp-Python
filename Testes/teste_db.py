import sqlite3
from time import sleep
import pandas as pd
import pyautogui
import csv
import pyperclip
sleep(5)

#x, y = pyautogui.position()
#print("""x = {}
#y = {}""".format(x, y))

#sleep(102)
conn = sqlite3.connect('gestao.db')
df = pd.read_sql_query("SELECT * FROM clientes", conn)
df.to_string('teste.csv', index=False)
conn.close()

cop = pyperclip.copy(df)
pyautogui.hotkey('Ctrl', 'v')
