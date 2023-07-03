# XORゲートの実装(python XOR.py)
import torch
# tensorデータを作成(多次元配列), int16, float32型など
x = torch.tensor([8], dtype = torch.float) # intからfloatに変換

print(x)
print(x.dtype) # tensorに渡したデータの型を表示
