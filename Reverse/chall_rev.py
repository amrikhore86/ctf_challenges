def x(b, k):
    k = k.encode()
    return bytes([b[i] ^ k[i % len(k)] for i in range(len(b))])

f = "hwj{this_is_the_flag}"

f = f.replace('a', '1')
f = bytes([ord(c) + 69 for c in f])
f = x(f, "hwj")
f = f[::-1]

print(f.hex())
