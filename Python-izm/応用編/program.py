
# python program.py

# x + xy + xyz = 31, x < y < y = 31となる組み合わせ
n = 31
for x in range(1, n + 1):
    for y in range(x + 1, n + 1): # x < y
        for z in range(y + 1, n + 1):
            if x + x * y + x * y * z == n:
                print("(x, y, z) = ({0}, {1}, {2})".format(x, y, z))
