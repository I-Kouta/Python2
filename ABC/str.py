# エスケープシーケンス,\と組み合わせる
# \newlineで改行,\nでも改行される
print("こんにちは。\nお元気ですか？\nそれではまた。")

# 出力時には改行されない
print("I will go to the amusement park with \
my children tomorrow")

# 三連引用符を使うと改行が中身はそのまま出力される
msg = '''\
こんにちは。
今日のミーティングですが"予定通り"の時間に行います。
何か変更があれば連絡してください。'''
print('\n' + msg)

print('\n改行が上にできます')
print(r'raw文字列を使うと\nとしてそのまま表示されます')
print(r'末尾にはこのように足します' + '\\')

# 文字列と数値の連結, 数値を文字列に変換する
num1 = 20
num2 = 18
print("I'm " + str(num1) + " years old.")

# 18+20=36と出力される
print('\n' + str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2))
print(str(num1) + 'を' + str(num2) + 'で割った余りは' + str(num1 % num2) + 'です')

# len("文字")で文字数を数える、形式は数値とみなします
print('\nメッセージの文字数は' + str(len(msg)) + '文字です')

sample = 'インデックスはゼロから始まるか、もしくは最後の文字が-1となるように数えます'

print(sample[10])  # ら
print(sample[-6])  # う
print(sample[0:6])  # インデックス→終了インデックスは+1した値を指定
print(sample[-4:])  # 数えます

step = '123456789'
perfume = 'p00e00r00f00u00m00e00'

print(step[0:10:2])  # 13579
print(step[1:10:2])  # 2468
print(perfume[0:20:3])  # perfume→飛ばしたい文字数+1
