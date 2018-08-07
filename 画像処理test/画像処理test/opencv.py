# -*- coding: utf-8 -*-

import cv2
import os


def main():

    for name in os.listdir("img\\"):
        # 入力画像の読み込み
        str="img\\"+name
        img = cv2.imread(str)

        # グレースケール変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # HoG特徴量 + SVMで人の識別器を作成
        #hog = cv2.HOGDescriptor()
        hog = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9)
        #hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())
        hogParams = {'hitThreshold': 1 ,'finalThreshold':2,'winStride': (8, 8), 'padding': (32, 32), 'scale': 2}

        # 作成した識別器で人を検出
        human, r = hog.detectMultiScale(gray, **hogParams)

        # 人の領域を赤色の矩形で囲む
        for (x, y, w, h) in human:
            cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

        # 結果を出力
        cv2.imwrite("result\\"+name,img) 


if __name__ == '__main__':
    main()