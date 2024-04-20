import math 
import random
import time
import Program1


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
        
encrypt = int(input("please enter the encrypted text"))
decrypt = int(input("please enter the decrypted text "))
p = int(input("please enter p "))
q = int(input("please enter q "))
n = int(input("please enter n "))
e = int(input("please enter e "))

# bits = int(input("how many bits do u want 8-bits or 16-bits"))

seconds_length = time.time()

totient = (q-1) * (p-1)

def bruteforce(e, totient, encrypted, message):
    for i in range(2, totient):
        if (e * i) % totient == 1: 
            decrypted = pow(encrypted, i, n)
            if decrypted == message:
                return i
    return None

bruteforce2 = bruteforce(e,totient,encrypt,decrypt)
print("the private key is ", bruteforce2)

final_time = time.time() - seconds_length
final_time *= 1000
print(f"The time taken: {final_time:.15f} milliseconds")