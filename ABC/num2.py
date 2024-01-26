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
    powers_list_bin = [] # 2進数を返すためのリスト

    power = 128
    while power > 0: # 足す値が1になるまで繰り返す
        if power <= n: # 与えられた値よりもpowerが小さければリストに入れる
            powers_list.append(power)
            powers_list_bin.append(1) # 2進数の出力結果には1を格納
            n -= power # 与えられた値から2のべき乗の値を引く
        else:
            powers_list_bin.append(0) # 2進数の出力結果には0を格納
        power //= 2 # 2のべき乗を2で割る
    return powers_list, powers_list_bin

decimal_number = 250
powers_result = decimal_to_powers(decimal_number)
print(f"{decimal_number}の各2のべき乗: {powers_result}")
