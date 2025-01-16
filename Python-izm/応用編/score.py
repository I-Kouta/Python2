
# python score.py
# 表と裏が出る確率それぞれ1 / 2のコインをn回投げ得点を決める
# 最初に数直線上の原点に石を置き、表なら2、裏なら3だけ数直線上を正方向に石を移動
# an ≠ 2n + 2の場合は得点0、an = 2n + 2の場合は得点をa1 + a2 + ... + anとする

import random
from fractions import Fraction
# 1.n回のうち裏の出る回数をrとした時のan
# an = 3r + 2(n - r) = 2n + r

# 2.n = 4とする時、得点が0でない確率・25である確率
n = 4
iteration = 100000 # 試行回数
count1 = 0 # 得点が0でない回数
count2 = 0 # 得点が25の回数

for _ in range(iteration):
    a = 0 # 石の位置
    score = 0 # 得点

    for i in range(n):
        p = random.random() # 0以上1未満の乱数
        if p < 0.5: # 表
            a += 2
        else: # 裏
            a += 3
        score += a

    if a != 2 * n + 2:
        score = 0

    if score != 0:
        count1 += 1
    if score == 25:
        count2 += 1

print(f"得点が0でない確率 : {count1 / iteration} = {Fraction(count1 / iteration).limit_denominator(100)}") # 約0.375(3 / 8)
print(f"得点が25の確率 : {count2 / iteration} = {Fraction(count2 / iteration).limit_denominator(100)}") # 約0.125(1 / 8)
print("-----")

# 3.n = 9とする時、得点が100である確率・奇数である確率
n = 9

# i回コインを投げて、石の位置がjで得点がkである確率
dp = [[[0] * (200) for _ in range(50)] for _ in range(n + 1)]

# 最初は石の位置が0で、得点が0
dp[0][0][0] = 1

for i in range(n):
    for j in range(3*(i+1)+1):
        for k in range(3*n*(n+1)//2+1):
            # i回コインを投げて、石の位置がjであって、得点がkである場合からの遷移を考える
            # i + 1回目のコイン投げで表が出た場合、
            # 石の位置は2進み、得点はその時点での石の位置であるj + 2が可算される
            dp[i + 1][j + 2][k + j + 2] += dp[i][j][k] * (1 / 2)

            # i+1回目のコイン投げで裏が出た場合,
            # 石の位置は3進み、得点はその時点での石の位置である j+3 が可算される
            dp[i + 1][j + 3][k + j + 3] += dp[i][j][k] * (1 / 2)

count1 = 0  # 得点が100である確率
count2 = 0  # 得点が奇数である確率

for j in range(3 * n + 1):
    for k in range(3 * n * (n + 1) // 2 + 1):

        if j == 2 * n + 2 and k == 100: # 得点が100であるときをカウント
            count1 += dp[n][j][k]

        if j == 2 * n + 2 and k % 2 == 1: # 得点が奇数であるときをカウント
            count2 += dp[n][j][k]


print(f"得点が100である確率 : {count1} = {Fraction(count1).limit_denominator(1000)}") # 約1 / 128
print(f"得点が奇数である確率 : {count2} = {Fraction(count2).limit_denominator(1000)}") # 約5 / 128
