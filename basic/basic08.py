# 234, csvファイル(python basic08.py)
import csv
f = open("small.csv", "r")
dataReader = csv.reader(f)
for row in dataReader:
    print(row)
f.close()
