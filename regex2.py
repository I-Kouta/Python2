# パターンとマッチする
import re


def checkMatch(msg, pat):
    pattern = re.compile(pat)
    result = pattern.fullmatch(msg)
    if result:
        print(result.group(0))
    else:
        print("完全一致しません")


checkMatch("シークレットシークレット", r"シ.*シ")  # 完全一致しません
checkMatch("シークレットシークレット", r"シ.*ト")  # シークレットシークレット

birth = "NA-0215, KY-1223, OA-0920"
pattern2 = re.compile(r"[A-Z]{2}-[0-9]{4}")
result2 = pattern2.findall(birth)

if (len(result2) == 0):
    print("一致しません")
else:
    for s in result2:
        print(s)

print(str(len(result2)) + "つ一致する要素があります\n")

msg3 = 'MA-1989, JO-1998, PP-199'
pattern3 = re.compile(r'([A-Z]{2})-([0-9]{4})')
result3 = pattern3.finditer(msg3)
m = None
for m in result3:
    print(f"Match:{m.group(0)}")
    print("アルファベット:" + m.group(1))
    print(f"数値: {m.group(2)}")

if m is None:
    print("Noneです")
