
# ビュフォンの針
# python buffon.py

import random
import math

class input_para:
    def __init__(self, t_val = 0, l_val = 0, n_val = 0):
        self.t_val = t_val
        self.l_val = l_val
        self.n_val = n_val

        def inp_val(self, p_type = "", val_type = float):
            while True:
                para_str = input(f"{p_type}を入力 : ")
                try:
                    para_tc = val_type(para_str)
                    return para_tc
                except ValueError:
                    print("数字を入力してください")
                else:
                    break

num = 0 # 試行回数の設定
hit = 0 # あたり回数の設定
