# 数値
print(3.34e+2)  # 334.0

print('12 × 12 =' + str(12 * 12))  # 12 × 12 = 144
print('100 ÷ 3 =' + str(100 / 3))  # 100 ÷ 3 = 33.333333…
print('100 ÷ 3 =' + str(100 // 3))  # 100 ÷ 3 = 33
print('100を3で割ったあまりは' + str(100 % 3))  # 余り1
print('32の2乗は' + str(32 ** 2))  # 1024,累乗の計算
print("\n")
# ビット値
# 10進数を2進数に変換して出力する記述
num = 10
binary_num = format(num, 'b')
print(f"{num}は2進数では{binary_num}")
# 2進数を10進数に変換
num_bit = "101000"
decimal_num = int(num_bit, 2)
print(f"{num_bit}は10進数では{decimal_num}")
del decimal_num  # 変数を削除する
# 10=>1010, 13=>1101
# |：片方でもが1の場合は1を返すので1111
print("10 | 13 = " + str(10 | 13))  # 10 | 13 = 15

# &：どちらも1の場合は1を返すので1000
print("10 & 13 = " + str(10 & 13))  # 10 & 13 = 8

# ^：片方のみが1の場合は1を返すので0111
print("10 ^ 13 = " + str(10 ^ 13))  # 10 ^ 13 = 7

# <<：右辺の数だけ左へシフトされる, 1ビットごとに値は2倍
print("10を左へ2ビットシフトすると" + str(10 << 2))  # 40

# >>：右辺の数だけ右へシフトされる, 1ビットごとに値は0.5倍
print("80を右へ2ビットシフトすると" + str(80 >> 2))  # 20
print('\n')

# trueは1, falseは0と等価
flag = True
if (flag):
    print(True + 3)  # ここでは数値の1
    print(str(True) + " is 1")  # ここではTrueの文字列
else:
    print(False + 2)
    print(str(False) + " is 0")
