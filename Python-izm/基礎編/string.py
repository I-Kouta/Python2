# python string.py

# 文字列への追加
# クォート3つで複数行に分けられる
text = """
1行目
2行目
"""
print(text)
# 文字列へ変換、置換
integer = 100
print(str(integer) + "円")
print(str(integer).replace("100", "200") + "円")
# 文字列の連結、分割
test_str = "123"
test_str += "-456"
test_str += "-789" * 3
print(test_str)
print(test_str.split("-"))
# 桁揃え
string = "12321"
print(string.rjust(10, "0"))
print(string.startswith("12")) # true
print(string.startswith("25")) # false
