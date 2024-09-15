import math
from collections import Counter


def count_letters(num_of_let, str_file):
    substr_counts = Counter(str_file[i:i + num_of_let] for i in range(len(str_file) - num_of_let + 1))

    alf_letters = {substr: [count, count / (len(str_file) - num_of_let + 1), ''] for substr, count in
                   substr_counts.items()}

    return alf_letters

def Code_Huffman(alf):
    num_of_let = len(next(iter(alf)))
    alf_dict = [(k, v[1]) for k, v in alf.items()]

    while len(alf_dict) > 1:
        alf_dict = sorted(alf_dict, key=lambda item: item[1], reverse=True)
        min_p, before_min_p = alf_dict[-2:]

        for symbols, code in [(min_p[0], '1'), (before_min_p[0], '0')]:
            while symbols:
                letter = symbols[:num_of_let]
                alf[letter][2] = code + alf[letter][2]
                symbols = symbols[num_of_let:]

        alf_dict = alf_dict[:-2]
        alf_dict.append((min_p[0] + before_min_p[0], min_p[1] + before_min_p[1]))

    alf_res = sorted(alf.items(), key=lambda item: item[1][1], reverse=True)
    return alf_res

def int_to_bin(i, length=0):
    binary_str = bin(i)[2:]
    if length:
        return '0' * (length - len(binary_str)) + binary_str
    else:
        return binary_str

def clygeb(alf):
    max_len = 0
    for el in alf:
        max_len = max(max_len, len(el[1][2]))
    ascii_code = []
    clygeb_cod = '0'
    already_used=[]
    kode=0
    counter = 1
    for i in range(1, max_len + 2):
        for j in range(2**i):
            cod=int_to_bin(j,i)
            find=0
            for el in alf:
                if cod==el[1][2]:
                    already_used.append(el[1][2])
                    clygeb_cod+='1'
                    print (counter, el[0], el[1][1], el[1][2])
                    counter += 1
                    k = el[0].encode("cp1251")
                    kode = (ord(k))
                    kode = int_to_bin(kode, 8)
                    ascii_code.append(kode)
                    find=1
            if not(cod.startswith(tuple(already_used))) and not(find):
                clygeb_cod+='0'
    return clygeb_cod, ascii_code
# text = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
def process_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        str_file = file.read().replace("\n", "")
        length = len(str_file)
    return str_file

str_file = process_file("main.txt")
one_let = count_letters(1, str_file)
one_let = Code_Huffman(one_let)
clygeb_info = clygeb(one_let)
print('C1=' + clygeb_info[0] + '', end='')
l1 = 0
for cod in clygeb_info[1]:
    print(cod, end=' ')
    l1 += len((cod))
l1 += len(clygeb_info[0])
print('\nL1 =', l1 - 33)
binary = ""
for let in str_file:
    for el in one_let:
        if el[0] == let:
            cod_let = el[1][2]
            break
    binary += cod_let
print()
print('C2 = ' + binary)

l2 = len(binary)
print('L2 = ' + str(l2))
print()
print('C3 = ' + binary + clygeb_info[0]+ ', ', end='')
for cod in clygeb_info[1]:
    print(int_to_bin(int(cod)), end='')
print('\nL3 =', l1+l2)

# w = "0000000000000011011010011011010000100110111111100010011111111111100100000 11110000 11100101 11101010 11110010 11100000 11110011 11101000 11101110 11100010 11101011 11111000 11101100 11101101 11101111 00100111 11100011 11111111 11110110 11100111 00101110 11110001 11110101 11110111 11010010 11010011 11100100 11111011 11110100 11010111 00100001 00101101 11111100"
# print(len(w), len(w)- w.count("0"))