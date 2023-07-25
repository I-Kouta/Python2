# pythonを用いた科学技術計算(python basic06.py)
import re
# ループの用法, 値のリストから最小値を見つける
smallest = None
print(f"before:{smallest}")
for itervar in [41, 12, 9, 3, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
print(f"smallest: {smallest}")

# 文字列路リスト
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split() # スペースでリストを分ける
print(pieces)
parts = pieces[3].split('-') # リストの3番目を"-"で分ける
print(parts)
n = parts[1] # lar@freecodecamp.org
print(n)

# pythonの辞書
dicts = {"Fri": 20, "Thu": 6, "Sat": 1}
dicts["Thu"] = 13
dicts["Sat"] = 2
dicts["Sun"] = 9
print(dicts) # 20, 13, 9, 2

print("\n")
# 辞書とループ
counts = {"chuck" : 1, "annie" : 42, "jan": 100}
for key in counts:
    if counts[key] > 10: # キーが10より大きい場合
        print(key, counts[key])

print("\n")
# タプルコレクション
d = dict()
d["quincy"] = 1
d["beau"] = 5
d["kris"] = 9
for (k, i) in d.items():
    print(k, i)

print("\n")
# 正規表現:データの称号と抽出
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# \\S+: 1文字以上の非空白文字
lst = re.findall('\\S+@\\S+', s)
print(lst)
