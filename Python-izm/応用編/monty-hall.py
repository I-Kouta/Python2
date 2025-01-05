
# モンティ・ホール問題
# python monty-hall.py

import random

def sim_choice():
    while True:
        try:
            num_sim = int(input("試行回数を入力してください : ")) # 試行回数入力、文字列を数字に変換
            plyer_choice = input("ドアを変更する YES = y or NO = n : ") # ドア変更するか？
        except ValueError: # 小数か文字列を入れると発生
            print("数字を入力してください")
        else: # 正常終了時
            pass
        if plyer_choice == "y": # ドア変更あり
            print(f"試行回数 : {num_sim}回、ドア変更あり")
            break
        elif plyer_choice == "n": # ドア変更なし
            print(f"試行回数 : {num_sim}回、ドア変更なし")
            break
        else:
            print("yかnを入力してください")
    return [num_sim, plyer_choice] # リストで返す[試行回数, ドア変y or n]

def monty(num, y_or_n):
    sim_count = 0 # これまでの試行回数
    door = [1, 2, 3] # ドア3つ
    car_count = 0 # 当たりの回数
    car = random.choice(door) # 当たりのドアをランダム
    player = random.choice(door) # プレイヤーが選ぶドアをランダム
    if car == random.choice(door): # はじめに正解の場合
        door.remove(car) # 当たりのドアを外して、
        monty_choice = random.choice(door) # ハズレのドアを選ぶ
        if y_or_n == "y":
            pass # 不正解でパス
        elif y_or_n == "n":
            car_count += 1 # 正解で当たりのカウントを+1
    else: # はじめに不正解の場合
        door.remove(car) # 当たりのドアを外して、
        monty_choice = random.choice(door) # ハズレのドアを選ぶ
        if y_or_n == "y":
            car_count += 1 # 正解で当たりのカウントを+1
        elif y_or_n == "n":
            pass # 不正解でパス
    sim_count += 1
    print(f"試行回数 : {sim_count}、当たりの回数 : {car_count}")
    print(f"当たりのドア : {car}、最初の選択 : {player}、モンティの選択 : {monty_choice}")

sim = sim_choice()
monty(sim[0], sim[1])
