bangchucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plaintext , key):
    cyphertext = ""
    key = key + plaintext

    for i in range(0,len(plaintext)):
        cyphertext+= bangchucai[(bangchucai.index(plaintext[i])+bangchucai.index(key[i]))%26]

    return cyphertext

def decryption(cyphertext , key):
    plaintext = ""

    for i in range(0,len(cyphertext)):
        kytumoi = bangchucai[(bangchucai.index(cyphertext[i])-bangchucai.index(key[i]))%26]
        key+=kytumoi
        plaintext+=kytumoi

    return plaintext

plaintext = "moneymakesth"
key = "nopain"

print(encryption(plaintext,key))
print(decryption("zccegzmyrwrt",key))