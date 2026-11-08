import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("step1:Open the chrome browser...")
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

print("step2:Go to the website...")
pyautogui.hotkey('ctrl', 't', interval=0.1)
time.sleep(1)
pyautogui.write('https://www.accuweather.com/en/in/hosur-sarjapur-road-layout/3352280/hourly-weather-forecast/3352280', interval=0.1)
time.sleep(1)
pyautogui.press('enter')

print("Step 3: Copy the full data of the website...")

pyautogui.click(700, 400)
time.sleep(2)

pyautogui.hotkey('ctrl', 'a', interval=0.1)
time.sleep(1)

pyautogui.hotkey('ctrl', 'c', inteval=0.1)
time.sleep(1)

print("Website content copied successfully!")

# Open WordPad using Run
pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')

time.sleep(3)

# Paste copied data
pyautogui.hotkey('ctrl', 'v')

print("Copied data pasted into WordPad successfully!")
