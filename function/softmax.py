# ソフトマックス関数(python softMax.py)
# 出力の値の合計が1になる → 確率として解釈
import numpy as np

def soft_max(x): # 関数の定義
    return np.exp(x) / np.sum(np.exp(x))

X = np.array([5, 3, 4]) # 入力値
y = soft_max(X)

print(y)
print(np.sum(y))
