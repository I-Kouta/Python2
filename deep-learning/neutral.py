# ニュートラルネットワーク(python neutral.py)
# パーセプトロン：複数の信号を受け取った時に0, 1どちらかを出力する
import numpy as np
import matplotlib.pyplot as plt

def confirm_execution():
  confirmation = input("実行するためにはyを押してください:")
  return confirmation.lower() == "y"


def simple_perceptron(x1, x2):
    w1 = 0.2 # x1の重み
    w2 = 0.8 # x2の重み
    b = -0.7 # 発火しやすさを調整するパラメータ
    y = x1 * w1 + x2 * w2 + b
    if y <= 0:
      return 0
    elif y > 0:
      return 1

def sigmoid(x): # シグモイド間数の定義
    return 1 / (1 + np.exp(-x))

def nn_1(x): # 簡易のニュートラルネットワーク, xを入力として受け取りyを返す
  w1 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
  b1 = np.array([[0.1, 0.2, 0.3]])

  w2 = np.array([[0.1, 0.3], [0.2, 0.4], [0.5, 0.7]])
  b2 = np.array([[0.1, 0.3]])

  # 行列計算:線形変換してシグモイド間数に代入している
  m = np.dot(x, w1) + b1
  n = sigmoid(m)
  y = np.dot(n, w2) + b2
  return y

x = np.array([0.3, 0.6])
y1 = nn_1(x)

# シグモイド関数を描画
x = np.linspace(-6, 6, 1000)
y = sigmoid(x) # 0~1の値を返す

def execute_matrix_calculation():
  print(simple_perceptron(0, 0))
  print(simple_perceptron(0, 1))
  print(y1)

  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(x, y)
  plt.show()

if confirm_execution():
   execute_matrix_calculation()
else:
   print("プログラムを終了します。")
