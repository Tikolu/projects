def is_prime(x):
    if x < 2:
        return True
    i = 0
    for n in range(2,x):
        if x % n != 0:
            i += 1
    return i == x - 2

def list_prime(length):
    e = 0
    while e != length:
        e += 1
        if is_prime(e):
            print(e)
