def x(b, k):
    k = k.encode()
    return bytes([b[i] ^ k[i % len(k)] for i in range(len(b))])

enc_hex = "a8db1edbdcccc0dad1cecfc6cecfc6c7cea8c5cbc5"

f = bytes.fromhex(enc_hex)
f = f[::-1]               # reverse back
f = x(f, "hwj")           # xor with key
f = ''.join([chr(b - 69) for b in f])  # subtract 69, convert to char
f = f.replace('1', 'a')   # restore 'a'

print(f)
