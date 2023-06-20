# 重回帰(python multiple-regression.py)
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# X1：一つ目の説明変数（身長 [cm]）
x1 = np.array([131, 132, 132, 133.5, 135, 142, 143.8, 144, 148, 149, 150, 152, 153, 157, 158, 158, 162, 164, 166, 169, 169.5, 170, 172, 173, 173, 176, 180, 184, 186, 190])

# X2：二つ目の説明変数（一日の摂取カロリー [kcal]）
x2 = np.array([1120, 1340, 1600, 1450, 1500, 1700, 1800, 1780, 2100, 1900, 2000, 2050, 2150, 2180, 2220, 2300, 2310, 2350, 2100, 2450, 2400, 2320, 2800, 2650, 2700, 3000, 2650, 2800, 2500, 2850])

# Y：Xに対応する正解データ（体重 [kg]）
y = np.array([28, 29, 35, 40, 31, 40, 42, 45, 50, 48, 56, 50, 51, 56, 65, 61, 66, 61.5, 69, 71, 63, 68, 80, 74, 76.5, 82, 68, 75, 92, 90])

fig = go.Figure(go.Scatter3d(x = x1,y = x2,z = y,mode = 'markers',marker=dict(size=2), line=dict(color="blue")))
fig.update_layout(
    scene = {
        "xaxis": {"title":"Height"},
        "yaxis":{"title":"cal"},
        "zaxis": {"title":"Weight"},
        'camera_eye': {"x": 1, "y": -1.5, "z": 1},
        "aspectratio": {"x": 1, "y": 1, "z": 1}
        }
        )
print(fig.to_html())
