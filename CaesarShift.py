
#ascii range for letter 65 - 90

def EncryptCaesarCypher(string, shift):

    encryptedString = ''
    i=0
    string = string.upper()
    string = string.replace(' ','')
    upper = len(string)

    while i < upper:

        letter = string[i]
        letter = ord(letter)

        encryptedLetter = letter + shift
        if encryptedLetter > 90:
            dif = encryptedLetter - 90
            encryptedLetter = 64 + dif
        elif encryptedLetter < 65:
            dif = 65 - encryptedLetter
            encryptedLetter = 91 - dif
            
        encryptedLetter = chr(encryptedLetter)
        encryptedString = encryptedString + encryptedLetter
        i+=1


    return encryptedString


def DecryptCaesarCypher(string, shift):
    decryptedString = ''
    i=0
    string = string.upper()
    string = string.replace(' ','')
    upper = len(string)

    while i < upper:

        letter = string[i]
        letter = ord(letter)

        decryptedLetter = letter - shift
        if decryptedLetter > 90:
            dif = decryptedLetter - 90
            decryptedLetter = 64 + dif
        elif decryptedLetter < 65:
            dif = 65 - decryptedLetter
            decryptedLetter = 91 - dif
            
        decryptedLetter = chr(decryptedLetter)
        decryptedString = decryptedString + decryptedLetter
        i+=1

    return decryptedString