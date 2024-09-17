import argparse
import random


# This is a convenience function for main(). You don't need to touch it.
def prime_test(N: int, k: int) -> tuple[str, str]:
    return fermat(N, k), miller_rabin(N, k)


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0 :
        return 1
    z= mod_exp(x, y//2, N) 

    #if Y is even
    if y % 2 == 0:
        return (z*z) % N 
    
    #if y is odd 
    else:
        return (x * (z * z)) % N


# You will need to implement this function and change the return value.
def fprobability(k: int) -> float:
    return 1-(.5**k)


# You will need to implement this function and change the return value.
def mprobability(k: int) -> float:
    
    return 1 -(.25**k)


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N: int, k: int) -> str:
    #negative numbers and 0 are not prime 
    if N <= 1:
        return "composite"
    for i in range(k) :
        i_rand = random.randint(2, N-2)
        if mod_exp(i_rand, N-1, N) != 1:
            return "composite"
    return "prime"


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.
def miller_rabin(N: int, k: int) -> str:
    if N <= 1:
        return 'composite'
    if N == 2:
        return 'prime'
    if N % 2 == 0:
        return 'composite'

    # Write N-1 as 2^s * d
    s = 0
    d = N - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform the test k times
    for _ in range(k):
        a = random.randint(2, N - 2)
        x = mod_exp(a, d, N)
        if x == 1 or x == N - 1:
            continue
        for _ in range(s - 1):
            x = mod_exp(x, 2, N)
            if x == N - 1:
                break
        else:
            return 'composite'
    return 'prime'


def main(number: int, k: int):
    fermat_call, miller_rabin_call = prime_test(number, k)
    fermat_prob = fprobability(k)
    mr_prob = mprobability(k)

    print(f'Is {number} prime?')
    print(f'Fermat: {fermat_call} (prob={fermat_prob})')
    print(f'Miller-Rabin: {miller_rabin_call} (prob={mr_prob})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()
    main(args.number, args.k)
