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
    data.append([p, q])
    label.append(r)

clf = svm.SVC()
clf.fit(data, label)
pre = clf.predict(data)
print('予測：', pre)
score = metrics.accuracy_score(label, pre)
print('正解率：', score)
# 予測： [0 1 1 1]
# 正解率： 1.0
