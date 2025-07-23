def x(b, k):
    k = k.encode()
    return bytes([b[i] ^ k[i % len(k)] for i in range(len(b))])

enc_hex = "aa120e1211d3c1c0cfdfc0ccc2ddd3d6dbc6d2c1cfd0c0dfc0d0cfa8c5cbc5"

f = bytes.fromhex(enc_hex)
f = f[::-1]               # reverse back
f = x(f, "hwj")           # xor with key
f = ''.join([chr(b - 69) for b in f])  # subtract 69, convert to char
f = f.replace('1', 'a')   # restore 'a'

print(f)
