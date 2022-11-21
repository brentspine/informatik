length = int(input("Länge eingeben: "))
 
def fakul_iteration(length):
    r = 1
    for i in range(length):
        r *= (i+1)
    return r
 
 
def fakul_rekursion(r, length):
    # print("r: " + str(r) + " l: " + str(length))
    if length == 1:
        return r
    return fakul_rekursion(r*length, length-1)
 
print(fakul_iteration(length))
print(fakul_rekursion(1, length))