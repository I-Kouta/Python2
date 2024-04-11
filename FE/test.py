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

print("\n")

# 斜辺の長さを求める
def calc(a, b):
    calcResult = pow(pow(a, 2) + pow(b, 2), 1 / 2) # powメソッド : 第一引数の第二引数乗
    return calcResult

a = 1
b = pow(3, 0.5)
result = calc(a, b)
print(f"底辺と高さが{a}, {b}の直角三角形の斜辺の長さは{result}")

print("\n")

# fizzBuzz問題
for i in range(1, 31):
    if i % 15 == 0: # 15で割り切れる場合
        print("fizzBuzz")
    elif i % 3 == 0: # 3で割り切れる場合
        print("fizz")
    elif i % 5 == 0: # 5で割り切れる場合
        print("Buzz")
    else:
        print(i)

print("\n")

# 最大公約数を求める(ユークリッドの互除法)

def gcd(x, y):
    while x != y:
        if x > y:
            x, y = y, x - y
        else:
            x, y = y , y - x
    return x

num1 = 36
num2 = 60
result = gcd(num1, num2)
print(f"{num1}, {num2}の最大公約数は{result}")

print("\n")

# 二分探索アルゴリズム
def binary_search(arr, x):
    left = 0  # 探索の右端
    right = len(arr) - 1  # 探索の左端
    while left <= right:
        mid = (left + right) // 2  # 探索範囲の中央を計算
        if arr[mid] < x:  # 中央の値よりxが大きい場合
            left = mid + 1  # 探索範囲の右を変える
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid + 1  # midはインデックス番号
    return -1 # 配列に存在していない場合


data = [10, 20, 30, 40, 50, 60]
dataX = 30
array = sorted(data)  # [10, 21, 32, 34, 43, 98]
searchResult = binary_search(array, dataX)
print(f"配列の{searchResult}番目に値が含まれている")
