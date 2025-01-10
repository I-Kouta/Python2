
# ストップウォッチをつくる
# python time.py

import time

start_signal = input("Push 'ENTER' to Start")
start_time = time.time()
stop_signal = input("Push 'ENTER' to Stop")
stop_time = time.time()
result = stop_time - start_time
print(f"Stop Time : {result:.3f}s")
