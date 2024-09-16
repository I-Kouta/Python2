# python hash.py
import hashlib

print(hashlib.md5(b"perfume").hexdigest())
print(hashlib.sha256(b"perfume").hexdigest())
