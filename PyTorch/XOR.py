# XORゲートの実装(python XOR.py)
import torch
import numpy as np

# tensorデータを作成(多次元配列), int16, float32型など
x = torch.tensor([[3.0, 2.0], [5.0, 6.0]]) # torch

print(f"x is {x}")

t_np = x.numpy() # np.nparrayに変換
print(f"t_np = {t_np}")
