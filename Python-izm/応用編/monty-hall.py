
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

sim_choice()
