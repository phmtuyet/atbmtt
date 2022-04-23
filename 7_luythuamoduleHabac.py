def luythuamoduleHabac(a,m,n):              #a^m mod n
    if(m==1):
        return a%n
    if(m%2==0):
        return luythuamoduleHabac(a*a%n,m//2,n)
    return (luythuamoduleHabac(a*a%n,m//2,n)*a) %n

print(luythuamoduleHabac(241,850,6737))
print(pow(241,850,6737))