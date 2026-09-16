
# 動的計画法
# python dp.py

# DPなし フィボナッチ数列
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(9))

# DPあり フィボナッチ数列
def fib_DP(n, memo={}):
    if n in memo: # 部分問題の解をメモしておく
        return memo[n]
    if(n==0):
        return 0 #F(0)=0
    if(n==1):
        return 1 #F(1)=1

    memo[n]=fib_DP(n-1, memo) + fib_DP(n-2, memo)
    return memo[n]
print(fib_DP(9))
