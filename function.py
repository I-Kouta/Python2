# 関数で解く
from sympy import Symbol, integrate, solve
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
# グラフの交点
intersection_points = solve(f1 - f2, x)
print(f"交点:{intersection_points}")
print(f"面積:{abs(enclosed_area(intersection_points))}")
