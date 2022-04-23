from cmath import sqrt

def isPrimeNumber(number):
    if(number<2):
        return False
    for i in range(2, int(sqrt(number).real)+1):
        if(number%i==0):
            return False
    return True

def Euler(number):
    euler = 1  
    
    if(isPrimeNumber(number)):      #case number la so nguyen to 
        return number-1
    
    listSoNT = []                   #phan tich number thanh so nguyen to
    listTanSo = []

    for i in range(2, number+1):
        while(number%i==0):
            if(i in listSoNT):
                listTanSo[listSoNT.index(i)]+=1
            else:
                listSoNT.append(i)
                listTanSo.append(1)
            number = number/i

    for i in range(0,len(listSoNT)):
        if(listTanSo[i]==1):
            euler*=listSoNT[i]-1
        else:
            euler*= pow(listSoNT[i],listTanSo[i]) - pow(listSoNT[i],listTanSo[i]-1)

    print(listSoNT)
    print(listTanSo)
    return euler

def check(a,n):             #ktra xem a co phai la can nguyen thuy cua n
    pi_n = Euler(n)

    lst_uoc_n = []

    for i in range(1,pi_n+1):
        if(pi_n%i==0):
            lst_uoc_n.append(i)

    for uoc in lst_uoc_n:
        if(uoc<pi_n):
            if(pow(a,uoc)%n==1):
                return False
    return True

print(check(3,353))


