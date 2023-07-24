# pythonを用いた科学技術計算(python basic06.py)
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
