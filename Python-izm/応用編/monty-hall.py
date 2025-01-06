
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
            # print(f"試行回数 : {num_sim}回")
            break
    return num_sim

def monty(num):
    sim_count = 0 # これまでの試行回数
    change_car = 0 # ドアを変えた場合の当たりの回数
    not_change_car = 0 # ドアを買えない場合の当たりの回数
    while True:
        if sim_count != num:
            door = [1, 2, 3] # ドア3つ
            car = random.choice(door) # 当たりのドアをランダム
            player = random.choice(door) # プレイヤーが選ぶドアをランダム
            if car == player: # はじめに正解の場合
                door.remove(car) # 当たりのドアを外して、
                random.choice(door) # ハズレのドアを選ぶ
                not_change_car += 1 # はじめに正解の扉を選んでいるので、変えなければ+1
            else: # はじめに不正解の場合
                door.remove(car) # 当たりのドアを外して、
                door.remove(player) # プレイヤーの選択したドアも外す
                random.choice(door) # ハズレのドアを選ぶ
                change_car += 1 # はじめに外れているので、変えたら+1
            sim_count += 1
            # print(f"試行No{sim_count}、判定 : {judge}")
        else:
            change_car_prob = 100 * change_car / sim_count
            print(f"試行回数 : {sim_count}回中{change_car}回当たり、{change_car_prob:3f}%当たり")
            not_change_car_prob = 100 * not_change_car / sim_count
            print(f"試行回数 : {sim_count}回中{not_change_car}当たり : {not_change_car_prob:3f}%当たり")
            break

sim = sim_choice()
monty(sim)
