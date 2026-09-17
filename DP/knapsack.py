
# 動的計画法無し ナップサック問題
# python knapsack.py
import time

def unbounded_knapsack(capacity, weights, values, n):
    # ベースケース：容量が0の場合
    if capacity == 0:
        return 0

    # 最大価値を保持する変数
    max_value = 0

    # 全てのアイテムについて繰り返す
    for i in range(n):
        # アイテムが容量内に収まる場合
        if weights[i] <= capacity:
            # そのアイテムを選んで再帰的に解く
            value_with_item = values[i] + unbounded_knapsack(capacity - weights[i], weights, values, n)

            # 最大価値を更新
            max_value = max(max_value, value_with_item)

    return max_value

# アイテムの重さと価値
weights = [5, 12, 15, 20, 21]
values = [3, 10, 13, 18, 20]

"""
金 価値:18 サイズ:20
ダイヤ 価値:20 サイズ:21
銅 価値:10 サイズ:12
プラチナ 価値:13 サイズ:15
鉛 価値:3 サイズ:5
"""

# ナップサックの容量
capacity = 50

# アイテムの数
n = len(values)

# 開始時間を記録
start_time = time.time()

# 最大価値を計算
max_value = unbounded_knapsack(capacity, weights, values, n)

# 終了時間を記録
end_time = time.time()

# 実行時間を計算
exec_time = end_time - start_time

# 実行時間を計算
print(f"ナップサック最大価値: {max_value}")
print(f"実行時間: {exec_time:.6f} 秒")
