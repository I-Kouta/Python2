import numpy as np
import random
import matplotlib.pyplot as plt

def tomoe(player_list, iter_num, seed = 42):

    ## set seed
    random.seed(seed)

    ## set object
    winner_cnt = {player:[0] for player in player_list}
    max_win = len(player_list) - 1

    for trial in range(iter_num):
        winner = ""
        battle = player_list[:2]
        waiting_list = player_list[2:]
        win_cnt = 0
        while win_cnt < max_win:
            _winner, _loser = random.sample(battle, 2)
            if winner == _winner:
                win_cnt += 1
            else:
                win_cnt = 1
                winner = _winner
            waiting_list.append(_loser)
            battle = sorted([winner, waiting_list.pop(0)])
        other_set = set(player_list) - set(winner)
        # updateting the result
        winner_cnt[winner].append(winner_cnt[winner][-1] + 1)
        for other in other_set:
            winner_cnt[other].append(winner_cnt[other][-1])
    return winner_cnt

N = 100000
result = tomoe(player_list = list("ABC"), iter_num = N)

fig, ax = plt.subplots(1, 1,figsize = (15, 10))
trial_range = np.arange(1, N + 1)

for player in sorted(result.keys()):
    win_prob = result[player][1:]/trial_range
    ax.plot(win_prob,label = (player + "`s converged win prob: {} %").format(round(win_prob[-1] * 100, 2)))

ax.set_title("Tomoesen : the cumulative win probability", fontsize = 15)
ax.set_xlabel("Trial", fontsize = 12)
ax.set_xlim(0, 1000)
plt.legend()
plt.show()
