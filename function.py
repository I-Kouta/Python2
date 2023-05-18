# 関数で解く
from sympy import Symbol, integrate, solve
from sympy.plotting import plot
import matplotlib.pyplot as plt
from fractions import Fraction
# 二次関数で囲まれた面積を求める

# 関数の定義
x = Symbol("x")
f1 = -(x - 2)**2 + 9  # -(x + 1)(x - 5) = -x**2 + 4*x + 5
f2 = (x - 3)**2 - 9  # x**2 - 6x = x(x - 6)
# [5/2 - sqrt(35)/2, 5/2 + sqrt(35)/2]:sqrt(35)は約5.9


def enclosed_area():
    # 交点を求める
    intersection_points = solve(f1 - f2, x)
    intersection_points = [float(point) for point in intersection_points]
    # 面積の計算
    area = integrate(f2 - f1, (x, intersection_points[0], intersection_points[1]))
    return area


# グラフ表示
p1 = plot(f1, f2, show=False)

# 囲まれた範囲に色を付ける

print(f"交点(x座標):{solve(f1 - f2, x)}")

print(f"面積(返り値):{enclosed_area()}")  # 小数、負の値の場合がある
process1 = abs(enclosed_area())  # 絶対値に変換
process2 = str(process1)  # 文字列を数値に変換
process3 = Fraction(process2).limit_denominator(100)  # 小数を分数に変換
print(f"面積(処理後):{process3}")

# 関数の式を表示
p1[0].line_color = "blue"
p1[1].line_color = "green"
p1[0].label = f1
p1[1].label = f2
p1.legend = True

p1.show()  # これが実際にグラフを表示させる。ここより下にコードは書かない
