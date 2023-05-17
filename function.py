# 関数で解く
from sympy import Symbol, integrate, solve
from sympy.plotting import plot
from fractions import Fraction
# 二次関数で囲まれた面積を求める

# 関数の定義
x = Symbol("x")
f1 = -x**2 + 1
f2 = x**2 - 1


def enclosed_area():
    # 交点を求める
    intersection_points = solve(f1 - f2, x)
    intersection_points = [float(point) for point in intersection_points]
    # 面積の計算
    area = integrate(f2 - f1, (x, intersection_points[0], intersection_points[1]))
    return area


print(f"交点(x座標):{solve(f1 - f2, x)}")

print(f"面積(返り値):{enclosed_area()}")  # 小数、負の値の場合がある
process1 = abs(enclosed_area())  # 絶対値に変換
process2 = str(process1)  # 文字列を数値に変換
process3 = Fraction(process2).limit_denominator(100)  # 小数を分数に変換
print(f"面積(処理後):{process3}")

# グラフ表示
p1 = plot(f1, f2, show=False)
p1.show()
