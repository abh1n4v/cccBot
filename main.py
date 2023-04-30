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

def capture():
    pointers = {}
    print('Hover your mouse on "CHECK ANSWER" button')
    time.sleep(3)
    pointers['check_answer'] = mouse.position

    print('Hover your mouse on "NEXT" button')
    time.sleep(3)
    pointers['next'] = mouse.position

    print('Hover your mouse on "SUBMIT CODE" button')
    time.sleep(3)
    pointers['submit'] = mouse.position

    return (pointers)

def mouse_reset(x,y):
    mouse.move(x,y)
    time.sleep(0.5)

def main():
    pointers = capture()
    n = int(input("Enter number of questions: "))
    for i in range(n):
        time.sleep(3)
        setMousePoition(pointers['check_answer'][0],pointers['check_answer'][1])  #check answer
        clickMouse()
        mouse_reset(0,-270) #move up
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
        setMousePoition(pointers['submit'][0],pointers['submit'][1]) #submit
        clickMouse()
        time.sleep(5)
        setMousePoition(pointers['next'][0],pointers['next'][1]) #next
        clickMouse()
        time.sleep(0.5)
        keyboard.tap(Key.esc)
        mouse_reset(0,-100)
        time.sleep(1)
        clickMouse()
        keyboard.tap(Key.tab)
        keyboard.tap(Key.enter)

main()
