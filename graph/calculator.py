import tkinter as tk  # ライブラリのインポート
from tkinter import ttk

BUTTON = [
    ["", "B", "C", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

SYMBOL = ["+", "-", "*", "/"]


class CaluGui(object):  # ウィンドウ・タイトル・サイズ設定
    def __init__(self, app=None):
        self.calc_str = ""  # 計算用の文字列
        # Window Setting
        app.title('簡易的な電卓を作ってみた')  # Window のタイトル
        app.geometry('400x600')  # Window のサイズ

        # frame setting
        calc_frame = ttk.Frame(app, width=300, height=100)  # 計算式・結果用
        calc_frame.propagate(False)  # サイズ固定
        calc_frame.pack(side=tk.TOP, padx=10, pady=20)  # 余白設定
        button_frame = ttk.Frame(app, width=300, height=400)  # 計算ボタンframe
        button_frame.propagate(False)  # サイズ固定
        button_frame.pack(side=tk.BOTTOM)  # 余白設定

        # parts setting
        self.calc_var = tk.StringVar()  # 計算式用動的変数
        self.ans_var = tk.StringVar()  # 結果用動的変数
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("", 20))  # 計算式用label
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("", 15))  # 結果用label
        calc_label.pack(anchor=tk.E)  # 右揃え
        ans_label.pack(anchor=tk.E)

        for y, row in enumerate(BUTTON, 1):  # ボタン配置
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=("", 15), width=6, height=3)
                button.grid(row=y, column=x)  # 列と行を指定して配置
                button.bind("<Button-1>", self.click_button)  # ボタンが押された場合

    def click_button(self, event):
        check = event.widget["text"]

        if check == "=":  # イコールが押された場合
            if self.calc_str[-1:] in SYMBOL:  # 記号の場合,記号より前で計算
                self.calc_str = self.calc_str[:-1]

            res = "= " + str(eval(self.calc_str))  # eval関数(文字列が式として評価される)
            self.ans_var.set(res)
        elif check == "C":
            self.calc_str = ""
            self.ans_var.set("")
        elif check == "B":
            self.calc_str = self.calc_str[:-1]
        elif check in SYMBOL:  # 記号の場合
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != "":
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL:  # 記号の場合は入れ替える
                self.calc_str = self.calc_str[:-1] + check
        else:  # 数字の場合
            self.calc_str += check

        self.calc_var.set(self.calc_str)


def main():
    app = tk.Tk()
    app.resizable(width=False, height=False)
    CaluGui(app)
    app.mainloop()  # Window をループで回すことでWidgetに対応できるようになる、メインループ実行


if __name__ == '__main__':  # スクリプトが直接実行された時にこれを実行する
    main()
