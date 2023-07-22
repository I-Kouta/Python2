# 条件分岐(python basic03.py)
import random
import matplotlib.pyplot as plt

def exception3(x, y, z):
    if x == y:
        return z
    elif y == z:
        return x
    elif z == x:
        return y
    else:
        return x + y + z

print(exception3(1, 1, 2))

def random_sequence(length): # ランダム文字列を生成する
    string = "ATCG"
    sequence = "".join(random.choice(string) for _ in range(length))
    return sequence

sequence = random_sequence(50)
print(sequence)
height = [0] * 4
for c in sequence:
    if c =="A":
        height[0] += 1
    elif c =="T":
        height[1] += 1
    elif c =="C":
        height[2] += 1
    elif c =="G":
        height[3] += 1

print(height)
plt.plot(height)
plt.show()
