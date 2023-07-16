# データ拡張(python cv.py)
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import cv2
# OpenCVを使って画像を読み込む
img = cv2.imread("/Users/ko-ta/downloads/ダーク系.jpg")
#BGRをRGBに変換
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 変換
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomErasing(p = 1),
    transforms.ToPILImage()  # PIL画像に変換する処理
    # transforms.RandomHorizontalFlip(p = 1) # 水平方向に回転
    # transforms.RandomVerticalFlip(p = 1) # 垂直方向に回転
])
transform = transform(img_rgb)

def visualize(original, reverse):
    plt.subplot(1, 2, 1)
    plt.title("original")
    plt.imshow(original)

    plt.subplot(1, 2, 2)
    plt.title("reverse")
    plt.imshow(reverse)
    plt.show()

visualize(img_rgb, transform)
