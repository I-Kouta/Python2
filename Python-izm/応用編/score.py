
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
iteration = 10000 # 試行回数
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
