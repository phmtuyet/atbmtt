import textwrap


def hex_to_bin(hex_str: str) -> str:
    bits = "0" + str(len(hex_str) * 4) + "b"  # 08b
    return format(int(hex_str, 16), bits)


def bin_to_hex(bin_str: str) -> str:
    return hex(int(bin_str, 2))[2:]


def dec_to_bin(dec_num: int) -> str:
    bits = "04b"  # 08b
    return format(int(str(dec_num), 10), bits)


def xor(a: str, b: str) -> str:
    res = ''
    for i in range(len(a)):
        res += '0' if a[i] == b[i] else '1'
    return res
    
inverse_initial_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# E
const_expansion_permutation = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]
# IP
const_initial_permutation = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]
# P
const_permutation_function = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
const_s_box = [
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ], [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ], [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ], [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ], [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
    ], [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
    ], [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11,
    ]
]

permuted_choice_one = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]
permuted_choice_two = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


def permuted(value: str, mat, parse_bin=False) -> str:
    res = ''
    if parse_bin:
        value = hex_to_bin(value)
    for i in range(len(mat)):
        res += value[mat[i] - 1]
    return res


def split(value):
    return textwrap.wrap(value, len(value) // 2)


def left_shift_str(s: str, bits: int) -> str:
    return s[bits:] + s[:bits]


def shift_left(_c: str, _d: str, _round: int):
    schedule_of_left_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    _c = left_shift_str(_c, schedule_of_left_shift[_round - 1])
    _d = left_shift_str(_d, schedule_of_left_shift[_round - 1])

    return _c, _d


def extend(right_text: str) -> str:
    return permuted(right_text, const_expansion_permutation)


def sub(s: str) -> str:
    calc_r_split = textwrap.wrap(s, 6)
    res = ''
    for i in range(8):
        row = int(calc_r_split[i][0] + calc_r_split[i][5], 2)
        col = int(calc_r_split[i][1:5], 2)
        s_box = const_s_box[i]
        res += dec_to_bin(s_box[row * 16 + col])
    return res


def p(text: str) -> str:
    return permuted(text, const_permutation_function)


def gen_key(k: str) -> [str]:
    lst_k = []
    k = permuted(k, permuted_choice_one, True)

    for i in range(1, 17):
        c, d = split(k)
        c, d = shift_left(c, d, i)
        lst_k.append(permuted(c + d, permuted_choice_two))
        k = c + d

    return lst_k


def encrypt(plain_text: str, k: str):
    cypher_text = ''
    plain_text = permuted(plain_text, const_initial_permutation, True)
    l, r = split(plain_text)
    key_list = gen_key(k)

    print('Encrypt')
    for i in range(1, 17):
        # calc_plaintext
        new_l = r

        r = permuted(r, const_expansion_permutation)
        r = xor(r, key_list[i - 1])
        r = sub(r)
        r = permuted(r, const_permutation_function)

        new_r = xor(r, l)
        l, r = new_l, new_r
        print('Round ' + str(i), bin_to_hex(l), bin_to_hex(r), bin_to_hex(key_list[i - 1]))

    l, r = r, l
    cypher_text += permuted(l + r, inverse_initial_permutation)

    return cypher_text


def decryption(cypher_text: str, k: str):
    plain_text = ''
    cypher_text = permuted(cypher_text, const_initial_permutation, True)
    l, r = split(cypher_text)
    key_list = gen_key(k)

    print('Decrypt')
    for i in range(1, 17):
        new_l = r

        r = permuted(r, const_expansion_permutation)
        r = xor(r, key_list[16 - i])
        r = sub(r)
        r = permuted(r, const_permutation_function)

        new_r = xor(l, r)
        l, r = new_l, new_r
        print('Round ' + str(i), bin_to_hex(l), bin_to_hex(r), bin_to_hex(key_list[i - 1]))

    l, r = r, l
    plain_text += permuted(l + r, inverse_initial_permutation)

    return plain_text


if __name__ == '__main__':
    output = bin_to_hex(encrypt('02468aceeca86420', '0f1571c947d9e859'))
    print(output)
    print(bin_to_hex(decryption(output, '0f1571c947d9e859')))