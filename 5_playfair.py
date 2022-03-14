bangchucai = "abcdefghiklmnopqrstuvwxyz"

def createMatrixKey(key):
    if(len(key)>25):
        key = key[0:25]
    matrixKey = [[],[],[],[],[]]

    for i in range(0,len(key)):
        matrixKey[i//5].append(key[i])
    
    indexInMatrix = len(key)    #vi tri tai ma tran dang chua co ky tu 
              
    for x in bangchucai:
        if( x in key):
            continue
        matrixKey[indexInMatrix//5].append(x)
        indexInMatrix+=1
    
    return matrixKey

def encryption(plaintext, key):
    cyphertext = ""
    matrixKey = createMatrixKey(key)
    print(matrixKey)
    
    doubleChar = []
    
    if(len(plaintext)%2!=0):
        plaintext+="x"

    for i in range(0,len(plaintext),2):
        doubleChar.append(plaintext[i]+plaintext[i+1])

    print(doubleChar)
    for x in doubleChar:
        char1 = x[0]
        char2 = x[1]
        if(char1==char2):         #neu 2 ky tu trong cap bi trung nhau
            if(char2 == "x"):
                char2 = "y"
            else:
                char2 = "x"

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
            char1 = matrixKey[rowX][(col+1)%5]
            char2 = matrixKey[rowY][(col+1)%5]
        
        elif(colX == colY):               #Case 2 : 2 ky tu cung 1 cot
            char1 = matrixKey[(rowX+1)%5][colX]
            char2 = matrixKey[(rowY+1)%5][colY]
        
        else:                               #Case 3 : 2 ky tu khac hang khac cot
            char1 = matrixKey[rowX][colY]
            char2 = matrixKey[rowY][colX]

        cyphertext += char1+char2
    return cyphertext

print(encryption("balloon","monarchy"))
    



                



