import locale
import unicodedata
import heapq
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
print(searchResult, "\n")
# クイックソートアルゴリズム


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


quicksortResult = quicksort([10, 21, 32, 34, 43, 98])
print(quicksortResult, "\n")
# ダイクストラアルゴリズム


def dijkstra(edges, start, end):
    graph = {}
    for a, b, cost in edges:  # aに始点, bに終点, cにコスト
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = cost
        graph[b][a] = cost

    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return (cost, path)
            for next_node in graph[node]:
                if next_node not in visited:
                    heapq.heappush(heap, (cost + graph[node][next_node], next_node, path))
    return -1


edges = [(1, 2, 7), (1, 3, 4), (1, 4, 3), (2, 3, 1), (2, 5, 2), (3, 5, 6), (4, 5, 5)]  # 始点, 終点, コスト
start = 1
end = 5
print(dijkstra(edges, start, end), "\n")

# 演算子の違い
a = [1, 2, 3]
b = a
a = a + [4]
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3]

print("\n")

c = [1, 2, 3]
d = c
c += [4]
print(c)  # [1, 2, 3, 4]
print(d)  # [1, 2, 3, 4]
print("\n")
# 動的計画法：指定された容量以内で最大の価値になる組み合わせを探す


def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = 3
opt_val = knapsack(W, wt, val, n)
print(f"最適な書価値の合計:{opt_val}")
# ハッシュマップ
