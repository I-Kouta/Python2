# python dateTime.py
import datetime

today = datetime.date.today()
todayDetail = datetime.datetime.today()
# 今日の日付
print(today)
print(todayDetail)

# 今日のそれぞれの値
print(today.year)
print(today.month)
print(today.day)
print(todayDetail.hour)
print(todayDetail.minute)
print(todayDetail.second, "\n")
# 日付のフォーマット
print(today.isoformat()) # 年 - 月 - 日
print(todayDetail.strftime("%Y/%M/%D %H:%M:%S")) # 年 - 月 - 日 時:分:秒
