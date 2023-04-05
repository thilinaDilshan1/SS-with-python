
import os
import pyautogui
import time

for i in range(1,103):
    file=str(i)+".php"
    name=str(i)
    os.system("cmd /c start http://localhost/co2114/2019COM79/Assignment%2001/PHP%20Basic/"+file)
    time.sleep(2)
    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to file
    screenshot.save('E:/Projects/Python/SS-with-python/screenshot'+name+'.png')

    time.sleep(1)

    # Close the browser tab
    pyautogui.hotkey('ctrl', 'w')

