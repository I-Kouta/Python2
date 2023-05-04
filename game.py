# 1.リストの要素の平均値を求める
def mean(numbers):
    ave = sum(numbers) / len(numbers)
    num = len(numbers)
    print(f"{num}つの要素の平均値は{ave}です")


mean([1, 2, 3, 4, 5])
# 2.内積を求める


def dot_product(list1, list2):
    sumProduct = sum([x * y for x, y in zip(list1, list2)])
    print(f"{inner_productA}と{inner_productB}の内積は{sumProduct}です")


inner_productA = [1, 2, 3]
inner_productB = [4, 5, 6]
dot_product(inner_productA, inner_productB)
# 3.回文かどうか判定する


def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s}は回文です")
    else:
        print(f"{s}は回文ではありません")


is_palindrome("eye")
# 4.フィボナッチ数列のn番目を求める(sequence)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, …
# フィボナッチ数列のn番目までの総和を求める
# 指定した値がフィボナッチ数列に含まれるか認識し、含まれる場合は総和を求める
# 値が含まれる場合はそこまでの配列と和を求める
print("\n")


def sequence(n):
    if n < 2:
        return n
    else:
        return sequence(n-2) + sequence(n-1)  # 重複を防ぐ,先に小さい値を計算する


def sequence_sum(n):
    sequence_list = [sequence(i+1) for i in range(n+1)]  # ここの+1を削除すると0からの数列になる
    sequence_sum = sum(sequence_list[::-1])
    print(f"{n}番目までのフィボナッチ数列は{sequence_list}です")
    print(f"{n}番目までのフィボナッチ数列の総和は{sequence_sum}です")


sequence_sum(5)

# 5.リスト内で最大値・最小値・中央値を求める


def find_min_max(numbers):
    if len(numbers) == 0:
        print("要素がありません")
    else:
        sorted_numbers = sorted(numbers)  # 要素を昇順にする
        n = len(sorted_numbers)  # 変数に昇順された要素の数を代入
        if n % 2 == 0:  # 要素数が偶数の場合
            median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2  # インデックス番号 + 1が値の個数目
        else:  # 要素数が奇数の場合
            median = sorted_numbers[n // 2]
        print(
            f"要素:{len(numbers)} 最小値:{min(numbers)} 最大値:{max(numbers)} 中央値:{median}")


find_min_max([2, 5, 6, 1, 5])
