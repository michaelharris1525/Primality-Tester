import random
import sys

# This may come in handy...
from fermat import miller_rabin

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    The Extended Euclid algorithm
    Returns x, y , d such that:
    - d = GCD(a, b)
    - ax + by = d

    Note: a must be greater than b
    """
    if b == 0:
        return (1,0,a)
    #finds the GCD 
    rem = a % b 
    n_x, n_y, gcd = ext_euclid(b, rem)

    #finds x and y from the linear equation ax + by = remainder
    x = n_y
    y = n_x - (a//b) * n_y
    
    return (x, y, gcd)


# Implement this function
def generate_large_prime(bits=512) -> int:
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    #def is_prime(p_num: int) -> bool: 
        #for i in range(2, (p_num //2 +1)):
            #if ((p_num % 1) == 0):
                #return False
        #return True


    
    
    while True:
        possible_prime = random.getrandbits(bits)
        # Ensure the candidate is odd and has the correct bit length
        possible_prime |= (1 << (bits -1)) #set the most significant bit to make sure the correct bit length
        possible_prime |= 1 #makes sure it is odd
        if(miller_rabin(possible_prime, 20) == "prime"): 
            return possible_prime
       # break
    #generate_large_prime(random.getrandbits(bits))
    
 # Guaranteed random prime number obtained through fair dice roll

def mod_inverse(e: int, phi: int) -> int:
    """Compute the modular multiplicative inverse of e modulo phi."""
    x, _, gcd = ext_euclid(e, phi)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for e = {e} and phi = {phi}.")
    return x % phi

# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q 
    r = (p-1)*(q-1)
    e = 17
    d = mod_inverse(e, r)



    return n, e, d
