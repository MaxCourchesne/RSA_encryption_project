
# this gcd function is based on the euclidian algorithm
def gcd(n, m):
    if n%m==0:
        return m
    elif m>n:
        return gcd(m, n)
    else:
        return gcd(m, n%m)

# this factor function will be used to test how long it takes to factor the modulus "n", product of two large primes
def factor(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            print(f"{n} = {i} * {int(n/i)}")
            # we found a factorization of n
            return True
        
    # It is impossible to factor "n" i.e. "n" is prime
    return False

