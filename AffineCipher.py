from CryptoHelpers import *
import VigenereCipher

def Encrypt(a,b,p):
    c = ""
    if gcd(a,26) is not 1:
        print("Error: a is invalid (a and 26 must be coprime)")
        exit(1)
    for char in p:
        c += NumToChar((a * CharToNum(char) + b) % 26)
    return c


def Decrypt(a,b,c):
    p = ""
    inv = ModMultInverse(a,26)
    if inv is None:
        print("Error: a is invalid (a and 26 mist be coprime)")
        exit(1)
    for char in c:
        p += NumToChar((inv * (CharToNum(char) - b)) % 26)
    return p




