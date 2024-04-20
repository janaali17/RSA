import math
import random

x = int(input("what would you like your input length to be? 8-bits or 16-bits "))
message= input("please enter a message to encrypt ")
def is_prime(num):
    """Checks if a number is prime using trial division."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_random_prime(x):
    """Generates a random prime number of a specified bit length."""
    while True:
        # Generate a random number within the desired bit length
        num = random.getrandbits(x)
        # Make sure the number is odd and has the desired bit length
        num |= 1  # Ensure the number is odd
        num |= (1 << (x - 1))  # Ensure the number has the correct bit length
        
        # Check if the number is prime
        if is_prime(num):
            return num
def extended_gcd(a, b):
    """Extended Euclidean algorithm to find the gcd of a and b and coefficients x and y."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def rsa_key_generation(x):
    """Generates RSA public and private keys."""
    # Generate prime numbers p and q
    if x == 8:
        p = get_random_prime(8)
        q = get_random_prime(8)
    elif x == 16:
        p = get_random_prime(16)
        q = get_random_prime(16)
    else: 
        exit()
    
    # Compute n and euler's totient function (eul)
    n = p * q
    eul = (p - 1) * (q - 1)
    
    # Choose a public exponent e
    e = 65537  # Common choice for e
    
    # Ensure e is coprime to eul
    gcd, x, y = extended_gcd(e, eul)
    
    while gcd != 1:
        e = random.randint(2, eul - 1)
        gcd, x, y = extended_gcd(e, eul)
    
    # Calculate the private exponent d
    d = x % eul
    if d < 0:
        d += eul
    
    # Return public and private keys
    public_key = (n, e)
    private_key = (n, d)
    print("p: " , p)
    print("q: " , q)
    print("n: ", n)
    print("e: ", e)
    print("d: ", d)
    return public_key, private_key

# Generate RSA keys
public_key, private_key = rsa_key_generation(x)
print("Public key:", public_key)
print("Private key:", private_key)

# Test encryption and decryption
# Message to be encrypted

n, e = public_key
n, d = private_key

# Encrypt the message
# c =pow(message, e, n)

# Decrypt the message
# M = pow(c, d, n)

# print("\nEncrypted message:", c)
# print("Decrypted message:", M)
print("n =", n)