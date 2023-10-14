# 出現回数をカウントする(python count.py)
import collections
import matplotlib.pyplot as plt

# アルファベット列
alphabet_sequence = "kokugo suugaku rika eigo buturi kagaku seibutu syakai nihonsi sekaisi tiri keizai keiei saiensu"

# アルファベットの出現回数を数える
letter_counts = collections.Counter(alphabet_sequence)

# アルファベットのリスト(aからzまで)
letters = [chr(ord('a') + i) for i in range(26)]

# 出現回数を格納するリスト
count_values = [letter_counts[letter] for letter in letters]

# グラフの描画
plt.bar(letters, count_values)
plt.xlabel('Alphabet')
plt.ylabel('Count')
plt.title('Alphabet Count in the Sequence')
plt.show()
