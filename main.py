import pyautogui
from time import sleep

works = ["*work Покормить электрочервей", "*work Поиграть с Сербаном", "*работать Прополоть грядки Бриллы", \
          "*работать Помочь Алеку на пляже", "*работать Попасти суджидаро", "*работать Принести Вандеру семена"]

pyautogui.FAILSAFE = True

while True:
    pyautogui.moveTo(564, 180, duration=1)
    pyautogui.click()
    pyautogui.keyDown("shift")

    for i in range(1, 30):
        pyautogui.press("left")

    pyautogui.keyUp("shift")

    pyautogui.keyDown('command')
    pyautogui.keyDown('c')
    pyautogui.keyUp('command')
    pyautogui.keyUp('c')

    pyautogui.moveTo(160, 1877, duration=0.5)

    pyautogui.click()

    pyautogui.click(button='right')

    pyautogui.moveTo(183, 1863, duration=0.5)

    pyautogui.click()

    pyautogui.press("enter")
    sleep(3600)

#print(pyautogui.position())
