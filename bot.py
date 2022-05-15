import cv2
import time
import keyboard
import pyautogui
import mss
import numpy

pyautogui.PAUSE = 0.0

sct = mss.mss()
left = False

x = 1

dimensions_left = {
    'left': 820,
    'top': 580,
    'width': 100,
    'height': 80
}

dimensions_right = {
    'left': 960,
    'top': 580,
    'width': 100,
    'height': 80
}

left_branch = cv2.imread('C:\\BotPy\\leftbranch.png')
right_branch = cv2.imread('C:\\BotPy\\rightbranch.png')

while True:

    if left:
        scr = numpy.array(sct.grab(dimensions_left))
        wood = left_branch
    else:
        scr = numpy.array(sct.grab(dimensions_right))
        wood = right_branch

    scr_remove = scr[:,:,:3]

    #comparacao das imagens
    result = cv2.matchTemplate(scr_remove, wood, cv2.TM_CCOEFF_NORMED)

    #achando o valor onde há o maior match
    _, max_val, _, _ = cv2.minMaxLoc(result)

    if max_val > 0.90:
        left = not left
        if left:
            x = 1
        else:
            x = 2

    if x == 1:
        keyboard.press_and_release('left arrow')
    else:
        keyboard.press_and_release('right arrow')
    time.sleep(.13)


