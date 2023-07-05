# XORゲート(python XOR.py)
import torch.nn as nn

# 3層のニュートラルネットワークを定義
model = nn.Sequential(
    nn.Linear(2, 8), # 線形層(入力数, 出力数)
    nn.ReLU(), # 活性化関数
    nn.Linear(8, 1),
    nn.Sigmoid()
)
print(model)
