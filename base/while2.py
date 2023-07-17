# for文を使った繰り返し
setList = ["edge", "Tiny Baby", "Hurly Burly"]
for list in setList:
    print(list)
else:
    print("\n")

count = 0
list = {"e": "edge", "T": "Tiny Baby", "H": "Hurly Burly"}
for initial, value in list.items():
    print(str(count + 1) + "曲目：" + initial + ",曲：" + value)
    count += 1
else:
    print("曲数：" + str(count))

num = 1
times = 10
for i in range(times):
    old = num
    num *= 2
    print(str(old) + "×2=" + str(num))
else:
    print(str(times) + "回繰り返して合計は" + str(num) + "で終了")

del num

# breakで終了させる
num = 50
while True:
    print("num = " + str(num))
    num -= 10
    if num < 10:
        break
print("\n")

# continueで処理をスキップさせられる
total = 0
for number in [10, 20, "30", 40, "pass", 60]:
    if isinstance(number, str):
        continue  # 文字型の要素は出力しない
    print("num=" + str(number))
    total += number
print("Total = " + str(total))
