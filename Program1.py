import math
import random

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

def get_random_prime(bit_length):
    """Generates a random prime number of a specified bit length."""
    while True:
        # Generate a random number within the desired bit length
        num = random.getrandbits(bit_length)
        # Make sure the number is odd and has the desired bit length
        num |= 1  # Ensure the number is odd
        num |= (1 << (bit_length - 1))  # Ensure the number has the correct bit length
        
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

p=5
q=9
e=2
n=p*q
eul=(p-1)*(q-1)

d= pow(e,-1,eul)
pub_key= {n,e}
pri_key= {n,d}
print("public key:" ,pub_key, "\n private key:", pri_key)
m=14
c=pow(m,e,n)
M=pow(c,d,n)
print("\n encrypt:",c, "\n decrypt:", M)