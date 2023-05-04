# python ファイル名で出力
# /Users/ko-ta_python_lesson

# 文の区切りと長い文を途中で改行して入力する方法
# 改行するとすると、そこまでで1つの文として処理される
# 文末に文字の入力は不要
str = 'hello,python'
print(str)
print("Tom's toy")  # クオーテーションを区別する場合

# 1行にまとめたい場合には;で改行したい箇所に記入。現状、なぜかその形式で保存されない
num1 = 10
num2 = 8
num3 = 12
num4 = "22"
print(num1 + num2 + num3)
print(num3 + int(num4))  # 文字を数値に変換する

# 長い文章を途中で改行するときにはバックスラッシュ\で区切る、windowsでは¥期号
# \改行のための記号の行にはコメントをかけない
number = 1 + 2 +\
    3 + 4\
    + 5
print(number)

# 文字コードを指定する
# coding: utf_8
# codingの後ろにエンコーディング名
print('こんにちは')
