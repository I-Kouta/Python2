# 算数・数学
import sympy
import math
import cmath
import itertools
import statistics
import collections
import random
import numpy as np
from sympy import sin, cos, tan, log
from fractions import Fraction
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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
print(math.exp(2))  # 自然対数の累乗
print(math.log(25, 5))  # (x, y)→yを底としたxの対数
print(math.log10(10))  # 10を底としたxの対数(常用対数)
print(math.log2(1024), "\n")  # 2を底としたxの対数(二進対数)

c = 1 + 2j
print(c)
print(f"実部:{c.real}")
print(f"虚部:{c.imag}")
print(f"共役:{c.conjugate()}")
print(f"絶対値:{abs(c)}, \n")

print(math.atan2(c.imag, c.real))
print(cmath.phase(c))  # どちらも同じ
print(math.degrees(cmath.phase(c)))  # 角度を取得
print(f"(絶対値, 偏角) = {cmath.polar(c)} \n")

m = [10, 1, 3, 7, 1]
print(f"平均:{statistics.mean(m)}")
print(f"調和平均:{statistics.harmonic_mean(m)}")  # 逆数の平均の逆数
print(f"最頻値:{statistics.mode(m)}")
print(f"母分散:{statistics.pvariance(m)}")  # 個々のデータが平均からどれくらい離れているか,データと平均の差を数で割る
print(f"標準偏差:{statistics.pstdev(m)}")  # 母分散の平方根
print(f"不偏分散:{statistics.variance(m)}")
print(f"標本標準偏差:{statistics.stdev(m)} \n")  # 不偏分散の平方根
# 素因数分解


def prime_factorize(n):
    a = []
    while n % 2 == 0:  # 偶数の場合,配列に2を加えて値を2で割る
        a.append(2)
        n //= 2
    f = 3
    while f ** 2 <= n:  # 与えられた値が9以下の場合
        if n % f == 0:  # 3の倍数の場合,3を加えて値を3で割る
            a.append(f)
            n //= f
        else:
            f += 2  # 3の倍数でなければ3に2を足す
    if n != 1:
        a.append(n)
    return a


print(prime_factorize(1024), "\n")

c = collections.Counter(prime_factorize(84))
print(c.items())  # 素因数分解の値と個数を取得


def random_range(start, end):  # ランダムな値を出力
    return random.sample(range(start, end+1), 3)


print(random_range(1, 100), "\n")

matrixA = np.array([[1, 2], [3, 4]])
matrixB = np.array([[5, 6], [7, 8]])

print(f"行列の和:{matrixA + matrixB}")
print(f"行列の差:{matrixA - matrixB}")
print(f"行列の積:{np.dot(matrixA,  matrixB)}")  # [19 22] [43 50]
# 内積によって計算
# 19 = 1 * 5 + 2 * 7
# 22 = 1 * 6 + 2 * 8
# 43 = 3 * 5 + 4 * 7
# 50 = 3 * 6 + 4 * 8
print("\n")
# 常微分方程式


def model(y, t):
    # y:未知関数, t:時間変数, dydt:yに対する導関数
    dydt = -y + 1.0  # 1.0に収束する
    return dydt


y0 = 0  # 初期値
t = np.linspace(0, 5)  # 時間
y = odeint(model, y0, t)
# 結果のプロット
plt.plot(t, y)  # (x軸の値, y軸の値)
plt.xlabel("time(x shaft)")  # 軸ラベルの名前
plt.ylabel("y(y shaft)")  # 軸ラベルの名前
plt.show()
