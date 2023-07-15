# データ拡張(python cv.py)
import matplotlib.pyplot as plt
import cv2
# OpenCVを使って画像を読み込む
img = cv2.imread('/Users/ko-ta/downloads/ダーク系.jpg')
#BGRをRGBに変換
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#読み込んだ画像を表示
plt.imshow(img_rgb)
plt.show()
