
# ゲーム理論
# python game.py

# 利得表を辞書で表現
payoff_matrix = {
    ("黙秘", "黙秘") : (0, 0),
    ("黙秘", "自白") : (-3, 0),
    ("自白", "黙秘") : (0, -3),
    ("自白", "自白") : (-2, -2)
}

print(f'どちらも自白の場合：{payoff_matrix[("自白", "自白")]}')
print(f'片方が自白の場合：{payoff_matrix[("黙秘", "自白")]}, {payoff_matrix[("自白", "黙秘")]}')
print(f'どちらも黙秘の場合：{payoff_matrix[("黙秘", "黙秘")]}')
