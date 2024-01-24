# 2進数, 10進数, 16進数を変換する
# python num2.py

# 10進数を16進数に変換する
a = 255

# 解法1: hexを使う。出力結果に16進数を表す「0x」が先頭に付く
hex = hex(a)
print(f"{a}をhexを使って16進数に変換すると「{hex}」")

# 解法2: formatを使う。「0x」は付かない
format = format(a,"x")
print(f"{a}を1formatを使って6進数に変換すると「{format}」")
