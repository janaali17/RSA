import math # so that python can understand any mathmatical equation
import random # for generating random integrs

x = int(input("\nwhat would you like your input length to be? 8-bits or 16-bits ")) 
# takes input from the user that asks for the length in bits
message= int(input("please enter a number to encrypt "))
# asks the user to enter a number encrypt 
def is_prime(num): # creating a function named "is_prime" to checks if a number is prime using trial division
    if num <= 1: # creating a conditional statement that checks if the num is less than or equal to 1
        return False # if the above condition is true then return false
    if num <= 3: #creating a conditional statement that checks if the num is less than or equal to 3
        return True #if the above condition is true then return true 
    if num % 2 == 0 or num % 3 == 0: 
    #creating a conditional statement that checks if num modulus 2 is equal to 0 or num modulus 3 is equal to 0 
        return False # if the above condition is true then return false
    i = 5 # assigning i to 5
    while i * i <= num: # creating a while loop that multplies i by i and checks if the product is less than or equal to the num
        if num % i == 0 or num % (i + 2) == 0: # if num mod 5 or num mod 7 is equal to 0 
            return False # then prints false
        i += 6 # add 6 to i which is 5 
    return True # else prints true 

def random_prime(x): 
    # creating a function named "get_random_prime" to generates a random prime number of a specified bit length

    while True: # creating a while loop to generate a random number within the desired bit length
        num = random.getrandbits(x)
        # make sure the number is odd and has the desired bit length
        num |= 1  # ensure the number is odd
        num |= (1 << (x - 1))  # ensure the number has the correct bit length
        
        # check if the number is prime
        if is_prime(num): # creating 
            return num # returns the output of num
def extended_gcd(a, b): 
    # creating a function named "extended_gcd" to find the gcd of a and b and coefficients x and y
    if a == 0: # condition to check if a is equal to 0
        return b, 0, 1 # if the above condition is true then print b, 0, 1
    else: # otherwise if it is false
        gcd, x1, y1 = extended_gcd(b % a, a) # if a != 0 
        x = y1 - (b // a) * x1 # this formula is to calculate coff of x and y  
        y = x1 
        return gcd, x, y # print out gcd,and calculated x and y 

def RSA_k(x):
    # creating a function named "RSA_k" to generates RSA public and private keys
    # generate prime numbers p and q
    if x == 8: # condition to check if x is equal to 8
        p = random_prime(8)  
        q = random_prime(8)
    elif x == 16: # otherwise if x is equal to 16
        p = random_prime(16)
        q = random_prime(16)
    else: # otherwise 
        exit() # if both are not true exit
    
    # compute n and euler's totient function
    n = p * q #euler's function (rule)
    eul = (p - 1) * (q - 1) # rule 
    
    # choose a public e (exponent)
    e = 65537  # common choice for e
    
    # ensure e is Co-prime to euler totient
    gcd, x, y = extended_gcd(e, eul)
    
    while gcd != 1: # creating while loo[ to check is gcd is not equal to 1]
        e = random.randint(2, eul - 1) 
        gcd, x, y = extended_gcd(e, eul)
    
   
    d = x % eul # calculating d which is x modulus eul
    if d < 0: # condition if d is less than 0  
        d += eul # d is equal to d plus eul
    
    public_key = (n, e) # public key is n and e 
    private_key = (n, d) # private key is n and d
    print("p: " , p) # print "p: " then the output of p
    print("q: " , q) # print "q: " then the output of q
    print("n: ", n) # print "n: " then the output of n
    print("e: ", e) # print "e: " then the output of e
    print("d: ", d) # print "d: " then the output of d
    return public_key, private_key # 

# Generate RSA keys
public_key, private_key = RSA_k(x)
print("Public key:", public_key) # print "public key: " then the output of public key
print("Private key:", private_key) # print "private key: " then the output of private key

(n, e) = public_key 
(n, d) = private_key

c =pow(message, e, n) 

M = pow(c, d, n)

print("\nEncrypted message:", c)
print("Decrypted message:", M)
