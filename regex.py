# 正規表現
import re
target64 = "495j6t9h4jy59nhjt049ehd8gbhetognbodoj988t7tgubuvcrtdr0j9ihbyvcta"
# print(len(target64))
pattern = re.compile(r'n...o')  # n---oがあれば返す
result = pattern.search(target64)
if result:
    print(result.group())


pat = re.compile(r"vcta$")  # この文字列で終わっているか
resultPat = pat.search(target64)
if resultPat:
    print("「" + resultPat.group() + "」" + "は末尾でパターンにマッチします")
else:
    print("パターンにマッチしません")
# 別パターン
patB = re.compile(r"$496")  # この文字列で終わっているか
resultPatB = patB.search(target64)
if resultPatB:
    print("「" + resultPatB.group() + "」" + "は先頭でパターンにマッチします")
else:
    print("パターンにマッチしません")

patC = re.compile(r"59nh")
resultPatC = patC.search(target64)
if resultPatC:
    print(resultPatC.group() + "は存在します")
else:
    print("一致しません")
print("\n")

# マッチした文字列を取得


def checkMatch(msg, pattern):
    result = pattern.search(msg)
    if result:
        print(result.group(0))
    else:
        print("一致する文字はありません")


pattern = re.compile(r'カガミ')
checkMatch('カワルカガミ, ハテナビト, Flow', pattern)  # カガミ
checkMatch('edge, エレワ', pattern)  # 一致する文字はありません
print("\n")


def checkMatchB(msgB, patternB, start, end):
    resultB = patternB.search(msgB, start, end)
    if resultB:
        print(resultB.group(0))
    else:
        print("一致する文字はありません")


msgB = "タワーレコード渋谷店"
patternB = re.compile(r'レコード')
checkMatchB(msgB, patternB, 0, 8)
checkMatchB(msgB, patternB, 0, 1)
