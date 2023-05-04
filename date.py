# 日付と時刻
import datetime

dt1 = datetime.datetime(2022, 4, 13)
print(dt1)  # 2022-04-13 00:00:00

dt2 = datetime.datetime(2022, 4, 13, 13, 22, 31)
print(dt2)  # 2022-04-13 13:22:31

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
dt3 = datetime.datetime(2022, 4, 13, 13, 22, 31, 551, tokyo_tz)
print(dt3)  # 2022-04-13 13:22:31.000551+10:00

dt4 = datetime.date(2022, 4, 14)
print(dt4)  # 2022-04-14,日付まで

t1 = datetime.time(14, 32)
print(t1, "\n")  # 04:14:00

dt5 = datetime.datetime.now(tokyo_tz)
print(dt5)  # 今の日付と時間、()は省略可

today = datetime.date.today()
print(today)  # 今日

print(dt5.year)  # 年だけ
print(dt5.month)  # 年だけ
print(dt5.day)  # 日付だけ
print(dt5.hour)  # 時間だけ
print(dt5.minute)  # 分だけ
print(dt5.second, "\n")  # 秒だけ

dt6 = datetime.datetime.strptime("2022/04/17 14:34:22", "%Y/%m/%d %H:%M:%S")
print(dt6)
