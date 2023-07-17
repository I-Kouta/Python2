# 繰り返し処理
num = 1  # この値から
last = 45  # この値まで
sum = 0  # 最初は0からスタート
print(str(num) + "から" + str(last) + "までの総和を算出")
while num <= last:  # いくつまで
    sum += num  # 右辺の処理をして繰り返す
    num += 1  # 1ずつ増やしていく
else:
    print("計算結果は" + str(sum) + "です\n")

# 1から数えて逆数の和が8を越えるのはいくつか
reciprocal_ans = 0
reciprocal_n = 0
while reciprocal_ans < 8:  # これを越える値
    reciprocal_n += 1
    reciprocal_ans += 1/reciprocal_n
else:
    print(str(reciprocal_n) + "までの逆数の総和は" + str(reciprocal_ans) + "です")
    number = str((reciprocal_ans - 1 / (reciprocal_n)))  # 1行にまとめたいので変数にします
    print(str(reciprocal_n - 1) + "までの逆数の総和は" + number + "となり、目的の値に最も近づきます\n")

# 1から数えて和が1000を越えるのはいくつか
ans = 0
n = 0
while ans < 1000:  # これを越える値
    n += 1
    ans += n  # ここで値の処理を記述(足す、累乗にするなど)
else:
    print(f"{n}まで足すと総和は{ans}となり、目的の値を超えます")
    print(str(n-1) + "まで足すと総和は" + str(ans-n) + "です\n")

# コラッツ予想
# 1.偶数は半分にする
# 2.奇数は3倍して1を足す


def conjecture(n):
    count = 0
    while n != 1:
        if n % 2 == 0:  # (偶数の場合)
            n //= 2  # 奇数だと//だと切り捨て
        else:  # (奇数の場合)
            n = n * 3 + 1  # 3倍して1足す
        count += 1
        print(str(count) + "回目の処理で値は" + str(n) + "です")
    print(f"初期値{initial_value}は{count}回の処理で1になります")


initial_value = 23
conjecture(initial_value)
