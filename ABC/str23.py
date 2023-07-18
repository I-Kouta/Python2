# 書式演算子%を使った文字列の書式設定,index23以降
num1 = 1023
result = '10進数では%d,16進数では%xです' % (num1, num1)
print(result)
print("10進数では%d,16進数では%xです" % (num1, num1))

# 変換指定子：%(マップキー) 変換フラグ 最小フィールド幅 精度 精度長変換子 変換型(これだけ必須)
# d:10進数、x:16進数など


def mypoint(str2, num2):
    result = "%-10sです, 得点は%5dです" % (str2, num2)
    print(result)


mypoint("Yamada", 75)
mypoint("Sugiyama", 1825)

print("{:,d}は、{}".format(100000, "10万です"))

# 省略版
number = 12340000
message = '1234万です'
print(f'{number:,d}は{message}です')
