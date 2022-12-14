length = int(input("Lange eingeben: "))

def fibo_iteration(length):
    r = 0
    last = 1
    for i in range(length-1):
        t = r
        r += last
        last = t
    return r


def fibo_rekursion(r, last, length):
    if length == 1:
        return r
    return fibo_rekursion(r+last, r, length-1)

print(fibo_iteration(length))
print(fibo_rekursion(0, 1, length))