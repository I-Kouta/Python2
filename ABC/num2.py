# 2進数, 10進数, 16進数を変換する
# python num2.py

# 16進数を10進数に変換する
a ="0xff" # 0xは無くても良い
# intを使う
intDecimal = int(a, 16) # ここで16進数が10進数に変換される
print(f"{a}を10進数に変換すると「{intDecimal}」\n")

# 10進数を2進数に変換する
changeBin = bin(intDecimal)
# 解法1: binを使うと出力結果に2進数を表す「0b」が先頭に付く
print(f"{intDecimal}をbinを使って2進数に変換すると「{changeBin}」")
# 解法2: formatを使うと「0b」は付かない
formatBin = format(intDecimal,"b")
print(f"{intDecimal}をformatを使って2進数に変換すると「{formatBin}」\n")

# 2進数を10進数に変換する
binary_num = "11111100"
intBin = int(binary_num, 2)
print(f"{binary_num}をformatを使って16進数に変換すると「{intBin}」\n")

# 10進数を16進数に変換する
# 解法1: hexを使うと出力結果に16進数を表す「0x」が先頭に付く
hex = hex(intBin)
print(f"{intBin}をhexを使って16進数に変換すると「{hex}」")
# 解法2: formatを使うと「0x」は付かない
formatHex = format(intBin,"x")
print(f"{intBin}をformatを使って16進数に変換すると「{formatHex}」\n")

# 与えられた値を2進数に変換するプロセス
def decimal_to_powers(n):
    powers_list = []

    # 2のべき乗を求める
    power = 1
    while power <= n:
        powers_list.append(power)
        n -= power
        power *= 2
    return powers_list

# テスト
decimal_number = 155
powers_result = decimal_to_powers(decimal_number)
print(f"{decimal_number}の各2のべき乗: {powers_result}")
