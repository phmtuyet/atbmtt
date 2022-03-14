bangchucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plaintext, key):
    cyphertext = ""
    for x in plaintext:
        cyphertext += bangchucai[(bangchucai.index(x) + key)%26]
    return cyphertext

def decryption(cyphertext, key):
    plaintext = ""
    for x in cyphertext:
        plaintext += bangchucai[(bangchucai.index(x) - key)%26]
    return plaintext

plaintext = "loveisblindlovei"

print(encryption(plaintext,8))
