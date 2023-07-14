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

for epoch in range(100):
  for batch, label in train_dataloader: # エポックのループの内側で、さらにデータローダーによるループ
    optimizer.zero_grad()
    t_p = net(batch)
    label = label.unsqueeze(1) #損失関数に代入するために次元を調節する処理
    loss = criterion(t_p, label)
    loss.backward()
    optimizer.step()
  if epoch % 10 == 0: # 10エポック毎に損失の値を表示
    print(f"epoch: {epoch + 1}  loss: {round(float(loss), 6)}")
# 離散化を行う関数
def discretize(proba):
  threshold = torch.Tensor([0.5]) # 0・1を分ける閾値を0.5に設定
  discretized = (proba >= threshold).int() # 閾値未満で0,以上で1に変換
  return discretized
# 離散化の処理
with torch.no_grad(): # 試験用データでは勾配を計算しない
    pred_labels = [] # バッチごとの結果格納
    for x in test_X:
            pred = net(x)
            pred_label = discretize(pred) # 離散化する
            pred_labels.append(pred_label[0])
pred_labels = np.array(pred_labels) # numpy arrayに変換
# 結果描写
X_red = test_X[pred_labels == 0]
X_blue = test_X[pred_labels == 1]
plt.scatter(X_red[:, 0], X_red[:, 1], color='red')
plt.scatter(X_blue[:, 0], X_blue[:, 1], color='blue')
plt.show()
