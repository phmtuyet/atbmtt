from pydoc import plain


bangchucai = "abcdefghiklmnopqrstuvwxyz"

def suakytuJ(text):
    newText = ""
    for i in range(0,len(text)):
        if(text[i] == 'j'):
            newText+='i'
        else:
            newText += text[i]
    return newText


def createMatrixKey(key):
    key = suakytuJ(key)
    matrixKey = [[],[],[],[],[]]

    newKey = ""      #key moi khong bi trung
    for x in key:
        if(x in newKey):
            continue
        newKey+=x

    for i in range(0,len(newKey)):
        matrixKey[i//5].append(newKey[i])
    
    indexInMatrix = len(newKey)    #vi tri tai ma tran dang chua co ky tu 
              
    for x in bangchucai:
        if( x in newKey):
            continue
        matrixKey[indexInMatrix//5].append(x)
        indexInMatrix+=1
       
    return matrixKey

def encryption(plaintext, key):
    plaintext = suakytuJ(plaintext)
    cyphertext = ""

    matrixKey = createMatrixKey(key)
    doubleChar = []

    for i in range(0,len(plaintext)+1,2):
        if(i==len(plaintext)-1):            #trường hợp bị lẻ ký tự cuối cùng
            plaintext+="q"

        if(plaintext[i]==plaintext[i+1]):
            charExtra = 'x'
            if(plaintext[i+1]=='x'):
                charExtra = 'y'
            plaintext = plaintext[0:i+1]+charExtra+plaintext[i+1:len(plaintext)]

        doubleChar.append(plaintext[i]+plaintext[i+1])

    for x in doubleChar:
        char1 = x[0]
        char2 = x[1]

        rowX = 0            #vi tri cua ky tu thu nhat trong matran key
        colX = 0
        isFindX = False

        rowY = 0            #vi tri cua ky tu thu hai trong matran key
        colY = 0
        isFindY = False

        for row in range(0,5):
            for col in range(0,5):
                if(matrixKey[row][col]==char1):
                    rowX = row
                    colX = col
                    isFindX = True
                if(matrixKey[row][col]==char2):
                    rowY = row
                    colY = col
                    isFindY = True
                if(isFindX & isFindY):
                    break
        
        if(rowX == rowY):               #Case 1 : 2 ky tu cung 1 hang
            char1 = matrixKey[rowX][(colX+1)%5]
            char2 = matrixKey[rowY][(colY+1)%5]
        
        elif(colX == colY):               #Case 2 : 2 ky tu cung 1 cot
            char1 = matrixKey[(rowX+1)%5][colX]
            char2 = matrixKey[(rowY+1)%5][colY]
        
        else:                               #Case 3 : 2 ky tu khac hang khac cot
            char1 = matrixKey[rowX][colY]
            char2 = matrixKey[rowY][colX]

        cyphertext += char1+char2
    return cyphertext


def decryption(cyphertext, key):
    plaintext = ""

    key = suakytuJ(key)
    matrixKey = createMatrixKey(key)

    doubleChar = []

    for i in range(0,len(cyphertext),2):
        doubleChar.append(cyphertext[i]+cyphertext[i+1])
    
    for x in doubleChar:
        char1 = x[0]
        char2 = x[1]

        rowX = 0            #vi tri cua ky tu thu nhat trong matran key
        colX = 0
        isFindX = False

        rowY = 0            #vi tri cua ky tu thu hai trong matran key
        colY = 0
        isFindY = False

        for row in range(0,5):
            for col in range(0,5):
                if(matrixKey[row][col]==char1):
                    rowX = row
                    colX = col
                    isFindX = True
                if(matrixKey[row][col]==char2):
                    rowY = row
                    colY = col
                    isFindY = True
                if(isFindX & isFindY):
                    break
        
        if(rowX == rowY):               #Case 1 : 2 ky tu cung 1 hang
            char1 = matrixKey[rowX][(colX-1)%5]
            char2 = matrixKey[rowY][(colY-1)%5]
        
        elif(colX == colY):               #Case 2 : 2 ky tu cung 1 cot
            char1 = matrixKey[(rowX-1)%5][colX]
            char2 = matrixKey[(rowY-1)%5][colY]
        
        else:                               #Case 3 : 2 ky tu khac hang khac cot
            char1 = matrixKey[rowX][colY]
            char2 = matrixKey[rowY][colX]

        plaintext += char1+char2
    return plaintext

print(encryption("balloon","monarchy"))
print(decryption("ibsupmna","monarchy"))


                



