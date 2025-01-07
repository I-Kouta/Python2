
# 確率の悪魔
# python lots.py

import random

# くじ作成
lot = ["〇", "×1", "×2","×3","×4","×5","×6","×7","×8","×9",]

# くじを引いた回数
lot_result = 0
# くじを引く
while True:
    if lot_result == 10:
        break
    else:
        your_lot = random.choice(lot)
        lot_result += 1
        if your_lot == "〇":
            print(f"{your_lot}, あたり")
        else:
            print(f"{your_lot}, はずれ")
