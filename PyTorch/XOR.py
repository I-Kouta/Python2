# XORゲート(python XOR.py)
import torch
import torch.nn as nn

X = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], requires_grad = True) # データ
y = torch.tensor([[0.0], [1.0], [1.0], [0.0]]) # ラベル

model = nn.Sequential( # 3層のニュートラルネットワークを定義
    nn.Linear(2, 8), # 線形層(入力数, 出力数)
    nn.ReLU(), # 活性化関数
    nn.Linear(8, 1),
    nn.Sigmoid()
)

loss_fn = nn.BCELoss() # 真の値と予測を比較して誤差を返す(損失関数)

optimizer = torch.optim.SGD(params = model.parameters(), lr = 0.1)

for epoch in range(2000): # 2000エポック学習させる
    optimizer.zero_grad() # 勾配を0に初期化する必要がある
    t_p = model.forward(X) # 順伝播
    loss = loss_fn(t_p, y) # 損失を計算
    loss.backward() # 逆伝播
    optimizer.step() # オプティマイザがパラメータの更新量を計算し、モデルに返してパラメータ更新

if epoch % 100 == 0:#100エポック毎に損失の値を表示
    print("epoch: %d  loss: %f" % (epoch + 1 ,float(loss)))
