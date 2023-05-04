# 算数・数学
import sympy
from sympy import sin, cos, tan, log

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
print(f"{expr} を展開：{expr_ex}")

expr_factor = sympy.factor(expr_ex)
print(f"{expr_ex} を因数分解：{expr_factor}")
print(f"{expr_ex}=0の解:{sympy.solve(expr_ex)}")

expr1 = x + y - 7
expr2 = 3 * x + 5 * y - 29
print(sympy.solve([expr1, expr2]))  # {x: ?, y: ?}

expr3 = x**3 + 2*x**2 - x + 2
expr3_1 = sympy.diff(expr3)
print(f"{expr3}を微分：{expr3_1}")
print(f"{expr3_1}を積分：{sympy.integrate(expr3_1)}", "\n")

print(sympy.diff(sin(x)))  # cos(x)
print(sympy.diff(cos(x)))  # -sin(x)
print(sympy.diff(tan(x)))  # tan(x)**2 + 1
print(sympy.diff(sympy.exp(x)))  # exp(x)
print(sympy.diff(log(x)), "\n")  # 1/x
print(sympy.integrate(sin(x)))  # -cos(x)
print(sympy.integrate(cos(x)))  # sin(x)
print(sympy.integrate(tan(x)))  # -log(cos(x))
print(sympy.integrate(sympy.exp(x)))  # exp(x)
print(sympy.integrate(log(x)))  # x*log(x) - x
