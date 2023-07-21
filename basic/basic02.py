# 仕様・テスト・デバッグ(python basic02.py)
def square(x):
    return x ** x
a = -2
assert square(a) >= 0 # 条件式が真であることを宣言, 偽ならプログラム停止(AssertionError)

def median(x, y, z): # 中央値を算出する
    if x > y:
        w = x
        x = y
        y = w # x, yを入れ替えている
    if x > z:
        return x
    if y > z:
        return z
    return y
assert median(3, 1, 2) == 2

word1 = "subtitle"
substr1 = "le"
substr2 = "me"
print(substr1 in word1) # true
print(substr2 in word1) # false
