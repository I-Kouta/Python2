# 文字列の出現回数をカウントする
def count_occurrences(string, target):
    count = 0
    # 文字列をループさせて出現した回数を数える
    for char in string:
        if char == target:
            count += 1
    if count == 0:
        print(f"{string}に{target}は含まれていません")
    else:
        print(f"{string}に{target}は{count}つ含まれます")


count_occurrences("perfume", "e")
print("\n")
# リストの重複を削除する
# list:ただの集合をリストに変換
# set:重複している要素を削除


def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    print(f"{numbers}から重複を除いた結果は{unique_numbers}です")


remove_duplicates([5, 4, 3, 2, 1, 2, 3, 4, 5])
print("\n")
# 指定した文字列を取り除く・置き換える


def remove_string(s, target):
    new_s = s.replace(target, "")  # ""内の文字に置き換える
    print(f"{s}から{target}を取り除いた結果は{new_s}です")


remove_string("safari", "a")
print("\n")
# 要素を逆順にする(文字列も可)


def reverse_list(numbers):
    reverse_numbers = numbers[::-1]
    print(f"{numbers}を逆順にすると{reverse_numbers}です")


reverse_list([1, 2, 3, 4, 5])
print("\n")
# 辞書型データをソートする


def sort_dictionary(d):
    sort_d = dict(sorted(d.items(), key=lambda x: x[1]))
    print(f"ソート前の辞書:{d}")
    print(f"値に基づいてソートされた辞書:{sort_d}")


sort_dictionary({"a": 2, "b": 1, "c": 3})
print("\n")
# フィボナッチ数列のn項目を求める
# 1から始まる場合(1, 1, 2, 3, 5, 8, 13, …)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


n = 9
sequence_sum = fibonacci(n)
print(f"1から始まるフィボナッチ数列の{n}番目の値は{sequence_sum}です")
print("\n")
# 0から始まる場合(0, 1, 1, 2, 3, 5, 8, 13, …),0項目は0


def fibonacci_zero(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 2) + fibonacci(m - 1)


m = 0
sequence_sumM = fibonacci(m)
print(f"0から始まるフィボナッチ数列の{m}番目の値は{sequence_sumM}です")
print("\n")
# 整数が素数かどうか判別する
# 49の場合→range内は2から8
# i = 7のとき、if文内が成立する
# 13の場合→range内は2, 3, 4
# いずれの値でもif文内が成立しないため素数


def is_prime(n):
    if n < 2:
        print(f"2未満の数値は素数ではありません")
    for i in range(2, int(n ** 0.5) + 1):  # n ** 0.5：nの平方根
        if n % i == 0:
            print(f"{n}は素数ではありません")
    print(f"{n}は素数です")


is_prime(7)
print("\n")
# n個目までの素数を配列で出力：エラトステネスの篩


def get_prime(n):
    prime_numbers = [2]
    current_number = 3
    while len(prime_numbers) < n:
        is_primes = True
        for divisor in range(2, int(current_number ** 0.5) + 1):
            if current_number % divisor == 0:
                is_primes = False
                break
        if is_primes:
            prime_numbers.append(current_number)
        current_number += 2
    print(prime_numbers)


get_prime(10)
print("\n")
# 整数2つの最大公約数・最小公倍数を求める


def gcd(a, b):
    if a < b:
        a, b = b, a  # 常にaが大きくなるように入れ替える
    while b != 0:
        a, b = b, a % b  # (12, 8)→(8, 4)、(8, 4)→(4, 0)
    return a


numA = 8
numB = 12
result = gcd(numA, numB)
lcm = (numA*numB) // result
print(f"{numA}と{numB}の最大公約数は{result}です")
print(f"{numA}と{numB}の最小公倍数は{lcm}です")
