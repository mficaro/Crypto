from CryptoHelpers import *
import VigenereCipher
import AffineCipher

c = "kqerejebcppcjcrkieacuzbkrvpkrbcibqcarbjcvfcupkriofkpacuzqepbkrxpeiieabdkpbcpfcdccafieabdkpbcpfeqpkazbkrhaibkapcciburccdkdccjcidfuixpafferbiczdfkabicbbenefcupjcvkabpcydccdpkbcocperkivkscpicbrkijpkabi"

# for a in range(1000):
#     if gcd(a,26) is not 1:
#             continue
#     for b in range(26):
#         if (a * 4 + b) % 26 == 2:
#             print("a={}, b={}".format(a,b))
#             print(AffineCipher.Decrypt(a,b,c))

print(AffineCipher.Decrypt(19,4,c))

