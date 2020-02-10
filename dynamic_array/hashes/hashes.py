import hashlib

# b = bitestring, strips metadata away
# ending with '.encode()' does the same thing

key = b'str'
my_string = 'this is a normal string. Nothing to see here'

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)

