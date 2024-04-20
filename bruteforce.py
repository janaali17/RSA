import math
import random
import time

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

p = int(input("please enter p "))
q = int(input("please enter q "))
n = int(input("please enter n "))
e = int(input("please enter e "))
encrypt = int(input("please enter a text to encrypt")) 
decrypt = int(input("please enter a text to decrypt"))
# bits = int(input("how many bits do u want 8-bits or 16-bits"))

seconds_lenghth = time.time()

totient = (p-1)*(q-1)
def bruteforce(e,totient,encrypted,decrypt)