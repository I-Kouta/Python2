# 2クラスの色分け(python classification.py)
import torch
import torch.nn as nn
from torch.nn import functional as F
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
# データセット
samples = 500
X, Y = datasets.make_circles(n_samples = samples, shuffle = False, factor = 0.3, noise = 0.1)
# データセットをシャッフルして分割
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2)
# float32のtensorに変換
train_X = torch.FloatTensor(train_X)
train_Y = torch.FloatTensor(train_Y)
test_X = torch.FloatTensor(test_X)
test_Y = torch.FloatTensor(test_Y)

train = TensorDataset(train_X, train_Y)
BATCH_SIZE = 8

train_dataloader = DataLoader( # 訓練用データ作成
    train,
    batch_size=BATCH_SIZE,
    shuffle=True
)
# モデル定義
class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.fc1 = nn.Linear(2, 8)
    self.fc2 = nn.Linear(8, 1)
    self.sigmoid = torch.nn.Sigmoid()

  def forward(self, x):
    x = self.fc1(x)
    x = F.relu(x)
    x = self.fc2(x)
    x = self.sigmoid(x)
    return x

net = Net() # インスタンス化
criterion = nn.BCELoss() # 損失関数の設定(BCE損失)
optimizer = torch.optim.SGD(net.parameters(), lr = 0.1) # 最適化手法の選択(SGD)

y_axis_list = [] #損失プロット用y軸方向リスト

for epoch in range(100):
  for batch, label in train_dataloader: #エポックのループの内側で、さらにデータローダーによるループ
    optimizer.zero_grad()
    t_p = net(batch)
    label = label.unsqueeze(1) #損失関数に代入するために次元を調節する処理
    loss = criterion(t_p, label)
    loss.backward()
    optimizer.step()
  y_axis_list.append(loss.detach().numpy()) # プロット用のy軸方向リストに損失の値を代入

  if epoch % 10 == 0: # 10エポック毎に損失の値を表示
    print(f"epoch: {epoch + 1}  loss: {round(float(loss), 6)}")

x_axis_list = [num for num in range(100)] # 損失プロット用x軸方向リスト
# 損失の描画
plt.xlabel("epoch")
plt.ylabel("loss")
plt.plot(x_axis_list, y_axis_list)
plt.show()
