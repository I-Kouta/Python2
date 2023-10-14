# 出現回数をカウントする(python count.py)
import collections
import matplotlib.pyplot as plt

# アルファベット列
alphabet_sequence = "kokugo suugaku rika eigo buturi kagaku seibutu syakai nihonsi sekaisi tiri keizai keiei saiensu"

# アルファベットの出現回数を数える
letter_counts = collections.Counter(alphabet_sequence)

# 文中のアルファベットの総数を計算
total_letters = sum(letter_counts.values())

# アルファベットのリスト(aからzまで)
letters = [chr(ord('a') + i) for i in range(26)]

# 出現頻度を数える
frequency_values = [letter_counts[letter] / total_letters for letter in letters]

# グラフの描画
plt.bar(letters, frequency_values)
plt.xlabel('Alphabet')
plt.ylabel('Frequency')
plt.title('Alphabet Count in the Sequence')
plt.show()
