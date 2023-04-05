import os
import pyautogui
import time

for i in range(1,18):
    file=str(i)+".php"
    name=str(i)
    os.system("cmd /c start http://localhost/co2114/2019COM79/Assignment%2001/PHP%20Searching%20and%20Sorting%20Algorithm/"+file)

    # wait until open the web browser
    time.sleep(1)

    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to file
    screenshot.save('E:/Projects/Python/SS-with-python/screenshot'+name+'.png')

    # Close the browser tab
    pyautogui.hotkey('ctrl', 'w')
