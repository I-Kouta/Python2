# 重回帰(python multiple-regression.py)
import numpy as np
import plotly.graph_objects as go
from variable import X1, X2, Y

Y = Y.reshape(30, -1) # 行列計算ができるように二次元配列の形式にする

def stand(X):
    M = X.mean()
    S = X.std()
    X = (X - M) / S
    return X

X1 = stand(X1)
X2 = stand(X2)
Y = stand(Y)

m = X1.shape[0] # データ数
X = np.c_[X1, X2, np.ones([m, 1])] # X1, X2とデータ数だけ1を並べた配列を結合する
theta = np.ones([3, 1]) # 初期値を1としてパラメータを設定
iterations = 1000 # 繰り返し回数(イテレーション)
alpha = 0.01
cost = []
for iter in range(iterations):
    h = np.dot(X, theta) # 現在のパラメータで仮説を計算
    # パラメータ更新
    theta[0] = theta[0] - (alpha / m) * (h - Y).T.dot(X1)
    theta[1] = theta[1] - (alpha / m) * (h - Y).T.dot(X2)
    theta[2] = theta[2] - (alpha / m) * (h - Y).sum()
    h = np.dot(X, theta) # 更新後のパラメータで仮設と目的関数を計算
    J = (1 / (2 * m)) * ((h - Y) ** 2).sum()
    cost.append(J)

a1 = theta[0]
a2 = theta[1]
b = theta[2]
print("学習後のa1: %f,"% a1)
print("学習後のa2: %f,"% a2)
print("学習後のb: %f,"% b)
print("学習後の目的関数の値: %f,"% J)
figCost = go.Figure(data = go.Scatter(y = cost))
figCost.update_layout(
    title = "cost function",
    xaxis_title = "iteration",
    yaxis_title = "cost",)
figCost.show()

G = go.Scatter3d(x = X1, y = X2, z = Y.reshape(30,), mode = "markers", marker = dict(size = 2), line = dict(color = "blue"))
x1 = x2 = np.linspace(-1.5, 1.5, 100)
X1, X2 = np.meshgrid(x1, x2)
h = theta[0] * X1 + theta[1] * X2 + theta[2]
H = go.Surface(x = X1, y = X2, z = h, opacity = 0.7)
fig = go.Figure()
fig.add_trace(G)
fig.add_trace(H)
fig.update_layout(
    scene = {
        "xaxis": {"title":"X:Height"},
        "yaxis":{"title":"Y:cal"},
        "zaxis": {"title":"Z:Weight"},
        'camera_eye': {"x": 1, "y": -1.5, "z": 1},
        "aspectratio": {"x": 1, "y": 1, "z": 1}
        }
        )
# print(fig.to_html())
fig.show()
