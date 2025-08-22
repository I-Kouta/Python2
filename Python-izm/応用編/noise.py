
# ガウシアンノイズ
# python noise.py

# 必要なライブラリの読み込み
import numpy as np
import cv2
import matplotlib.pyplot as plt

# シードの設定
np.random.seed(42)

#ノイズ付与の関数
def add_noise(img, mu = 0, sigma = 1):
    # 画素数xRGBのノイズを生成
    noise = np.random.normal(mu, sigma, img.shape)
    # ノイズを付加して8bitの範囲にクリップ
    noisy_img = img.astype(np.float64) + noise
    noisy_img = np.clip(noisy_img, 0, img.shape[0]).astype(np.uint8)

    return noisy_img

# 画像の読み込み
img = cv2.imread("/Users/ko-ta/Downloads/Tokyo.jpg", cv2.IMREAD_COLOR)

# 画像にノイズを追加
mu = 0
sigma = 100
noisy_img = add_noise(img, mu, sigma)

# 画像の表示
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("raw image")
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(noisy_img)
plt.title(f"add noise mu{mu}_sigma{sigma}")
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
