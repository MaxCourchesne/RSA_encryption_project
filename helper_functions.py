# this gcd function is based on the euclidian algorithm
def gcd(n, m):
    if n%m==0:
        return m
    elif m>n:
        return gcd(m, n)
    else:
        return gcd(m, n%m)
