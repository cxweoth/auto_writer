import subprocess
import pyautogui
import time
import keyboard

# read the article from a file
filepath = "text.txt"
with open(filepath, "r") as file:
    article = file.read()

subprocess.Popen(["notepad.exe"])

time.sleep(5)  

try:
    index = 0
    total_len = len(article)
    while True:
        if keyboard.is_pressed('esc'):
            print("stopped by ESC")
            break
        
        char = article[index]
        pyautogui.write(char, interval=0.05)  
        index += 1

        if index >= total_len:
            # eliminate all texts
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.press('backspace')
            time.sleep(2)
            index = 0

except KeyboardInterrupt:
    print("stopped by user")

