# シーザー暗号をつくってみる(python caesar.py)
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # 文字がアルファベットの場合のみシフトを適用
            is_upper = char.isupper()
            char = char.lower()
            shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted = shifted.upper()
            result += shifted
        else:
            # アルファベット以外の文字は変更せずにそのまま結果に追加
            result += char
    return result

original_word = "orange"
shifted_word = caesar_cipher(original_word, 1)
print("元の単語:", original_word)
print("1つ進めた後:", shifted_word)
