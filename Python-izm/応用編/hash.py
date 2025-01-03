# python hash.py
import hashlib
import uuid

print(hashlib.md5(b"perfume").hexdigest())
print(hashlib.sha256(b"perfume").hexdigest())

print("\n")

# UUIDの生成(ランダムな生成)

print(uuid.uuid4())

print("\n")

# 最大値・最小値の取得

print(max([3, 2, 4, 5, 1]))
print(min(["f", "D", "a", "A"])) # 文字列の最小値(A)

print("\n")

# 合計値
num = [10, 20, 30, 20, 5, 3]
print(sum(num)) # 和
print(sum(num, 1000)) # 開始値を指定
