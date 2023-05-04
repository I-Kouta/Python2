# 階乗を行う
import locale
import unicodedata
locale.setlocale(locale.LC_COLLATE, 'ja_JP.UTF-8')


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


m = 5
resultFactorial = factorial(m)
if m <= 0:
    print(f"0以下の値が与えられています")
else:
    print(f"{m}の階乗は{resultFactorial}です")
print("\n")
# 文字列をアルファベット準にソート
strings = ["game", "cling cling", "Story", "fusion"]
sort_strings = sorted(strings, key=str.lower)  # key=str.lowerで大文字小文字を区別しない
print(sort_strings)

# 日本語は、平仮名→カタカナ→漢字の順
stringsB = ["日本語", "アイスクリーム", "神奈川県", "いーぶい"]


sort_stringsB = sorted(
    stringsB, key=lambda s: unicodedata.normalize('NFKC', s).lower())
print(sort_stringsB)
print("\n")
# 文字列を並び替えて等しくできるか


def can_rearrange_to_t(s, t):
    return sorted(s) == sorted(t)


s = "abc"
t = "bca"
if can_rearrange_to_t(s, t):
    print("yes")
else:
    print("no")
print("\n")
# 整数a, bの積が偶数か奇数かを識別→3 3のように入力
a, b = map(int, input().split())
if (a * b) % 2 == 0:
    print("even")
else:
    print("odd")
print("\n")
# 二分探索アルゴリズム


def binary_search(arr, x):
    left = 0  # 探索の右端
    right = len(arr) - 1  # 探索の左端
    while left <= right:
        mid = (left + right) // 2  # 探索範囲の中央を計算
        if arr[mid] < x:  # 中央の値よりxが大きい場合
            left = mid + 1  # 探索範囲の右を変える
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid + 1  # midはインデックス番号
    return -1


data = [10, 34, 43, 21, 98, 32]
dataX = 98
array = sorted(data)  # [10, 21, 32, 34, 43, 98]
searchResult = binary_search(array, dataX)
print(searchResult)
