# 重回帰追記(python multiple-regression2.py)
import numpy as np

# X1：一つ目の説明変数（身長 [cm]）
X1 = np.array([131, 132, 132, 133.5, 135, 142, 143.8, 144, 148, 149, 150, 152, 153, 157, 158,
               158, 162, 164, 166, 169, 169.5, 170, 172, 173, 173, 176, 180, 184, 186, 190])

# X2：二つ目の説明変数（一日の摂取カロリー [kcal]）
X2 = np.array([1120, 1340, 1600, 1450, 1500, 1700, 1800, 1780, 2100, 1900, 2000, 2050, 2150, 2180, 2220,
               2300, 2310, 2350, 2100, 2450, 2400, 2320, 2800, 2650, 2700, 3000, 2650, 2800, 2500, 2850])

# Y：Xに対応する正解データ（体重 [kg]）
Y = np.array([28, 29, 35, 40, 31, 40, 42, 45, 50, 48, 56, 50, 51, 56, 65,
              61, 66, 61.5, 69, 71, 63, 68, 80, 74, 76.5, 82, 68, 75, 92, 90])

def stand(X):
    M = X.mean()
    S = X.std()
    X = (X - M) / S
    return M, S

X1_m, X1_s = stand(X1)
X2_m, X2_s = stand(X2)
Y_m, Y_s = stand(Y)

# 以下、未知データに対する予測
x1 = 170 # 未知の入力値1
x2 = 2300 # 未知の入力値2
# y = 67.7 # 未知の入力値3

x1_ = (x1 - X1_m) / X1_s # 入力値1を標準化
x2_ = (x2 - X2_m) / X2_s # 入力値2を標準化
# y_ = (y - Y_m) / Y_s # 入力値3を標準化

# 学習によって得られたパラメータ
a1 = 0.598604
a2 = 0.379209
b = 0.000043

h_ = a1 * x1_ + a2 * x2_ + b # 仮説で予測値を計算
# h_ = a1 * x1_ + a2 * y_ + b # 仮説で予測値を計算

h = h_ * Y_s + Y_m # 標準化された値を元に戻す
# h = h_ * X2_s + X2_m # 標準化された値を元に戻す

print(f"身長{x1}cm、接種カロリー{x2}kcalの人の体重は{round(h, 1)}kg")
# print(f"身長{x1}cm、体重は{y}kgのひとのカロリーは{round(h, 1)}")
