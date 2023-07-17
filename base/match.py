# マッチオブジェクトからマッチした文字列の情報を取得
import re
msg1 = 'birthday is 1989/02/15'
pat1 = re.compile(r"(\d{4})/(\d{2})/(\d{2})")
result1 = pat1.search(msg1)
if result1:
    print("生年月日：" + result1.group(0))
    print("年：" + result1.group(1))
    print("月：" + result1.group(2))
    print("日：" + result1.group(3))

print("\n")
msg2 = 'birthday is 1999/02/03'
pat2 = re.compile(r"(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})")
result2 = pat2.search(msg2)
if result2:
    print("マッチ：" + result2.group(0))
    print("group[年]:" + result2.group("year"))
    print("group[月]:" + result2.group("month"))
    print("group[日]:" + result2.group("day"))

print("\n")
msg3 = "バリデーション:文字数,型,一意性,同一か"
pat3 = re.compile(r":|,")
result3 = pat3.split(msg3)
print(result3, "\n")

msg4 = "Red, red, RED, Blue, blue, オレンジ, pink"
pat4 = re.compile(r"Red|RED")  # これが置換される
result4 = pat4.sub("赤", msg4)  # これに置換される
print(result4, "\n")

msg5 = "1994-07-05"
pat5 = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
result5 = pat5.sub(r"\1年\2月\3日", msg5)
print(result5)

msg6 = "It's My Life"
pat6 = re.compile(r"\b[a-zA-Z]+?\b")


def replaceStr(m):
    s = m.group(0)
    return s.lower()  # 対はupper


result6 = pat6.sub(replaceStr, msg6)
print(result6)
