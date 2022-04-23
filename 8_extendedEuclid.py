from asyncio.windows_events import NULL


def extendedEuclid(n,a):            #a^-1 mod n
    (a2 , a3) = (0 , n)
    (b2 , b3) = (1 , a)

    while(b3 not in [0,1]):
        q = a3 // b3
        (t2,t3)=(a2 - q * b2 , a3 - q*b3)
        (a2,a3) = (b2, b3)
        (b2,b3)= (t2,t3)
    
    if(b3 == 0):
        return NULL
    if(b3 == 1):
        return b2%n

print(extendedEuclid(5,17))