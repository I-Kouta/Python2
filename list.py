# リストを作成する
PerfumeList = ["Pick Me Up", "Spinning World", "コミュニケーション", "FAKE IT"]
print(PerfumeList[0])  # Pick Me Up
print(PerfumeList[-1])  # FAKE IT
print(PerfumeList[-2])  # コミュニケーション
print("最後の要素は" + PerfumeList[len(PerfumeList) - 1])
print("要素の数は" + str(len(PerfumeList)) + "つです\n")

# スライス機能
print(PerfumeList[0:2])  # SWまで。最後は要素+1
print(PerfumeList[:2])  # 同じ
print(PerfumeList[2:])
print("\n")
print("変更前のオブジェクトidは" + str(id(PerfumeList)))
# 要素を入れ替える
PerfumeList[-1] = "マワルカガミ"
print(PerfumeList[-1])  # マワルカガミ
print("変更後のオブジェクトidは" + str(id(PerfumeList)) + "で、変わっていません")
print("\n")
# リストを追加する
PerfumeList.append("ハテナビト")
print(PerfumeList)
print("\n")
# 指定位置に要素を挿入
numberList = [101, 102, 106, 107]
numberList.insert(2, 103)  # 2番目の値の前に3を挿入する
print(numberList)  # 101, 102, 103, 106, 107
addList = [104, 105]
numberList[3:3] = addList
print(numberList)  # これで番号順
del numberList[-1]
print(numberList)  # 107が消えている
del numberList[2:5]
print(numberList)  # 103から105が消えている
numberList.pop(1)
print(numberList)  # 102が消えている
numberList.remove(101)  # "101"は不可
print(numberList)  # 101が消えている
numberList.clear()  # 全ての要素を削除
print(numberList)  # []のみ
del numberList

# 同じ要素が含まれるか
num = [401, 402, 404, 404, 405]
newNum = sorted(num, reverse=True)
print("404" in num)  # true
print("40" in num)  # false, 完全に一致しないと不可
print("401" not in num)  # false
print(num.count(404))  # "404"は0
print(num.index(402))  # 最初に見つかった位置を返す,見つからなかったらエラー
print("\n")
print("before:", num)
print("after :", newNum)
del num
del newNum
# range型オブジェクトを引数に指定してリストオブジェクトを指定
length10 = list(range(10))
print(length10, "\n")  # 0から9までの数値を要素としてもつリスト
# 多次元リスト
teamPacific = [["ソフトバンク", 1], ["オリックス", 2], [
    "楽天", 3], ["西武", 4], ["千葉ロッテ", 5], ["日本ハム", 6]]
print(teamPacific[0])  # ["ソフトバンク", 1]
print(teamPacific[1][0])  # オリックス
for p in [0, 1, 2, 3, 4, 5]:
    for m in [0, 1]:
        print("[" + str(p) + "][" + str(m) + "] = ", teamPacific[p][m])
print("\n")
del teamPacific
# リスト内包表記
max = 5
numberList = [i for i in range(1, max + 1)]
print(numberList)  # [1, 2, 3, 4, 5]
numberListA = [i * 10 for i in range(1, max + 1)]
print(numberListA)  # [10, 20, 30, 40, 50]
numberListB = [i for i in range(1, 11) if i % 2 == 0]
print(numberListB, "\n")  # [2, 4, 6, 8, 10] 偶数を表示
# 多重ループ
# 赤カッコ内を先に繰り返す
myList = [[i * 100 + j for j in range(1, 3)]for i in range(1, 4)]
myListB = [i * 100 + j for j in range(1, 3) for i in range(1, 4)]
print(myList)  # [[101, 102], [201, 202], [301, 302]]
print(myListB)  # [101, 201, 301, 102, 202, 302]
