# XORゲートの実装(python XOR.py)
import torch
import torch.nn as nn # nnモジュール

linear_model = nn.Linear(1, 1) # 線形モデルのインスタンスを生成, 入力値(tensor型)・出力値(tensor型)・バイアス(bool)

x = torch.tensor([3.0]) # 線形変換した結果の出力が得られる

print(f"重み:{linear_model.weight}", "\n") # 重み
print(f"バイアス:{linear_model.bias}", "\n") # バイアス
print(f"tensorを入力として代入した結果:{linear_model(x)}")
