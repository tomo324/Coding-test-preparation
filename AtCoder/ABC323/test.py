# OpenCV でカメラ映像を取得し、ぼかして表示する
# 起動時の引数　--radius でぼかしの強さを調整可能
# Qキーを入力すると終了する

import cv2
import argparse

# コマンドライン引数のパース
parser = argparse.ArgumentParser()
parser.add_argument('--radius', type=int, default=10, help='blur radius')
args = parser.parse_args()

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

while True:
    # フレームを取得
    _, frame = cap.read()

    # ぼかしを適用
    frame = cv2.blur(frame, (args.radius, args.radius))

    # フレームを表示
    cv2.imshow('Original', frame)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()

# 画像の読み込み
img = cv2.imread('sample.jpg')

# 画像の表示
cv2.imshow('sample', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像の保存
cv2.imwrite('sample.png', img)

# 画像のサイズを変更
img = cv2.resize(img, (500, 300))

# 画像の一部を切り取り
img = img[100:200, 200:300]

