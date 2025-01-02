
# 秘書問題を解く
# python hisyo.py

import numpy as np

# 応募者の人数
N = 100

# シミュレーション回数
n_exam = 1000

# 評価値の最大値
max_eval = 100

np.random.seed(1)

def make_application_sample(N, max_eval):
    """
    応募者と評価値の最大値を受け取り、応募者のリストを返す
    """
    sample = np.random.normal(10, 10, N) # 平均, 標準偏差, 配列数
    min_sample = np.min(sample)
    max_sample = np.max(sample)
    # 正規化処理(0 ~ 1の間になる)
    normalized = (sample - min_sample) / (max_sample - min_sample) * max_eval
    return normalized

def parse_secretary_problem(N, max_eval, verbose = False):
    """
    N : 応募者数
    max_eval : 評価値の最大値
    verbose : デバッグ情報を表示するか
    return : 採用結果(候補者の評価値, 失敗なら0)
    """
    sample = make_application_sample(N, max_eval)

    # 先頭からN / e人を無条件で見送り、ベンチマーク評価値を作る
    pos_bench = np.int(N / np.e)
    score_bench = np.max(sample[0 : pos_bench])
    if verbose:
        print("採用見送り人数(この値は一定で問題ない) : {}".format(pos_bench)) # 見送った人数
        print("見送った人の最高スコア : {}".format(score_bench))
    result = 0 # 0の場合は、採用失敗
    for _score in sample[pos_bench:]:
        # 面談者の評価値が、ベンチマークを上回ったか
        if _score >= score_bench:
            # ベンチマークを上回ったら、そこで採用して、選考プロセスを終了する
            result = _score
            break
    return result # 上回った値を返す

# 動作試験
for i in range(10):
    print(parse_secretary_problem(N, max_eval, verbose=True))
    print("-" * 70)

# 採用結果、採用した人の評価値の履歴、できなければ0
history = []
for i in range(n_exam):
    history.append(parse_secretary_problem(N, max_eval, verbose = False))
history = np.array(history)
print("採用結果の期待値(失敗時も含む) : {}".format(np.mean(history)))
print("採用時の期待値 : {}".format(np.mean(history[history > 0])))
print("採用できた確率 : {}".format(np.sum(history > 0) / n_exam))
print("最適な候補者の採用確率 : {}".format(np.sum(history >= max_eval) / n_exam))
