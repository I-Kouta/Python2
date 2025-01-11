
# ビュフォンの針
# python buffon.py

import random
import math

def t_input():
    while True:
        t_str = input("間隔 t =") # 間隔
        try:
            t_flo = float(t_str) # floatで設定
            return t_flo
            break
        except ValueError:
            print("数字を入力してください")

def l_input():
    while True:
        l_str = input("針の長さ l =") # 長さ
        try:
            l_flo = float(l_str) # floatで設定
            return l_flo
            break
        except ValueError:
            print("数字を入力してください")

def n_input():
    while True:
        n_str = input("試行回数 N =") # 試行回数
        try:
            n_int = int(n_str) # intで設定
            return n_int
            break
        except ValueError:
            print("数字を入力してください")

num = 0 # 試行回数の設定
hit = 0 # あたり回数の設定
