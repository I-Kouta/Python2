# 基本情報の問題をコードにしてみる

# 2で割ることを繰り返す、奇数変換の流れ図
def bin(x):
    x_after = []
    while x >= 1:
        mod = x % 2 # xを2で割った余りを格納する(0 or 1)
        x_after.append(mod) # xを2で割った余り(0 or 1)を配列に格納する
        x //= 2 # xを2で割る(切り捨て)
    return x_after[::-1] # 表示させる順番を入れ替える

x = 250
x_after = bin(x)
print(f"{x}を2進数に変換すると{x_after}")
