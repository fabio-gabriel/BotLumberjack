import cv2
import time
import keyboard
import pyautogui
import mss
import numpy

pyautogui.PAUSE = 0.0

print("Press s to start")
print("Press q to stop")
keyboard.wait('s')

sct = mss.mss()
left = False

x = 'esq'

dimensions_left = {
    'left': 820,
    'top': 580,
    'width': 150,
    'height': 150
}

dimensions_right = {
    'left': 920,
    'top': 580,
    'width': 150,
    'height': 150
}

left_branch = cv2.imread('C:\\BotPy\\leftbranch.png')
right_branch = cv2.imread('C:\\BotPy\\rightbranch.png')

w = left_branch.shape[1]
h = left_branch.shape[0]

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
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    print(f"Max val: {max_val} Max loc {max_loc}")

    scr = scr.copy()

    if max_val > 0.90:
        left = not left
        if left:
            x = 'esq'
        else:
            x = 'dir'
        cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (255, 0, 0), 2)

    cv2.imshow('Screen Shot', scr)
    cv2.waitKey(1)
    if x == 'esq':
        keyboard.press_and_release('left arrow')
    else:
        keyboard.press_and_release('right arrow')
    time.sleep(.15)

    if keyboard.is_pressed('q'):
        break
# counter = 0

# while counter < 30:

#     print("oi")
#     time.sleep(1)
#     keyboard.press_and_release('right arrow')
#     counter += 1

