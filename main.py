import objc
import pyautogui as pg
import pyautogui
import time
import random



TAI_X = 453
TAI_Y = 587
XIU_X = 802
XIU_Y = 588
MOT_NGHIN_X = 354
MOT_NGHIN_Y = 718
SUBMIT_X = 615
SUBMIT_Y = 785
CANCEL_X = 769
CANCEL_Y = 785

MONEY = 5 # 5000 nghin moi lan cuoc

def TAI(money):
    print(money)
    pyautogui.click(TAI_X,TAI_Y)
    time.sleep(2)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X,MOT_NGHIN_Y)
    time.sleep(2)
    pyautogui.click(SUBMIT_X,SUBMIT_Y)

def XIU(money):
    print(money)
    pyautogui.click(XIU_X,XIU_Y)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X,MOT_NGHIN_Y)
    pyautogui.click(SUBMIT_X,SUBMIT_Y)


while True:
    time.sleep(60)
    TAI_XIU_RANDOM = random.randint(1, 100)
    ps = pg.position()
    print(ps)
    # caculate...
    print(TAI_XIU_RANDOM)
    if(TAI_XIU_RANDOM % 2 == 0):
        TAI(MONEY)
        print('tai an lz 5k')
    else:
        print('xiu an lz 5k')
        XIU(MONEY)


# def tai(money):

# tai: x=428, y=451
# xiu: x=782, y=430