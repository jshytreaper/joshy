from pynput.mouse import Button , Controller
import time
import ctypes


wait = time.sleep
mouse = Controller()

mouse.position = 640, 525



def click():
    mouse.click(Button.left,90000000000)
    

inp = input("Autoclick?\n\n")

if inp == "y" or inp == "Y":
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    click()
