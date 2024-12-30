
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

def make_application_sample(N, max_eval):
    """
    応募者と評価値の最大値を受け取り、応募者のリストを返す
    """
    sample = np.random.normal(10, 10, N) # 平均, 標準偏差, 配列数
    min_sample = np.min(sample)
    max_sample = np.max(sample)
    # 正規化処理(0 ~ 1の間になる)
    normalized = (sample - min_sample) / (max_sample - min_sample) * max_eval
    return normalized

print(make_application_sample(N, max_eval))
