# 文字列で提供されているメソッドの使い方(数値は不可)
print(',' .join(['あ〜ちゃん', 'かしゆか', 'のっち']))

message = 'Perfume Closet'

print(message.lower())  # 全て小文字になる
print(message.upper())  # 全て大文字になる

member = 'a-chan KASHIYUKA NOCCHi'

print(member.capitalize())  # 最初の文字のみ大文字(単語毎の区別ナシ)
print(member.title())  # 単語毎に先頭の文字のみ大文字
print(member.swapcase())  # 大文字と小文字を逆にする

# 数値と日本語は区別されない
print(message.islower())  # 全ての文字が小文字ならtrue
print('perfume closet'.islower())  # true
print('西脇綾香'.islower())  # 区別される文字が含まれていないためfalse
print('20230305'.islower())  # 区別される文字が含まれていないためfalse
print('NIGHT FLIGHT'.isupper())  # 全て大文字だとtrue

print('Party Maker'.istitle())  # 単語の先頭のみ大文字だとtrue
print('FAKE IT'.istitle())  # false

print('\n')
print('20230306'.isdecimal())  # 10進数ならtrue
print('-1,024'.isdecimal())  # これだとfalse
print('3ff'.isdecimal())  # 10進数以外の文字、アルファベット,ハイフン,ドット,漢数字,空文字などもfalse

print('\n')
print('③③④'.isdigit())  # true
print('２０２３'.isdigit())  # true

print('\n')
print('七五三'.isnumeric())  # true
print('壱伍'.isnumeric())  # true

print('\n')
print('-1.414'.isascii())  # カンマ,ハイフン,ドットも含まれる,空でもtrue

print('\n')
print('HoldYourHand'.isalpha())  # true
print('Hold Your Hand'.isalpha())  # スペースがあるとfalse
print('3569'.isalpha())  # false

print('\n')  # 空の場合はfalse
print('いじわるなハロー'.isalnum())  # true
print('100years'.isalnum())  # true
print('3:5:6:9'.isalnum())  # false
