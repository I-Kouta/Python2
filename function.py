# 関数で解く
from sympy import Symbol, integrate, solve
from fractions import Fraction
# 二次関数で囲まれた面積を求める

# 関数の定義
x = Symbol("x")
f1 = x**2 - 1
f2 = -x**2 + 1


def enclosed_area():
    # 交点を求める
    intersection_points = solve(f1 - f2, x)
    intersection_points = [float(point) for point in intersection_points]
    # 面積の計算
    area = integrate(f2 - f1, (x, intersection_points[0], intersection_points[1]))
    return area


print(f"交点(x座標):{solve(f1 - f2, x)}")
graphArea = Fraction(str(abs(enclosed_area()))).limit_denominator(100)  # 文字列型にしてから分数にする
print(f"面積:{graphArea}")
