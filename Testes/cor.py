import pyautogui
from time import sleep
sleep(5)

x,y = pyautogui.position()
print("""posição x: {}
      posição y: {}""".format(x, y))