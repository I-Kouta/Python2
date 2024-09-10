# python tuple.py
import datetime

# タプル
def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
    return value

testTuple = get_today()
print(testTuple[0]) # 年だけ
print(testTuple[1]) # 月だけ
print(testTuple[2]) # 日だけ

# リスト
testList = ["111", "111", "1111"]

testList.insert(1, "-") # インデックス値を指定して要素を追加(appendだと末尾に付与)
testList.insert(3, "-")
testList.pop(4) # 該当のインデックス値の要素を削除
print(testList)
print(testList.index("111")) # 引数に該当するインデックス値を返す
print(testList.count("111")) # 指定の引数の数を数える
