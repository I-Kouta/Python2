
# 動的計画法有り ナップサック問題
# python knapsack_dp.py
import time

def unbounded_knapsack_dp(capacity, weights, values):
    n = len(weights)
    dp = [0] * (capacity + 1)

    # 開始時刻を記録
    start_time = time.time()

    for c in range(capacity + 1):
        for i in range(n):
            if weights[i] <= c:
                dp[c] = max(dp[c], values[i] + dp[c - weights[i]])

    # 終了時刻を記録
    end_time = time.time()

    # 実行時間を計算
    execution_time = end_time - start_time

    return dp[capacity], execution_time

# アイテムの重さと価値
values = [3,10,13,18,20]
weights = [5, 12,15,20,21]

"""
金 価値:18 サイズ:20
ダイヤ 価値:20 サイズ:21
銅 価値:10 サイズ:12
プラチナ 価値:13 サイズ:15
鉛 価値:3 サイズ:5
"""

# ナップサックの容量
capacity = 100

# 最大価値と実行時間を取得
max_value, exec_time = unbounded_knapsack_dp(capacity, weights, values)
print(f"DP有のナップサックの最大価値: {max_value}, 実行時間: {exec_time:.6f} 秒")
