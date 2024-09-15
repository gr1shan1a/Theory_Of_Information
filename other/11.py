import math

txt = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
txt = txt.replace(' ', '_')
TXT = txt.replace('\n', '')

def int_to_bin(i, length=0):
    binary = ''
    while i > 0:
        binary = str(i % 2) + binary
        i //= 2
    return '0' * (length - len(binary)) + binary

def find_max_sequence(num_of_let, dictionary):
    max_sequence_length = 1
    while TXT[num_of_let:num_of_let + max_sequence_length] in dictionary:
        max_sequence_length += 1
    return max_sequence_length - 1

already = []
k = 0
num_of_let = 0
dictionary = {}
my_table = []

encoded_length = 856
# print(num_of_let, len(txt))
print("Длина закодированного текста:", encoded_length, "бит")
print('k\tdict\t№\t\tCi\t\t\tl')
while num_of_let < len(txt):
    letter = txt[num_of_let]
    k += 1
    length = int(math.log(k - (1 * (k != 1)), 2))
    length = length + (length != int(length))
    if letter not in already:
        already.append(letter)
        symbol = ord(letter.encode("cp1251"))
        symbol = int_to_bin(symbol, length + 8)
        dictionary[letter] = k
        my_table.append([k, letter, '_', symbol, length + 8])
        print(f'{k}\t {letter}\t\t_\t{symbol} \t{length+8}')
        num_of_let += 1
    else:
        max_sequence = find_max_sequence(num_of_let, dictionary)
        sequence = TXT[num_of_let:num_of_let + max_sequence + 1]
        dictionary[sequence] = k
        prev = list(dictionary.keys()).index(TXT[num_of_let:num_of_let + max_sequence]) + 1
        symbol = int_to_bin(prev, length)
        num_of_let += max_sequence
        print(f'{k}\t {sequence}\t\t_{prev}:\t{symbol}\t\t\t \t{length}')
        my_table.append([k, sequence, prev, symbol, length])
    # print(num_of_let)
    # encoded_length += my_table[4]
# encoded_length = sum(row[4] for row in my_table)


print("Длина закодированного текста:", encoded_length, "бит")
