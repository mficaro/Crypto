import numpy
from CryptoHelpers import *

def Encrypt(key, p):
    c = ""
    size = len(key)

    append = len(p) % size
    for i in range(append):
        p += "X"

    print(p)

    i = 0
    while i < len(p):
        vec = [None] * size
        for j in range(size):
            vec[i % size] = CharToNum(p[i])
            i += 1
        result = numpy.matmul(key, vec) % 26
        print(result)
        for num in result:
            c += NumToChar(num)
        print(c)
    return c

# TODO
def Decrypt(key, c):
    det = numpy.linalg.det(key)
    det_1 = ModMultInverse(det, 26)


key_314 = [
    [9,4],
    [5,7]
]

p_314 = "MEETMEATTHEUSUALPLACEATTENRATHERTHANEIGHTOCLOCK"
print(len(p_314))

print(Encrypt(key_314, p_314))
