
# モンティ・ホール問題
# python monty-hall.py

import random

def sim_choice():
    while True:
        try:
            num_sim = int(input("試行回数を入力してください : ")) # 試行回数入力、文字列を数字に変換
            plyer_choice = input("ドアを変更する YES = y or NO = n") # ドア変更するか？
        except ValueError: # 小数か文字列を入れると発生
            print("数字を入力してください")
        else: # 正常終了時
            break
    if plyer_choice == "y": # ドア変更あり
        print(f"試行回数 : {num_sim}回、ドア変更あり")
    elif plyer_choice == "n": # ドア変更なし
        print(f"試行回数 : {num_sim}回、ドア変更なし")
    return [num_sim, plyer_choice] # リストで返す[試行回数, ドア変y or n]

def monty(num, y_or_n):
    sim_count = 0 # これまでの試行回数
    door = [1, 2, 3] # ドア3つ
    car_count = 0 # 当たりの回数
    car = random.choice(door) # 当たりのドアをランダム
    player = random.choice(door) # プレイヤーが選ぶドアをランダム
    if car == random.choice(door): # はじめに正解の場合
        door.remove(car) # 当たりのドアを外す
        monty_choice = random.choice(door) # ハズレのドアを選ぶ
        if y_or_n == "y":
            pass # 不正解でパス
        elif y_or_n == "n":
            car_count += 1 # 正解で当たりのカウントを+1
    else:
    sim_count += 1

sim_choice()
