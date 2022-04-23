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

def public_key(p: int, q: int, e: int) -> (int, int):
    n = p * q
    return e, n


def private_key(p: int, q: int, e: int) -> (int, int):
    n = p * q
    fi_n = (p - 1) * (q - 1)
    d = extendedEuclid(e, fi_n)
    return d, n


def rsa_authentication_encrypt(p: int, q: int, e: int, plain_text: int) -> int:
    d, n = private_key(p, q, e)
    cypher_text = pow(plain_text,d)%n
    return cypher_text


def rsa_authentication_decrypt(p: int, q: int, e: int, cypher_text: int) -> int:
    e, n = public_key(p, q, e)
    plain_text = pow(cypher_text, e)% n
    return plain_text


def rsa_confidentiality_encrypt(p: int, q: int, e: int, plain_text: int) -> int:
    e, n = public_key(p, q, e)
    cypher_text = pow(plain_text, e)% n
    return cypher_text


def rsa_confidentiality_decrypt(p: int, q: int, e: int, cypher_text: int) -> int:
    d, n = private_key(p, q, e)
    plain_text = pow(cypher_text, d)% n
    return plain_text


if __name__ == '__main__':
    m, p, q, e = 47, 37, 59, 53
    enc = rsa_authentication_encrypt(p, q, e, m)
    dec = rsa_authentication_decrypt(p, q, e, enc)
    print(enc)
    print(dec)

    enc = rsa_confidentiality_encrypt(p, q, e, m)
    dec = rsa_confidentiality_decrypt(p, q, e, enc)
    print(enc)
    print(dec)