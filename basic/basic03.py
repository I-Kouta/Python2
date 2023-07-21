# 条件分岐(python basic03.py)
def exception3(x, y, z):
    if x == y:
        return z
    elif y == z:
        return x
    elif z == x:
        return y
    else:
        return x + y + z

print(exception3(1, 1, 2))
