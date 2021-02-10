'''
Full Project Link :- https://github.com/shantonuacharjee1/Auto-Comment-Facebook-Messenger-WhatsApp
Author: Shantonu Acharjee
Email: shantonuacharjee@gmail.com
YouTube :- http://tinyurl.com/yy374bou
FaceBook: http://tinyurl.com/y52rgdd4
'''
import pyautogui
import time
a= 372
while True:

    time.sleep(5)
    pyautogui.typewrite("Never Do This Again."+str(a))
    time.sleep(5)
    a=a+1

    pyautogui.press('enter')
    if a == 3001:
        break