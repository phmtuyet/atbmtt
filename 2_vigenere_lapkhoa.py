bangchucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plaintext , key):
    cyphertext = ""

    for i in range(0,len(plaintext)):
        cyphertext+= bangchucai[(bangchucai.index(plaintext[i])+bangchucai.index(key[i%len(key)]))%26]

    return cyphertext

def decryption(cyphertext , key):
    plaintext = ""

    for i in range(0,len(cyphertext)):
        plaintext+= bangchucai[(bangchucai.index(cyphertext[i])-bangchucai.index(key[i%len(key)]))%26]

    return plaintext

plaintext = "bettersafeth"
key = "itsasm"

print(encryption(plaintext,key))