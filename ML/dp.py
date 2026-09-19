
# 動的計画法
# python dp.py
import timeit

# DPなし フィボナッチ数列
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(10))

# DPあり フィボナッチ数列
def fib_DP(n, memo = {}):
    if n in memo: # 部分問題の解をメモしておく
        return memo[n]
    if(n == 0):
        return 0 #F(0)=0
    if(n == 1):
        return 1 #F(1)=1

    memo[n] = fib_DP(n - 1, memo) + fib_DP(n - 2, memo)
    return memo[n]
print(fib_DP(10))

# 計算速度を比較
ns = [5, 20, 35]
results = []

# 各項の計算時間を測定
for n in ns:
    fib_result = fib(n)
    fib_DP_result = fib_DP(n, {})
    # 実行時間を計測
    original_time = timeit.timeit('fib(n)', globals = globals(), number = 1)
    memoized_time = timeit.timeit('fib_DP(n)', globals = globals(), number = 1)
    results.append((n, fib_result, original_time, fib_DP_result, memoized_time))

# 結果を表示
for result in results:
    n, fib_result, original_time, fib_DP_result, memoized_time = result
    print(f"n = {n}")
    print(f"動的計画法なし: 解 {fib_result}  実行時間 {original_time:.6f} s")
    print(f"動的計画法あり: 解 {fib_DP_result}  実行時間 {memoized_time:.6f} s")
    print()
