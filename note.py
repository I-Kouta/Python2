# 算数・数学
import sympy
import math
import itertools
from sympy import sin, cos, tan, log
from fractions import Fraction

x = sympy.Symbol("x")  # sympy.Symbol()で定義
y = sympy.Symbol("y")
print(type(x), "\n")
expr = x**2 + y + 1
print(expr)
print(f"xに1を代入:{expr.subs(x, 1)}")
print(f"xにyを代入:{expr.subs(x, y)}")
del expr

expr = (x - 3) ** 2
expr_ex = sympy.expand(expr)
print(f"{expr} = {expr_ex}")

expr_factor = sympy.factor(expr_ex)
print(f"{expr_ex} = {expr_factor}")
print(f"{expr_ex}=0の解:{sympy.solve(expr_ex)}")

expr1 = x + y - 7
expr2 = 3 * x + 5 * y - 29
print(sympy.solve([expr1, expr2]))  # {x: ?, y: ?}

expr3 = x**3 + 2*x**2 - x + 2
expr3_1 = sympy.diff(expr3)
print(f"({expr3})' = {expr3_1}")
print(f"∮({expr3_1}) = {sympy.integrate(expr3_1)}", "\n")

print(sympy.diff(sin(x)))  # cos(x)
print(sympy.diff(cos(x)))  # -sin(x)
print(sympy.diff(tan(x)))  # tan(x)**2 + 1
print(sympy.diff(sympy.exp(x)))  # exp(x)
print(sympy.diff(log(x)), "\n")  # 1/x
print(sympy.integrate(sin(x)))  # -cos(x)
print(sympy.integrate(cos(x)))  # sin(x)
print(sympy.integrate(tan(x)))  # -log(cos(x))
print(sympy.integrate(sympy.exp(x)))  # exp(x)
print(sympy.integrate(log(x)), "\n")  # x*log(x) - x

pi = Fraction(3.14159265359)
e = Fraction(2.71828182846)
print(pi.limit_denominator(100))  # 分母がこの値以下の分数を返す
print(e.limit_denominator(1000), "\n")  # 分母がこの値以下の分数を返す

lcm = math.lcm(4, 6, 5)
gcd = math.gcd(4, 6, 5)
print(f"最小公倍数は{lcm}")
print(f"最大公約数は{gcd}", "\n")

factorial = 4
print(f"{factorial}! = {math.factorial(factorial)}")  # math.factorial(階乗のメソッド)
print(f"n個からk個選んで並べる,いわゆるP:{math.perm(4, 2)}")
print(f"n個からk個選ぶ,いわゆるC:{math.comb(4, 2)}", "\n")

l = ["a", "b", "c", "d"]
for v in itertools.permutations(l, 2):
    print(v)

v = "arc"
v_list = list(itertools.permutations(v, 2))
print(v_list)  # lから2つを取得するのは同じ
print(len(v_list), "\n")

Pi = math.pi  # 円周率
print(Pi)
print(math.degrees(Pi))  # ラジアン(弧度法)→度に変換(180.0)
print(math.radians(180))  # 度→ラジアンに変換(3.14…)

radian45 = math.radians(45)  # π/4
print(math.sin(radian45))  # 0.7071…
print(math.cos(radian45))
print(math.tan(radian45), "\n")  # 約1

sin30 = math.asin(0.5)
cos60 = math.acos(0.5)
tan45 = math.atan(1)
print(math.degrees(sin30))  # 約30
print(math.degrees(cos60))  # 約60
print(math.degrees(tan45), "\n")  # 45

print(math.e)  # 自然対数
print(pow(3, 4))
print(math.pow(2, 10))  # どちらも**べき乗と同様
print(pow(2, 4, 5), "\n")  # (x ** y) % zと同様
print(math.sqrt(2))  # **0.5と同様
