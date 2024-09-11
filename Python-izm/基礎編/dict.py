# python dict.py

testDict = {"year" : "2024", "month" : "9", "day" : "1"}
print(testDict) # ただ出力されるだけ
for i in testDict:
    print(i)
    print(testDict[i])

# リスト
testList =["123", "456", "789", "012"]
print(testList[-1:]) # 末尾の1つ
print(testList[:-1]) # 末尾の1つ以外
print(testList[::-1]) # 全ての逆順
