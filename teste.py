import pyautogui as auto
import time

# hotkey combina teclas de atalho
auto.hotkey('win','r')
time.sleep(0.5)
auto.write('chrome', interval=0.2)
auto.press('enter')
time.sleep(2)
auto.press('tab')
auto.press('enter')
time.sleep(2)
auto.write('www.uol.com.br')
auto.press('enter')
time.sleep(2)
auto.moveTo(x=791, y=478, duration=2)
auto.click()


