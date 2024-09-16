# python hash.py
import hashlib
import uuid

print(hashlib.md5(b"perfume").hexdigest())
print(hashlib.sha256(b"perfume").hexdigest())

print("\n")

# UUIDの生成(ランダムな生成)

print(uuid.uuid4())
