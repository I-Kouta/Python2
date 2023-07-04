# PyTorch, テンソル(多次元配列)(python example.py)
import torch
import numpy as np
# tensorデータを作成(多次元配列), int16, float32型など
array = np.array([[3.0, 2.0], [5.0, 6.0]]) # NumPyのデータ型はfloat64型

print(f"np.arrayを定義: {array}")

array = array.astype(np.float32) # np.ndarrayのデータ型をfloat32型に変換

array2tensor = torch.from_numpy(array)

print(f"torch.tensorに変換: {array2tensor}")
