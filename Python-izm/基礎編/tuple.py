# python tuple.py
import datetime

def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
    return value

testTuple = get_today()
print(testTuple[0]) # 年だけ
print(testTuple[1]) # 月だけ
print(testTuple[2]) # 日だけ
