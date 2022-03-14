bangchucai = "abcdefghijklmnopqrstuvwxyz"

def encryption(plaintext, key):
    cyphertext = ""

    for i in range(0,len(plaintext)):
        cyphertext += key[bangchucai.index(plaintext[i])]
    return cyphertext

def decryption(cyphertext , key):
    plaintext = ""

    for i in range(0, len(cyphertext)):
        plaintext += bangchucai[key.index(cyphertext[i])]
    return plaintext

plaintext = "thegrassarealway"
key = "hlxqpsvkmzycduegjtnfbaiwor"

cyphertext = encryption(plaintext,key)
print(cyphertext)
print(decryption(cyphertext,key))
