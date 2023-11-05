# 10進数を変換する(python bin.py)
num = 25
binary_num = format(num, '08b')
binary_hex = format(num, 'x')
print(f"{num}は2進数では{binary_num}")
print(f"{num}は16進数では{binary_hex}")
print("\n")

# 2進数を10進数に変換
num_bin = "11111110"
decimal_num = int(num_bin, 2)
print(f"{num_bin}は10進数では{decimal_num}")
