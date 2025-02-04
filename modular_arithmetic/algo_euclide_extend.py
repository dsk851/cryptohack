import math
def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0  # Cas de base : PGCD = a, x = 1, y = 0
    else:
        pgcd, x1, y1 = euclide_etendu(b, a % b)  # Appel récursif
        x = y1
        y = x1 - (a // b) * y1
        return pgcd, x, y

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modular_arithm(a,m):
    b = a%m
    return b

def modular_arithm2(a,b,c):
    return (a**b)%c


if __name__ == "__main__":
    a, b = 26513, 32321
    pgcd, x1, y1 = euclide_etendu(a, b)
    print(pgcd,x1,y1)

    print('Modular arithmetic\n')

    a = 11
    m = 6
    b = modular_arithm(a,m)
    print(f"b = {b}")

    
    a = 8146798528947
    m = 17
    b = modular_arithm(a,m)
    print(f"b = {b} (second modulus)")

    print('Modular arithmetic 2\n')

    print(modular_arithm2(5,16,17))