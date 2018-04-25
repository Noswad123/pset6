from cs50 import get_string
import sys

keyCounter = 0
#keyChar

if len(sys.argv) != 2:
    print("usage: Python vigenere <cipherText>")
    sys.exit()

key = sys.argv[1]

for i in range(len(key)):
    if key[i].isalpha() == False:
        sys.exit


plainText = get_string("plain text: ")
cipherText = ""

print(len(plainText))
print("ciphertext: ",end="")

for j in range(len(plainText)):
    if plainText[j].isalpha() == False:
        cipherText += plainText[i]
    else:
        if key[keyCounter].isupper() == True:
            keyChar = ord(key[keyCounter]) - ord("A")
        else:
            keyChar = ord(key[keyCounter]) - ord("a")

    if plainText.isupper() == True:
        if ord(plainText[j]) + keyChar > ord("Z"):
            keyChar = ((ord(plainText[j]) + keyChar) % ord("Z")) %26
            cipherText += chr(ord("A") + keyChar - 1)
        else:
            cipherText.append(chr(ord(plainText) + keyChar))
    else:
        if ord(plainText[j]) + keyChar > ord("z"):
            keyChar = ((ord(plainText[j]) + keyChar) % ord("z")) %26
            cipherText += chr(ord("a") + keyChar - 1)
        else:
            cipherText += chr(ord(plainText[j]) + keyChar)

    keyCounter +=1
    if(keyCounter == len(key)):
        keyCounter = 0
print(cipherText)