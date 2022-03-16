def encryption(plaintext,key):
    cyphertext =""

    matrixText = [""]*(key)

    for i in range(0, len(plaintext)):          #các số có vị trí đồng dư khi chia cho key cùng 1 hàng
        matrixText[i%key]+=plaintext[i]

    for i in range(0,key):                      #nối các hàng trong matrixKey
        cyphertext+=matrixText[i]

    return cyphertext

def decryption(cyphertext,key):
    plaintext = ""

    soHangNhieuHon = len(cyphertext)%key

    minCol = len(cyphertext)//key
    maxCol = minCol+1

    #Chia cypher text ra thành 2 phần 1 phần có 3 cột trong maxtrixKey
    #1 phần có 2 cột

    matrixKey = [""]*maxCol
    for i in range(0, soHangNhieuHon*maxCol):
        matrixKey[i%maxCol] += cyphertext[i]

    for i in range(soHangNhieuHon*maxCol,len(cyphertext)):
        matrixKey[i%minCol] += cyphertext[i]

    for i in range(0,len(matrixKey)):
        plaintext +=matrixKey[i]

    return plaintext

print(encryption("DONTTROUBLETROUBLE",8))
print(decryption("DBLOLENETTTRROOUUB",8))


