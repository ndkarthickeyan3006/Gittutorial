import pyautogui
import time
import pyscreeze

#pyautogui.PAUSE = 0

#time.sleep(2)

#pyautogui.typewrite("Hello World!", interval=0.1)

#hot Keys
#pyautogui.hotkey('ctrl', 'c', _pause=False)

screenshot = pyautogui.screenshot()
screenshot.save("final.png")

print("Screenshot saved successfully!")