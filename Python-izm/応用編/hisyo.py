
# 秘書問題を解く
# python hisyo.py

import numpy as np

# 応募者の人数
N = 100

# シミュレーション回数
n_exam = 1000

# 評価値の最大値
max_eval = 100

# 採用結果、採用した人の評価値の履歴、できなければ0
history = []

np.random.seed(1)
