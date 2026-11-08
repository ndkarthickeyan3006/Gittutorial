
import pyautogui
import pyperclip
import time
import os
from datetime import datetime

# Basic settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Get today's date and time
now = datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")
today_date = now.strftime("%Y-%m-%d")

# Create output folder using your given path
folder = r"C:\Users\eluxybc\OneDrive - Ericsson\Desktop\Gittutorial\Daily_Weather_Reports"

os.makedirs(folder, exist_ok=True)

# Excel and screenshot file paths
excel_file = os.path.join(
    folder, f"daily_report_{today_date}.xlsx"
)

screenshot_file = os.path.join(
    folder, f"daily_report_{today_date}.png"
)

try:

    # STEP 1: Open Chrome browser
    print("Step 1: Opening Chrome browser...")

    pyautogui.hotkey('win', 'r')
    time.sleep(2)

    pyautogui.write('chrome')
    pyautogui.press('enter')

    time.sleep(10)


    # STEP 2: Open AccuWeather website
    print("Step 2: Opening AccuWeather website...")

    pyautogui.hotkey('ctrl', 'l')

    pyautogui.write(
        'https://www.accuweather.com/en/in/hosur-sarjapur-road-layout/3352280/hourly-weather-forecast/3352280'
    )

    pyautogui.press('enter')

    time.sleep(15)


    # STEP 3: Copy website information
    print("Step 3: Copying website information...")

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    website_data = pyperclip.paste()

    if not website_data.strip():
        raise Exception("Website data was not copied.")

    print("Website information copied successfully!")


    # STEP 4: Prepare daily report
    print("Step 4: Preparing daily report...")

    comment = "Check weather before outdoor activities"

    excel_data = (
        "Date and Time\tWeather Information\tComment\n"
        + date_time + "\t"
        + website_data[:500] + "\t"
        + comment
    )



   # STEP 6: Take screenshot
    print("Step 8: Taking screenshot...")
    
    pyautogui.screenshot().save(screenshot_file)
    
    print("Screenshot saved successfully!")

    # STEP 5: Open Microsoft Excel
    print("Step 5: Opening Microsoft Excel...")

    pyautogui.hotkey('win', 'r')
    time.sleep(2)

    pyautogui.write('excel')
    pyautogui.press('enter')

    time.sleep(12)


    # STEP 7: Create new Excel workbook
    print("Step 6: Creating Excel workbook...")

    pyautogui.hotkey('ctrl', 'n')
    time.sleep(5)

    pyperclip.copy(excel_data)

    pyautogui.hotkey('ctrl', 'v')

    time.sleep(3)

    print("Weather information entered into Excel!")



    # STEP 8: Save Excel file
    print("Step 7: Saving Excel report...")

    pyautogui.press('f12')
    time.sleep(4)

    pyperclip.copy(excel_file)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')

    time.sleep(5)

    print("Excel file saved!")


   
    # STEP 9: Display completion message
    print("\n===================================")
    print("DAILY WEATHER REPORT COMPLETED!")
    print("===================================")

    print("Date and Time:", date_time)
    print("Screenshot:", screenshot_file)
    print("Excel File:", excel_file)
    

    print("\nAll tasks completed successfully!")


except pyautogui.FailSafeException:

    print("\nPyAutoGUI safety stop activated!")
    print("Move your mouse away from the screen corners.")
    print("Restart the program when ready.")


except Exception as e:

    print("\nAn error occurred:", e)
    print("Please check Chrome, Excel and clipboard.")

