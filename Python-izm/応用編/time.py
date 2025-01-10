
# ストップウォッチをつくる
# python time.py

import time

def convert(sec):
    minutes = sec // 60 # 分の部分
    second = sec % 60 # 秒の部分
    milli_sec = (second - int(second)) * 1000
    hour = minutes // 60
    min = minutes % 60
    return f"{int(hour)} : {int(min)} : {int(second)} : {int(milli_sec)}"

start_signal = input("Push 'ENTER' to Start")
start_time = time.time()
stop_signal = input("Push 'ENTER' to Stop")
stop_time = time.time()
result = stop_time - start_time
time_result = convert(result)
print(f"Stop Time : {time_result}")
