# 2進数, 10進数, 16進数を変換する
# python num2.py

# 10進数を16進数に変換する
a = 255
# 解法1: hexを使うと出力結果に16進数を表す「0x」が先頭に付く
hex = hex(a)
print(f"{a}をhexを使って16進数に変換すると「{hex}」")
# 解法2: formatを使うと「0x」は付かない
formatHex = format(a,"x")
print(f"{a}をformatを使って6進数に変換すると「{formatHex}」\n")

# 10進数を2進数に変換する
bin = bin(a)
# 解法1: binを使うと出力結果に2進数を表す「0b」が先頭に付く
print(f"{a}をbinを使って2進数に変換すると「{bin}」")
# 解法2: formatを使うと「0b」は付かない
formatBin = format(a,"b")
print(f"{a}をformatを使って6進数に変換すると「{formatBin}」\n")

# 16進数を10進数に変換する
b ="0xf0" # 0xは無くても良い
# intを使う
int = int(b, 16)
print(f"{b}を10進数に変換すると「{int}」\n")
