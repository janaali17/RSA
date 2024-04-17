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
p=5
q=9
e=2
n=p*q
eul=(p-1)*(q-1)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
        return a
    while e<eul:
        if gcd(e,eul)== 1:
            break
        else:
            e+=1
d= pow(e,-1,eul)
pub_key= {n,e}
pri_key= {n,d}
print("public key:" ,pub_key, "\n private key:", pri_key)
m=14
c=pow(m,e,n)
M=pow(c,d,n)
print("\n encrypt:",c, "\n decrypt:", M)