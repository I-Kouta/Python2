
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

    def y_change(self, t_val, ep = ""):
        y_2 = self.y_posi # y_2にy_posi代入
        while True:
            if y_2 <= t_val: # y_2が間隔t以下
                break
            else:  # y_2が間隔tより大きい
                y_2 -= t_val # y_2から tを引く
        y_2_ep = y_2 + self.n_len * math.sin(math.radians(self.theta))
        if ep == "ep":
            return y_2_ep #ｙ変更後の終点
        else:
            return y_2 #y変更後のy

def buffon_main(t_val, l_val, n_val):
    num = 0 # 試行回数の設定
    hit = 0 # あたり回数の設定
    limit = 3 * t_val # ｘとyの最大値は 3t
    while num < n_val: # 試行回数 < 目標試行回数
        needle = Needle(n_len = l_val, x_lim = limit, y_lim = limit) # 針の設定
        needle.throw() # 針を投げる = x, y, θの再設定
        if needle.theta <= 180: # θ <= 180
            if needle.y_change(t_val, "ep") >= t_val:
                hit += 1 # 交差カウント +1
            else:
                pass
        else: # θ > 180
            if needle.y_change(t_val, "ep") <= 0:
                hit += 1 # 交差カウント +1
            else:
                pass
        y_2 = needle.y_change(t_val, "ep")
        num += 1
    print(f"試行回数：{num}")
    print(f"交差本数：{hit}")
    prob = hit / num # 交差する確率
    print(f"交差する確率 P = 2l/t(pi) = {prob}")
    pi = 2 * l_val / (t_val * prob) # pi = 2*l/(t*prob)
    print(f"円周率 : {pi}")

para = input_para()
para.t_val = para.inp_val("間隔 t ", float)
para.l_val = para.inp_val("針の長さ l ", float)
para.n_val = para.inp_val("試行回数 n ", int)
print(f"間隔t :{para.t_val}, 針の長さl : {para.l_val}, 試行回数n : {para.n_val}")
buffon_main(para.t_val, para.l_val, para.n_val) # t(平行線の間隔) > l(針の長さ)だと良い
