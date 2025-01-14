
# python math.py
# 表と裏が出る確率それぞれ1 / 2のコインをn回投げ得点を決める
# 最初に数直線上の原点に石を置き、表なら2、裏なら3だけ数直線上を正方向に石を移動
# an ≠ 2n + 2の場合は得点0、an = 2n + 2の場合は得点をa1 + a2 + ... + anとする

import random

# 1.n回のうち裏の出る回数をrとした時のan
# an = 3r + 2(n - r) = 2n + r
