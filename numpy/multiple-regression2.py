# 重回帰追記(python multiple-regression2.py)
from variable import X1, X2, Y

def stand(X):
    M = X.mean()
    S = X.std()
    X = (X - M) / S
    return M, S

X1_m, X1_s = stand(X1)
X2_m, X2_s = stand(X2)
Y_m, Y_s = stand(Y)

# 以下、未知データに対する予測(170cm, 2300kcal, 67.7kg)
x1 = 170 # 未知の入力値1
# x2 = 2300 # 未知の入力値2
y = 67.7 # 未知の入力値3

x1_ = (x1 - X1_m) / X1_s # 入力値1を標準化
# x2_ = (x2 - X2_m) / X2_s # 入力値2を標準化
y_ = (y - Y_m) / Y_s # 入力値3を標準化

# 学習によって得られたパラメータ
a1 = 0.598604
a2 = 0.379209
b = 0.000043

# h_ = a1 * x1_ + a2 * x2_ + b # 仮説で予測値を計算
h_ = a1 * x1_ + a2 * y_ + b # 仮説で予測値を計算

h = h_ * X2_s + X2_m # 標準化された値を元に戻す

# print(f"身長{x1}cm、接種カロリー{x2}kcalの人の体重は{round(h, 1)}kg")
print(f"身長{x1}cm、体重は{y}kgのひとのカロリーは{round(h, 1)}")
