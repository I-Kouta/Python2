# 行列の計算(python queue.py)
import numpy as np

matrixA = np.array([[1, 2]])
matrixB = np.array([[1, 2, 3], [4, 5, 6]])
 # 1 * 1 + 2 * 4 = 9
 # 1 * 2 + 2 * 5 = 12
 # 1 * 3 + 2 * 6 = 15
print(f"行列の積:{np.dot(matrixA,  matrixB)}")
