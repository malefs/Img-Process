# -*- coding: utf-8 -*-
import cv2
import ctypes
import numpy as np
import mylib.mylib as mylib
import sys
import os
import time
import threading
import win32gui
 

 
#WordPadClassの部分を、アクティブにするウィンドウのクラス名にすればよい。
def find_rect_of_target_color(image,h_v,h_v2,s_v,s_v2,v_v,v_v2):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:,:,2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > h_v * 255 / 360) | (h < h_v2 * 255 / 360)) & ((s > s_v) & (s < s_v2)) & ((v > v_v) & (v < v_v2))] = 255#h色相 s彩度 v明度
    _,contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)#0
        #rect = cv2.minAreaRect(approx) #1
                                               #print(rect[2])
                                               #box= cv2.boxPoints(rect)
                                               #print(rect)
        rects.append(np.array(rect))
        #rects.append(np.int0(box))
    return rects

def hsv_show():
    hsv_img = mylib.imread("image\hsv.png", 1)
    cv2.imshow("hsv",hsv_img)
    cv2.waitKey(0)

thread_1 = threading.Thread(target=hsv_show)

# 画像の読み込み
img = mylib.imread(mylib.Select(), 1)
if type(img) != np.ndarray:
    print("画像が読み込めませんでした。")
    os.system("pause")
    sys.exit()

origin = img.copy()

# 読み込んだ画像の高さと幅を取得
height = img.shape[0]
width = img.shape[1]

img = img[int(height / 3):int(height * 2 / 3),int(width / 3):int(width * 2 / 3)]

height = img.shape[0]
width = img.shape[1]

size = 100

k = width / size

# 画像のサイズを変更
 # 第一引数：サイズを変更する画像
 # 第二引数：変更後の幅
 # 第三引数：変更後の高さ
resized_img = cv2.resize(img,(size,int(height / k)))

resized_img = cv2.resize(resized_img,(width,height))

thread_1.start()

while(True):
    test_img = resized_img.copy()

    while(True):
        print("h以上")
        try:
            h = int(input(">> "))
        except:
            pass
        else:
            break
    
    while(True):
        print("h以下")
        try:
            h2 = int(input(">> "))
        except:
            pass
        else:
            break

    while(True):
        print("s以上")
        try:
            s = int(input(">> "))
        except:
            pass
        else:
            break

    while(True):
        print("s以下")
        try:
            s2 = int(input(">> "))
        except:
            pass
        else:
            break

    while(True):
        print("v以上")
        try:
            v = int(input(">> "))
        except:
            pass
        else:
            break

    while(True):
        print("v以下")
        try:
            v2 = int(input(">> "))
        except:
            pass
        else:
            break

    print("色相: " + str(h) + "以上" + str(h2) + "以下")
    print("彩度: " + str(s) + "以上" + str(s2) + "以下")
    print("明度: " + str(v) + "以上" + str(v2) + "以下")
        


    rects = find_rect_of_target_color(test_img,h,h2,s,s2,v,v2)
    resized_img2 = origin.copy()

    for rect in rects:
        cv2.rectangle(test_img,tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]),(0,0,255),thickness=2)
        #cv2.drawContours(test_img,rect,0,(0,0,255),2)

    #cv2.imshow("img", test_img)
    try:
        cv2.destroyWindow("img-s")
    except:
        pass
    cv2.imshow("img-s",test_img)
    handle = ctypes.windll.user32.FindWindowW(0, "img-s")
    if handle is not 0:
      win32gui.SetForegroundWindow(handle)
    cv2.waitKey(0)
    handle = ctypes.windll.user32.FindWindowW(0, "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe")
    if handle is not 0:
      win32gui.SetForegroundWindow(handle)

sys.exit()
