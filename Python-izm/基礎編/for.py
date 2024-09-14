# python for.py

sample = []
sample.append("1つめ")
sample.append("---")
sample.append("2つめ")
sample.append("---")
sample.append("3つめ")
sample.append("---")

for val in sample:
    print(val)

print("\n")

# while文
count = 0
while count < 30:
    count += 1
    if count % 3 == 0 and count % 5 == 0:
        print("fizzBuzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)

print("\n")

# continue
for count in range(100):
    if count % 10: # 10で割った余りは次の処理へ
        continue
    print(count) # 10で割り切れる場合のみ表示

print("\n")

# range, xrange

for i in range(2, 10): # 出力は2から9
    print(i)

print("\n")

# 例外処理

def exception(val1, val2):
    print("計算開始")
    result = 0
    try:
        result = val1 + val2
    except: # エラーがなければ処理されない
        print("計算不能")
    finally: # 例外の有無に関わらず必ず実行される
        print("計算終わり")
    return result

print(exception(100, 200)) # try, finally, return
print(exception(100, "200")) # except, finally, return
