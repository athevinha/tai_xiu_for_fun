import pyautogui as pg
import pyautogui
import time
import random


# Tool của NTV
# STEP 1: Tìm các vị trí đúng của TAI, XIU,MOT_NGHIN, ĐẶT CƯỢC, HUỶ ở trong màn hình
# bằng cách tắt hàm START và chạy hàm FIND_TAI_XIU_SUBMIT_POSITION rồi di chuột để lấy vị trí của các nút
# STEP 2: MONEY là số tiền muốn cược mỗi lần ( tự chỉnh )
# STEP 3: Chạy hàm START rồi ngồi chill chờ tiền bay :)))

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
TIME = 60 # 60s cuoc 1 lan

def TAI(money):
    pyautogui.click(TAI_X,TAI_Y)
    time.sleep(1)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X,MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X,SUBMIT_Y)

def XIU(money):
    pyautogui.click(XIU_X,XIU_Y)
    time.sleep(1)
    for i in range(money):
        pyautogui.click(MOT_NGHIN_X,MOT_NGHIN_Y)
    time.sleep(1)
    pyautogui.click(SUBMIT_X,SUBMIT_Y)

def START():
    while True:
        time.sleep(TIME)
        TAI_XIU_RANDOM = random.randint(1, 100)
        ps = pg.position()
        print(ps)
        # caculate...
        print(TAI_XIU_RANDOM)
        if(TAI_XIU_RANDOM % 2 == 0):
            TAI(MONEY)
            print('tai')
        else:
            print('xi')
            XIU(MONEY)

def FIND_TAI_XIU_SUBMIT_POSITION():
      while True:
        time.sleep(5)
        ps = pg.position()
        print(ps)
