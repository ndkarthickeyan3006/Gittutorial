import pyautogui
import time

time.sleep(3)
#Mouse Opertion
#pyautogui.moveTo(100, 100, duration =1)

#pyautogui.click(100, 100)
#pyautogui.rightClick(100, 100)
#pyautogui.leftClick(100, 100)

#pyautogui.doubleClick(100, 100)

#pyautogui.dragTo(100, 100, duration =1)

pyautogui.scroll(-500) #Scroll up 500 units
time.sleep(3)
pyautogui.scroll(500) #Scroll down 500 units