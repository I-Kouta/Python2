# python dateTime.py
import datetime
import calendar

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
print(todayDetail.strftime("%Y/%M/%D %H:%M:%S"), "\n") # 年 - 月 - 日 時:分:秒

# 日付の計算
print(todayDetail) # 今日
print(todayDetail + datetime.timedelta(days = 1)) # 翌日
newYear = datetime.datetime(2024, 1, 1)
calc = todayDetail - newYear
print("今日は1/1から" + str(calc.days) + "日後", "\n")
#うるう年の判定
print(calendar.isleap(2015)) # false
print(calendar.isleap(2024)) # true
print(calendar.leapdays(2010, 2020)) # 期間内にうるう年がある回数
