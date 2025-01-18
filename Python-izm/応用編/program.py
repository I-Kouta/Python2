
# python program.py

# x + xy + xyz = 31, x < y < y = 31となる組み合わせ
a = 31
for x in range(1, a + 1):
    for y in range(x + 1, a + 1): # x < y
        for z in range(y + 1, a + 1):
            if x + x * y + x * y * z == a:
                print("(x, y, z) = ({0}, {1}, {2})".format(x, y, z))

print("===")
# 3桁とも素数で、2乗すると5桁とも素数となるもの
def is_nice(n, target_len):
    b = str(n)
    if len(b) != target_len: # 桁数が条件を満たしていない場合
        return False
    for i in b:
        if i != "2" and i != "3" and i != "5" and i != "7": # 2, 3, 5, 7以外の数字が含まれている場合
            return False
    return True

for n in range(100, 1000):
    if is_nice(n, 3) and is_nice(n * n, 5):
        print(f"{n}を2乗すると{n ** 2}になる")

print("===")
# 97, 100, 103で割った余りがそれぞれ32, 33, 34の正の整数のうち最小のもの
c = 1
while c % 97 != 32 or c % 100 != 33 or c % 103 != 34: # 1つでも条件を満たさなければ、足し続ける
    c += 1
print("Answer : {0}".format(c))
