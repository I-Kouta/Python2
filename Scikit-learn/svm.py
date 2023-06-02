# python svm.py
from sklearn import svm, metrics

xor_data = [
    [0 ,0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q]) # 学習データを格納
    label.append(r) # labelに答えを格納,fit()メソッドで学習

clf = svm.SVC() # SVMオブジェクトを生成
clf.fit(data, label) # 与えられたデータを学習
pre = clf.predict(data) # 学習結果からデータを予測
print('予測：', pre)
score = metrics.accuracy_score(label, pre) # 正解率を求める
print('正解率：', score)
# 予測： [0 1 1 1]
# 正解率： 1.0
