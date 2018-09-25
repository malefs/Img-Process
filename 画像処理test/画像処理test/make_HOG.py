# -*- coding: utf-8 -*
import os, glob, sys
import cv2
import numpy as np

# Hog特徴量の計算
def calc_hog(img_paths, bin_n=32):
    hists = []
    for img_path in img_paths:
        # 画像をグレースケールで読み込み
        gray = cv2.imread(img_path, 0)
        # ソーベルフィルタで縦・横方向のエッジ画像を生成
        gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)
        # エッジ勾配の角度と大きさを算出
        mag, ang = cv2.cartToPolar(gx, gy)
        # 勾配方向の量子化(16方向)
        bins = np.int32(bin_n*ang/(2*np.pi))
        # 勾配方向ヒストグラムを計算
        hist = np.bincount(bins.ravel(), mag.ravel(), bin_n)
        hists.append(hist)

    return np.array(hists, np.float32)

def main():
    # 正解画像・非正解画像のファイルパスを取得
    pos_img_paths = glob.glob('pos/*')
    neg_img_paths = glob.glob('neg/*')
    
    # Hog特徴量の計算
    pos_hogs = calc_hog(pos_img_paths)
    neg_hogs = calc_hog(neg_img_paths)
    hogs = np.r_[pos_hogs, neg_hogs]

    # ラベル用配列の生成（正解：1, 非正解:0）
    pos_labels = np.ones(len(pos_img_paths), np.int32)
    neg_labels = np.zeros(len(neg_img_paths), np.int32)
    labels = np.array([np.r_[pos_labels, neg_labels]])

    # Hog特徴量をSVMで学習
    svm = cv2.ml.SVM_create()
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_RBF)
    svm.setGamma(5.4)
    svm.setC(2.7)
    svm.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 1.e-06))
    svm.train(hogs, cv2.ml.ROW_SAMPLE, labels)
    svm.save('hog_car1.xml') # 自作識別器の出力


if __name__ == '__main__':
    main()