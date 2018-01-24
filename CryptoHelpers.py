import sys
import math    

def ExtEuclidAlg(a,b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def gcd(a,b):
    return ExtEuclidAlg(a,b)[0]

def CharToNum(char):
    return ord(char.capitalize()) - ord("A")

def NumToChar(num):
    return chr(num + ord("A"))

def ModMultInverse(a,m):
    result = ExtEuclidAlg(a,m)
    if result[0] is not 1:
        print("Error: no modular multiplicative inverse of {} and {}".format(a,m))
        return None
    return result[1] % m