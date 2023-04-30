from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()

def checkMousePosition():
    print('Pointer position {0}'.format(mouse.position))

def setMousePoition(x,y):
    mouse.position = (x,y)
    print('position {0}'.format(mouse.position))
    time.sleep(0.5)

def clickMouse():
    mouse.click(Button.left, 1)
    time.sleep(0.5)

def scrollMouse(x,y):
    mouse.scroll(x,y) 
    time.sleep(0.5)

def selectAll():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(0.5)

def copy():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('c')
        keyboard.release('c')
    time.sleep(0.5)

def paste():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(0.5)

def switchTab():
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    time.sleep(0.5)

def main():
    n = int(input("Enter number of questions: "))
    for i in range(n):
        time.sleep(3)
        setMousePoition(1177,1000)  #check answer
        clickMouse()
        setMousePoition(1177,650) #move up
        scrollMouse(0,-20)
        clickMouse()
        selectAll()
        copy()
        switchTab()
        clickMouse()
        selectAll()
        paste()
        time.sleep(2)
        switchTab()
        scrollMouse(0,20)
        clickMouse()
        selectAll()
        keyboard.type("/do")
        setMousePoition(1643,1000) #submit
        clickMouse()
        time.sleep(3)
        setMousePoition(810, 1000) #next
        clickMouse()
        keyboard.tap(Key.esc)
        setMousePoition(923,649)
        clickMouse()
        time.sleep(3)

main()


