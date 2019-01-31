'''
A script for handeling inputs into the factorio windows gui
'''

import win32gui, win32api, win32con
import random
import time


#bind to factorio window

#(759,394) #'play' pos
#(760, 419) #'new game' pos
#(537, 406) #'rich resources'
#(972, 740) #'Generate'

#while(True):
    #get visual output
    #give input


#useful functions:
'''
win32gui
GetCursorInfo()
HWND = GetActiveWindow()

win32api
SetCursorPos((x,y))
keybd_event(bVk, bScan, dwFlags, dwExtraInfo)


'''

#handle enumerating through all windows to find factorio window
def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'Factorio 0.16.51' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, 0, 0, 1520, 1000, True)
            print(hwnd)




def windows_mouse_click_left(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x,y, 0, 0)#'play' pos
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x,y, 0, 0)#'play' pos
    time.sleep(1)

def windows_mouse_click_right(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x,y, 0, 0)#'play' pos
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x,y, 0, 0)#'play' pos
    time.sleep(1)

def windows_keybd_press_w():
    win32api.keybd_event(0X57, 0, 0, 0)
    time.sleep(5)
    win32api.keybd_event(0X57, 0, win32con.KEYEVENTF_KEYUP)

def windows_keybd_press_a():
    win32api.keybd_event(0X41, 0, 0, 0)
    time.sleep(5)
    win32api.keybd_event(0X41, 0, win32con.KEYEVENTF_KEYUP)

def windows_keybd_press_s():
    win32api.keybd_event(0X53, 0, 0, 0)
    time.sleep(5)
    win32api.keybd_event(0X53, 0, win32con.KEYEVENTF_KEYUP)

def windows_keybd_press_d():
    win32api.keybd_event(0X44, 0, 0, 0)
    time.sleep(5)
    win32api.keybd_event(0X44, 0, win32con.KEYEVENTF_KEYUP)

def begin_game():
    #set Factorio to the proper size
    win32gui.EnumWindows(enumHandler, None)

    print("Clicking play...")

    #prepare the game
    windows_mouse_click_left(759,394)    #start
    windows_mouse_click_left(760,419)    #new game
    windows_mouse_click_left(537,406)    #rich resources --optional
    windows_mouse_click_left(972,740)    #generate

def run_randomly():
    #hold down the w key
    rand = random.randint(0,3)
    if rand == 0:
        windows_keybd_press_w()
    elif rand == 1:
        windows_keybd_press_a()
    elif rand == 2:
        windows_keybd_press_s()
    elif rand ==3:
        windows_keybd_press_d()

