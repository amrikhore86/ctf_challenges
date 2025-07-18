import sympy
import random
from Crypto.Util.number import bytes_to_long

# --- Generate weak primes ---
def generate_weak_rsa_key(bits=512):
    # Generate a base prime p
    p = sympy.randprime(2**(bits - 1), 2**bits)
    
    # Make q close to p (p + small delta)
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

# --- Encrypt flag ---
def encrypt_flag(flag, e, N):
    m = bytes_to_long(flag.encode())
    c = pow(m, e, N)
    return c

# --- Main logic ---
flag = "flag{Fermat_Factorization_Works}"
rsa = generate_weak_rsa_key(bits=512)
ciphertext = encrypt_flag(flag, rsa['e'], rsa['N'])

# --- Output for CTF ---
print("==== CTF CHALLENGE ====")
print(f"N = {rsa['N']}")
print(f"e = {rsa['e']}")
print(f"c = {ciphertext}")
print("\n(Note: p and q are close!)")
