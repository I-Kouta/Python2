# 重回帰(python multiple-regression.py)
import numpy as np
import plotly.graph_objects as go

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
    return X

X1 = stand(X1)
X2 = stand(X2)
Y = stand(Y)

m = X1.shape[0] # データ数
X = np.c_[X1, X2, np.ones([m, 1])]
theta = np.ones([3, 1]) # 初期値を1としてパラメータを設定
h = np.dot(X, theta) # 行列積を用いたドット積で仮説定義
G = go.Scatter3d(x = X1, y = X2, z = Y, mode = 'markers', marker=dict(size=2), line=dict(color="blue"))
x1 = x2 = np.linspace(-1.5, 1.5, 100)
X1, X2 = np.meshgrid(x1,x2)
h = theta[0]*X1+theta[1]*X2+theta[2]
H = go.Surface(x = X1,y = X2,z = h, opacity=0.7)
fig = go.Figure()
fig.add_trace(G)
fig.add_trace(H)
# fig = go.Figure(go.Scatter3d(x = x1,y = x2,z = y,mode = 'markers',marker=dict(size=2), line=dict(color="blue")))
fig.update_layout(
    scene = {
        "xaxis": {"title":"X:Height"},
        "yaxis":{"title":"Y:cal"},
        "zaxis": {"title":"Z:Weight"},
        'camera_eye': {"x": 1, "y": -1.5, "z": 1},
        "aspectratio": {"x": 1, "y": 1, "z": 1}
        }
        )
print(fig.to_html())
fig.show()
