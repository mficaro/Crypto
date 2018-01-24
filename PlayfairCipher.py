# NOTE: I REPRESENTS LETTERS I AND J
#       When decrypting we assuing I is the proper plain letter
#       When encrypting we set cipher letter to I
#       So basically there will never be a J after we encrypt or decrypt
#       Go through by hand and determine if plaintext should be an I or a J

def ReadKey(key):
    result = {}
    
    # loop through key and populate dictionary
    for i in range(0,5):
        for j in range(0,5):
            if key[i][j] == "I":
                result["I"] = (i,j)
                result["J"] = (i,j)
            else:
                result[key[i][j]] = (i,j)
    
    return result


def Decrypt(key, c):
    p = ""
    dic = ReadKey(key)

    i = 0
    while i < len(c):
        char1 = c[i]
        i += 1
        char2 = c[i]
        char1_row = dic[char1][0]
        char1_col = dic[char1][1]
        char2_row = dic[char2][0]
        char2_col = dic[char2][1]
        if (char1 == char2): # same char
            p += char1
            p += char2
        elif (char1_row == char2_row): # same row
            new_char1_col = (char1_col - 1) % 5
            new_char2_col = (char2_col - 1) % 5
            p += key[char1_row][new_char1_col]
            p += key[char2_row][new_char2_col]
        elif (char1_col == char2_col): # same col
            new_char1_row = (char1_row - 1) % 5
            new_char2_row = (char2_row - 1) % 5
            p += key[new_char1_row][char1_col]
            p += key[new_char2_row][char2_col]
        else: # same row, opposite col
            p += key[char1_row][char2_col]
            p += key[char2_row][char1_col]
        i += 1
    return p

def Encrypt(key, p):
    c = ""
    dic = ReadKey(key)

    i = 0
    while i < len(p):
        char1 = p[i]
        i += 1
        char2 = p[i]
        char1_row = dic[char1][0]
        char1_col = dic[char1][1]
        char2_row = dic[char2][0]
        char2_col = dic[char2][1]
        if (char1 == char2): # same char
            c += char1
            c += char2
        elif (char1_row == char2_row): # same row
            new_char1_col = (char1_col + 1) % 5
            new_char2_col = (char2_col + 1) % 5
            c += key[char1_row][new_char1_col]
            c += key[char2_row][new_char2_col]
        elif (char1_col == char2_col): # same col
            new_char1_row = (char1_row + 1) % 5
            new_char2_row = (char2_row + 1) % 5
            c += key[new_char1_row][char1_col]
            c += key[new_char2_row][char2_col]
        else: # same row, opposite col
            c += key[char1_row][char2_col]
            c += key[char2_row][char1_col]
        i += 1
    return c


jfkKey = [
    ["R", "O", "Y", "A", "L"],
    ["N", "E", "W", "Z", "D"],
    ["V", "B", "C", "F", "G"],
    ["H", "I", "K", "M", "P"],
    ["Q", "S", "T", "U", "X"]
]

jfkcipher = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"

key_311a = [
    ["M","F","H","I","K"],
    ["U","N","O","P","Q"],
    ["Z","V","W","X","Y"],
    ["E","L","A","R","G"],
    ["D","S","T","B","C"],
]

plaintext_311 = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCEX"
print(Encrypt(key_311a, plaintext_311))

key_311b = [
    ["L","A","R","G","E"],
    ["S","T","B","C","D"],
    ["F","H","I","K","M"],
    ["N","O","P","Q","U"],
    ["V","W","X","Y","Z"],
]

print(Encrypt(key_311b, plaintext_311))




