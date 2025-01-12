
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

class Needle:
    def __init__(self, n_len = 1, x_lim = 1, y_lim = 1, x_posi = 0, y_posi = 0, theta = 0):
        self.n_len = n_len # 針の長さ
        self.x_lim = x_lim # xの最大値
        self.y_lim = y_lim # yの最大値
        self.x_posi = x_posi # 針先位置(x)
        self.y_posi = y_posi # 針先位置(y)
        self.theta = theta # 針角度θ

    def throw(self):
        self.x_posi = random.uniform(0, self.x_lim) # x位置を0からxlimまでの小数に変える
        self.y_posi = random.uniform(0, self.y_lim) # y位置を0からylimまでの小数に変える
        self.theta = random.uniform(0, 360) # θを0から360までの小数に変える

    def endpoint(self, xy = "y"): #針先終点計算、xyはどちらを出力するか
        # θをラジアンに変換、cos(ラジアン)、sin(ラジアン)
        # x終点 = x + l cos(θ)、y終点 = y + l sin(θ)
        x_ep = self.x_posi + self.n_len * math.cos(math.radians(self.theta))
        y_ep = self.y_posi + self.n_len * math.sin(math.radians(self.theta))
        if xy == "x":
            return x_ep
        elif xy == "y":
            return y_ep
        else:
            return "error"

num = 0 # 試行回数の設定
hit = 0 # あたり回数の設定
