from cs50 import get_string
import sys

newKey = 0
#newKey

if len(sys.argv) != 2:
    sys.exit()

key = int(sys.argv[1])
cipherText=""
plainText = get_string("plain text: ")

print("ciphertext: ",end="")

for j in range(len(plainText)):
    newKey=key
    if plainText[j].isalpha() == False:
        cipherText += (plainText[j])
    elif plainText[j].isupper() == True:
        if ord(plainText[j]) + newKey > ord("Z"):
            newKey = ((ord(plainText[j]) + newKey) % ord("Z")) %26
            cipherText += chr(ord("A") + newKey - 1)
        else:
            cipherText += chr(ord(plainText) + newKey)
    else:
        if ord(plainText[j]) + newKey > ord("z"):
            newKey = ((ord(plainText[j]) + newKey) % ord("z")) %26
            cipherText += chr(ord("a") + newKey - 1)
        else:
            cipherText += chr(ord(plainText[j]) + newKey)
print(cipherText)