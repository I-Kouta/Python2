# python basic01.py
import math
print(math.sqrt(2)) # 平方根の記述
print(math.pi) # 円周率
val01 = (math.sqrt(5) + 1) / 2 # 5の平方根に1を加えて2で割る(黄金比)
print(val01)

# fフィートiインチをセンチメートルに変換する(1フィート = 12インチ = 30.48cm)
def ft_to_cm(f, i):
  return (f + i / 12) * 30.48

feet = 3
inch = 3
print(f"{feet}フィート + {inch}インチ = {ft_to_cm(feet, inch)}cm")

# mメートルをフィート・インチに変換する
def m_to_ft(m):
  inches =  m * 39.37
  feet =  m * 3.28
  return inches, feet

m = 18.44
inches, feet = m_to_ft(m)
print(f"{m}メートル = {inches}インチ = {feet}フィート")

# 二次関数の値を求める
def quadratic(a, b, c, x):
  return a * x ** 2 + b * x + c

answer = quadratic(1, -5, -2, 7)
print(answer)
