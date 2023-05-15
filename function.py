# 関数で解く
from sympy import Symbol, integrate
# 二次関数で囲まれた面積を求める

# 関数の定義
x = Symbol("x")
f1 = x**2 - 1
f2 = -x**2 + 1


def enclosed_area(a, b):
    area = integrate(f2 - f1, (x, a, b))
    return area


# 面積の計算
a = 1
b = -1
enclosed_area(a, b)
print(f"面積:{abs(enclosed_area(a, b))}")
