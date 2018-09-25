# -*- coding: utf-8 -*-
import numpy as np
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image

def main():
    # VGG16の学習済みモデルを読み込み
    model = VGG16(weights='imagenet')

    # 入力画像の読み込み（VGG16の標準サイズ(224x224)にリサイズ）
    img = image.load_img("input.jpg", target_size=(224, 224))

    # NumPy配列に変換
    x = image.img_to_array(img)

    # 3次元配列→4次元配列
    x = np.expand_dims(x, axis=0)

    # 予測
    preds = model.predict(preprocess_input(x))

    # 予測結果（第1～5候補）の表示
    results = decode_predictions(preds, top=5)[0] # 出力ベクトルを文字列に変換
    for result in results:
        print(result)


if __name__ == '__main__':
    main()