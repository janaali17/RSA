import math # so that python can understand any mathmatical equation
import random # for generating random integrs
import time # figures out time taken to excute the code
import mainprogram # extracting functions from a different file

def is_prime(num): #O(1)
    # creating a function named "is_prime" to checks if a number is prime using trial division
    if num <= 1: #O(1)
        # creating a conditional statement that checks if the num is less than or equal to 1
        return False # if the above condition is true then return false
    if num <= 3: #O(1)
         # creating a conditional statement that checks if the num is less than or equal to 3
        return True # if the above condition is true then return true
    if num % 2 == 0 or num % 3 == 0: #O(1)
        # creating a conditional statement that checks if num modulus 2 is equal to 0 or num modulus 3 is equal to 0
        return False # if the above condition is true then return false
    i = 5
    while i * i <= num: # O(N)
        if num % i == 0 or num % (i + 2) == 0: #O(1)
            return False
        i += 6
    return True

def random_prime(bit_length): #O(1)
    # creating a function named "random_prime" to generates a random prime number of a specified bit length
    while True: # O(N)
        # creating a while loop to generate a random number within the desired bit length
        num = random.getrandbits(bit_length)
        # Make sure the number is odd and has the desired bit length
        num |= 1  # ensure the number is odd
        num |= (1 << (bit_length - 1))  # ensure the number has the correct bit length
        
        # check if the number is prime
        if is_prime(num):#O(1)
            return num # returns the output of num
        
encrypted = int(input("\nplease enter the encrypted text ")) 
# ask the user to enter the encrypted text
decrypt = int(input("please enter the decrypted text "))
# ask the user to enter the decrypt a text
p = int(input("\nplease enter p ")) # print "p: " then the output of p
q = int(input("please enter q ")) # print "q: " then the output of q
n = int(input("please enter n ")) # print "n: " then the output of n
e = int(input("please enter e ")) # print "e: " then the output of e

seconds_length = time.time()

totient = (q-1) * (p-1)

def bruteforce(e, totient, encrypted, message):
    for i in range(2, totient): # O(N)
        if (e * i) % totient == 1: #O(1)
            decrypted = pow(encrypted, i, n) 
            if decrypted == message:
                return i
    return None

bruteforce2 = bruteforce(e,totient,encrypted,decrypt)
print("the private key is ", bruteforce2)

ftime = time.time() - seconds_length
ftime *= 1000
print(f"The time taken: {ftime:.10f} milliseconds")