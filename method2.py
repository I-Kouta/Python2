# 指定した文字列が〜以降
pta = 'Perfume'

# 最初に現れる位置をインデックスで返す,該当が無ければ-1
# indexメソッドだと-1ではなくエラー
print(pta.find('e'))  # 1
print(pta.find('g'))  # -1
print('\n')
# 最後に現れるインデックスを取得(rindexも同様)
print(pta.rfind('e'))  # 6
print(pta.rfind('ume'))  # 4
print('\n')
# countメソッド：大文字と小文字の区別アリ
print('Spinning World'.count('n'))  # 3
print('Spinning World'.count('s'))  # 0
print('Spinning World'.count('i', 0, 2))  # Spまでが対象なので0
print('\n')
# splitメソッド：区切って分割して取得
print('World-Baseball-Classic'.split('-'))  # ['---', '----']
print('World\nBaseball\nClassic')  # 改行される
print('\n')
# 文字を取り除くメソッド
print('abcedgeabc'.strip('abc'))  # edge
print('edgeabc'.rstrip('abc'))  # 末尾から文字を取り除く
print('abcedge'.lstrip('abc'))  # 先頭から文字を取り除く
print('\n')
# 別の文字列に置換するメソッド
print("It's My Life".replace('M', 'm').replace('L', 'l'))  # It's my life
print("It's My Life".replace("It's My Life", 'やーーーー！'))  # やーーーー！
