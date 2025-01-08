
# 確率の悪魔
# python lots.py

import random

# くじ作成
lot = ["〇", "×1", "×2","×3","×4","×5","×6","×7","×8","×9",]

# くじを引いた回数
lot_num = 0
# あたりの回数
win = 0
# くじを引く
while True:
    if lot_num == 10:
        break
    else:
        your_lot = random.choice(lot)
        lot_num += 1
        if your_lot == "〇":
            print(f"{lot_num}回目、{your_lot}, あたり")
            win += 1
        else:
            print(f"{lot_num}回目、{your_lot}, はずれ")
            pass

# 10回であたったか判定
if win == 0:
    print("当たりなし")
else:
    print(f"当たり{win}回")
