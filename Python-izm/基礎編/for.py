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

# continue
for count in range(100):
    if count % 10: # 10で割った余りは次の処理へ
        continue
    print(count) # 10で割り切れる場合のみ表示
