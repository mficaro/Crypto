from CryptoHelpers import *

def EncryptDecryptPartA(left, right):
    l = left
    r = right

    print("Input={} {}".format(bin(l), bin(r)))
    
    counter = 1
    for i in range(16):
        l_temp = r
        r = (l ^ 0b1111)
        l = l_temp
        # print()
        # print('round={}'.format(counter))
        # print('left={}'.format(bin(l)))
        # print('right={}'.format(bin(r)))
        counter += 1

    l_temp = r
    r = l
    l = l_temp
    print("Output={} {}".format(bin(l),bin(r)))

    return (l,r)


def EncryptDecryptPartB(left, right):
    l = left
    r = right

    print("Input={} {}".format(bin(l), bin(r)))
    
    counter = 1
    for i in range(16):
        l_temp = r
        r = (l ^ (r ^ 0b1111))
        l = l_temp
        print()
        print('round={}'.format(counter))
        print('left={}'.format(bin(l)))
        print('right={}'.format(bin(r)))
        counter += 1

    l_temp = r
    r = l
    l = l_temp
    print("Output={} {}".format(bin(l),bin(r)))

    return (l,r)

# print("ENCRYPTING")
# encrypt = EncryptDecryptPartA(0b1010, 0b0111)
# print("DECRYPTING")
# decrypt = EncryptDecryptPartA(encrypt[0], encrypt[1])

print("ENCRYPTING")
encrypt = EncryptDecryptPartB(0b1010, 0b0111)
print("DECRYPTING")
decrypt = EncryptDecryptPartB(encrypt[0], encrypt[1])