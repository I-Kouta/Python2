
# ゲーム理論
# python game.py

import random

def always_silent(): # 常に黙秘する
    return "黙秘"

def always_betray(): # 常に自白する
    return "自白"

def random_choice(): # ランダムに選択する
    return random.choice(["黙秘", "自白"])

# 利得表
payoff_matrix = {
    ("黙秘", "黙秘") : (-1, -1),
    ("黙秘", "自白") : (-3, 0),
    ("自白", "黙秘") : (0, -3),
    ("自白", "自白") : (-2, -2)
}

def play_games(strategy_A, strategy_B):
    choice_A = strategy_A() # 選択した戦略
    choice_B = strategy_B() # 選択した戦略
    payoff_A, payoff_B = payoff_matrix[(choice_A, choice_B)]

    print(f"A : {choice_A}, B : {choice_B} → 利得 : A = {payoff_A}, B = {payoff_B}")
    return payoff_A, payoff_B

play_games(always_silent, always_betray) # Aは常に黙秘、Bは常に自白
