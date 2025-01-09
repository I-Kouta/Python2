
# 確率の悪魔
# python lots.py

import random

# くじ作成
lot = ["〇", "×1", "×2","×3","×4","×5","×6","×7","×8","×9",]
lot_num = 0 # くじを引いた回数
win_count= 0 # あたりの回数

prog_num = 0 # 10回判定のプログラムの試行回数
prog_win_num = 0 # 10回判定のプログラムのあたり回数

# 10回繰り返す
while True:
    if prog_num == 10:
        break
    else: # くじを引く
        while True:
            if lot_num == 10:
                prog_num += 1
                break
            else:
                your_lot = random.choice(lot)
                lot_num += 1
                if your_lot == "〇":
                    # print(f"{lot_num}回目、{your_lot}, あたり")
                    win_count+= 1
                else:
                    # print(f"{lot_num}回目、{your_lot}, はずれ")
                    pass
        if prog_win_num == 0:
            print("あたりなし")
        else:
            print(f"{prog_win_num}回目にあたり")
            prog_win_num += 1
        lot_num = 0
        win_count= 0
print("試行回数", prog_num)
print("あたり回数", prog_win_num)
