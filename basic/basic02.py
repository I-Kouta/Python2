# 仕様・テスト・デバッグ(python basic02.py)
def square(x):
    return x ** x
a = -2
assert square(a) >= 0 # 条件式が真であることを宣言, 偽ならプログラム停止(AssertionError)
