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
