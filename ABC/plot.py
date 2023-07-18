# 常微分方程式(python plot.py)
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model(y, t):
    # y:未知関数, t:時間変数, dydt:yに対する導関数
    dydt = -y + 1.0  # 1.0に収束する
    return dydt

y0 = 0  # 初期値
t = np.linspace(0, 5)  # 時間
y = odeint(model, y0, t)
# 結果のプロット
plt.plot(t, y)  # (x軸の値, y軸の値)
plt.xlabel("time(x shaft)")  # 軸ラベルの名前
plt.ylabel("y(y shaft)")  # 軸ラベルの名前
plt.show()
