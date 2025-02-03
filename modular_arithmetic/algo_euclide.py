 
def pgcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a


a = 52920 
b = 66528

r = pgcd(a, b)
print(f"PGCD ( {a} , {b} ) = {r} ")
