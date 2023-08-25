import pyperclip
import time
import keyboard
import os
from pynput.keyboard import Controller

os.system("mode con cols=30 lines=30")
pastInst = Controller()

print("请将输入法切换英文使用")
print("使用ctrl+.键入剪切板内容")
print("使用end键结束程序")
print("cmd框内使用ctrl+c强制结束程序")

def prt():
    time.sleep(2)
    data = pyperclip.paste()
    resout_data=data.replace('\r', '')
    pastInst.type(resout_data)
    print("数据键入完成！")

keyboard.add_hotkey('ctrl+.', prt)
keyboard.wait("end")