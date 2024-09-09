# python integer.py

string = "100"
result = int(string) + 300 # 文字を数値に変換している
print("100 + 300 = " + str(result)) # 数値を文字に変換して結合している

# 浮動小数点
num = "100.5"
result = float(num) + .5 # 整数部分が0なら省略可
print(str(num) + " + 0.5 = " + str(result))

# 複素数
complex = 100 + 5j
print(complex.real) # 実部
print(complex.imag) # 虚部
