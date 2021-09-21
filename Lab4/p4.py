def gcd(a, b):
    if a == 0:
        return b
    b = b % a
    return gcd(b, a)

def simplify_fraction(n, m):
    g = gcd(min(n, m), max(n, m))
    print('{}/{}'.format(n//g, m//g))

def simplify_fraction_bad(n, m):
    for i in range(min(n, m))[::-1]:
        if n % i == 0 and m % i == 0:
            print(f'{n//i}/{m//i}')
            return

            
simplify_fraction(16, 12)
simplify_fraction_bad(16, 12)


