# 185,クラス定義から(python basic04.py)
import random
class HelloFile:
    def __init__(self, n): # 初期化のメソッド
        self.n = n # オブジェkとのnという名前の属性を表す(右辺はメソッドの引数)

    def readline(self):
        if self.n == 0:
            return ""
        self.n = self.n - 1
        return "Hello.\n"
f = HelloFile(3) # オブジェクト作成, 3がnに渡される
print(f.readline())

# 224, 再帰関数の例
def prefixes(s):
    if s == "":
        return []
    else:
        return [s] + prefixes(s[:-1]) # 接頭辞リストを返す
        # return [s] + prefixes(s[1:]) # 接尾辞リストを返す
print(prefixes("abcde"), "\n")

# べき乗の計算
def power(base, expt):
    if expt == 0:
        return 1 # 0乗であれば1を返す
    else:
        # return base * power(base, expt - 1) # こっちだと再帰的
        return base ** expt

# 繰り返し処理だとこうなる
def power2(base2, expt2):
    e = 1
    for i in range(expt2):
        e *= base2
    return e

print(power(2, 10))
print(power2(2, 10))

# マージソート
def merge_sort_rec(data, l, r, work):
    n = 0
    if r - l <= 1:
        return n
    m = l + (r - l) // 2
    n1 = merge_sort_rec(data, l, m, work)
    n2 = merge_sort_rec(data, m, r, work)
    i1 = l
    i2 = m
    for i in range(l, r):
        from1 = False
        if i2 >= r:
            from1 = True
        elif i1 < m:
            n = n + 1
            if data[i1] <= data[i2]:
                from1 = True
        if from1:
            work[i] = data[i1]
            i1 = i1 + 1
        else:
            work[i] = data[i2]
            i2 = i2 + 1
    for i in range(l, r):
        data[i] = work[i]
    return n1 + n2 + n

def merge_sort(data):
    return merge_sort_rec(data, 0, len(data), [0] * len(data))

a = [random.randint(1, 10000) for i in range(100)]
print(merge_sort(a))
