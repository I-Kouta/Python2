# XORゲート(python XOR.py)
import torch
import torch.nn as nn

# 3層のニュートラルネットワークを定義
model = nn.Sequential(
    nn.Linear(2, 8), # 線形層(入力数, 出力数)
    nn.ReLU(), # 活性化関数
    nn.Linear(8, 1),
    nn.Sigmoid()
)

loss_fn = nn.BCELoss() # 真の値と予測を比較して誤差を返す(損失関数)

x = torch.tensor([2.0], requires_grad = True) # 線形変換
w = torch.tensor([4.0], requires_grad = True) # 重み
b = torch.tensor([-7.0], requires_grad = True) # バイアス

print(model)
print(loss_fn)

y = w * x + b
print(y) # 計算の流れを記憶できる
y.backward() # 計算の逆向きに自動で勾配を計算してくれる
print(w.grad)
