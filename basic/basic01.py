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

# ヘロンの公式
def heron(a, b, c):
  s = (a + b + c) / 2
  return math.sqrt(s * (s - a) * (s - b) * (s - c))

side1 = 3
side2 = 4
side3 = 5
print(f"3辺が{side1}, {side2}, {side3}の三角形の面積:{heron(side1, side2, side3)}")

# 二次方程式の判別式と解qe_disc, qe_solution
def qe_disc(a, b, c):
  return b ** 2 - 4 * a * c

def qe_solution(a, b, c):
  desc = qe_disc(a, b, c)
  desc1 = (-b + math.sqrt(desc)) / (2 * a)
  desc2 = (-b - math.sqrt(desc)) / (2 * a)
  return desc1, desc2

valueA = 1
valueB = -2
valueC = 1
discriminate = qe_disc(valueA, valueB, valueC) # 判別結果
desc1, desc2 = qe_solution(valueA, valueB, valueC)
print(f"判別結果:{discriminate}")
print(f"解:{desc1}, {desc2}")
