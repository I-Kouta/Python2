# python file.py

# ファイルの読み込み(ただ表示させるのみ)
f = open("function.py", "r")
for row in f:
    print(row)
f.close()
