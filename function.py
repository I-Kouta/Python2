# 関数で解く
from sympy import Symbol, integrate, solve
# 二次関数で囲まれた面積を求める

# 関数の定義
x = Symbol("x")
f1 = x**2 - 1
f2 = -x**2 + 1


def enclosed_area(a, b):
    # 交点を求める
    intersection_points = solve(f1 - f2, x)
    intersection_points = [float(point) for point in intersection_points]
    # 交点を範囲に反映
    if a < intersection_points[0] < b:
        a = intersection_points[0]
    if a < intersection_points[1] < b:
        b = intersection_points[1]

    area = integrate(f2 - f1, (x, a, b))
    return area


print(f"交点(x座標):{solve(f1 - f2, x)}")
print(f"面積:{abs(enclosed_area(-1, 1))}")
