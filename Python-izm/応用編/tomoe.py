# python tomoe.py
# 巴戦
from random import choice

count = 100000

wrestlers_str = "ABC"
wrestlers = set(wrestlers_str)
need_win_count = len(wrestlers) - 1
won_count_dic = {wrestler: 0 for wrestler in wrestlers}

for _ in range(count):
    #print("=" * 32)
    _win = "X"
    win = "X"
    dohyo = set(wrestlers_str[:2])
    win_count = 0
    while True:
        _win = choice(list(dohyo))
        #print(dohyo, _win, win)
        if win == _win:
            win_count += 1

        if need_win_count == win_count:
            won_count_dic[win] += 1
            break

        win = _win

        dohyo = {_win, choice(list(wrestlers - dohyo))}

print({wrestler: won_count_dic[wrestler]  / count for wrestler in wrestlers_str})
