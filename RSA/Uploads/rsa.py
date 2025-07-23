import sympy
import random
from Crypto.Util.number import bytes_to_long

def generate_rsa_key(bits=512):
    p = sympy.randprime(2**(bits - 1), 2**bits)
    
    delta = random.randint(1, 10000)
    q = sympy.nextprime(p + delta)

    N = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)

    return {
        'p': p,
        'q': q,
        'N': N,
        'e': e,
        'd': d
    }

def encrypt_flag(flag, e, N):
    m = bytes_to_long(flag.encode())
    c = pow(m, e, N)
    return c

flag = "FLAG REDACTED"
rsa = generate_rsa_key(bits=512)
ciphertext = encrypt_flag(flag, rsa['e'], rsa['N'])

print(f"N = {rsa['N']}")
print(f"e = {rsa['e']}")
print(f"c = {ciphertext}")
