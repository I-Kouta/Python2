
# 確率の悪魔
# python lots.py

import random

# くじ作成
lot = ["〇", "×1", "×2","×3","×4","×5","×6","×7","×8","×9",]

# くじを引く
your_lot = random.choice(lot)
if your_lot == "〇":
    print(f"{your_lot}, あたり")
else:
    print(f"{your_lot}, はずれ")
