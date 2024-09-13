# python if.py

num = 1111
if num % 2 == 0:
    print(str(num) + "は偶数です")
    # passを書くと何も処理されない
elif num % 3 == 0:
    print(str(num) + "は3で割り切れる奇数です")
elif num % 5 == 0:
    print(str(num) + "は5で割り切れる奇数です")
elif num % 7 == 0 or num % 11 == 0: # いずれかの条件
    print(str(num) + "は7か11で割り切れる奇数です")
else:
    print(str(num) + "は3でも5でも割り切れない奇数です")
