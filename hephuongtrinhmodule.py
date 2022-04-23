from asyncio.windows_events import NULL


def extendedEuclid(n,a):            #a^-1 mod n
    (a1 , a2 , a3) = (1 , 0 , n)
    (b1 , b2 , b3) = (0 , 1 , a)

    while(b3 not in [0,1]):
        q = a3 // b3
        (t1,t2,t3)=(a1 - q * b1 , a2 - q * b2 , a3 - q*b3)
        (a1, a2, a3) = (b1, b2, b3)
        (b1,b2,b3)= (t1,t2,t3)
    
    if(b3 == 0):
        return NULL
    if(b3 == 1):
        return b2

def giaihe(lst_m , lst_a):
    lst_c = []
    lst_M = []

    aici=0
    M=1
    for mi in lst_m:
        M*=mi

    for i in range(0,len(lst_m)):
        Mi = M//lst_m[i]
        lst_M.append(Mi)
        lst_c.append(Mi*((extendedEuclid(Mi,lst_m[i]))))
        aici += lst_a[i]*lst_c[i]

    return aici%M

print(giaihe([17,19,11],[16,18,7]))
    