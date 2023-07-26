# 185,クラス定義から(python basic04.py)
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
# 226から
