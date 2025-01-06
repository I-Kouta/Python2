
# モンティ・ホール問題
# python monty-hall.py

import random

def sim_choice():
    while True:
        try:
            num_sim = int(input("試行回数を入力してください : ")) # 試行回数入力、文字列を数字に変換
        except ValueError: # 小数か文字列を入れると発生
            print("数字を入力してください")
        else: # 正常終了時
            print(f"試行回数 : {num_sim}回")
            break
    return num_sim

def monty(num, y_or_n):
    sim_count = 0 # これまでの試行回数
    car_count = 0 # 当たりの回数
    while True:
        if sim_count != num:
            door = [1, 2, 3] # ドア3つ
            car = random.choice(door) # 当たりのドアをランダム
            player = random.choice(door) # プレイヤーが選ぶドアをランダム
            if car == player: # はじめに正解の場合
                door.remove(car) # 当たりのドアを外して、
                monty_choice = random.choice(door) # ハズレのドアを選ぶ
                if y_or_n == "y":
                    judge = "はずれ"
                elif y_or_n == "n":
                    car_count += 1 # 正解で当たりのカウントを+1
                    judge = "あたり"
            else: # はじめに不正解の場合
                door.remove(car) # 当たりのドアを外して、
                door.remove(player) # プレイヤーの選択したドアも外す
                monty_choice = random.choice(door) # ハズレのドアを選ぶ
                if y_or_n == "y":
                    car_count += 1 # 正解で当たりのカウントを+1
                    judge = "あたり"
                elif y_or_n == "n":
                    judge = "はずれ"
            sim_count += 1
            # print(f"試行No{sim_count}、判定 : {judge}")
        else:
            car_prob = 100 * car_count / sim_count # あたりの確率
            print(f"試行回数 : {sim_count}回中、あたり : {car_count}回、あたり確率 : {car_prob:3f}%")
            break

sim = sim_choice()
monty(sim[0], sim[1])
