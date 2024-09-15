import math

text = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
length = len(text)

def build_huffman_tree(symbols_probabilities):
    nodes = [(symbol, probability) for symbol, probability in symbols_probabilities.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x[1])
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = (None, left[1] + right[1], left, right)
        nodes.append(merged)
    return nodes[0]

def huffman_codes(root, current_code="", codes={}):
    if root[0] is not None:
        codes[root[0]] = current_code
    else:
        huffman_codes(root[2], current_code + "0", codes)
        huffman_codes(root[3], current_code + "1", codes)
    return codes

slov_1 = {}

for i in range(length):
    if text[i] not in slov_1:
        slov_1[text[i]] = 1
    else:
        slov_1[text[i]] += 1

print()

cntr = 1
mas1 = []
huffman_tree = build_huffman_tree(slov_1)
huffman_codes_dict = huffman_codes(huffman_tree)
avr_len = []
total_l = 0
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)   |  I(xi)   | p(xi) * I(xi)     |    code   |  length')
for char, count in slov_1.items():
    freq = count/length
    code_length = len(huffman_codes_dict[char])

    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length:<3} "
          f"| {freq:.6f} | {-math.log2(count/length):.6f} | "
          f" {(-math.log2(count/length) * count/length):.8f}       |  {(huffman_codes_dict[char]):8}"
          f" |   {code_length}")
    a_lenth = freq * code_length
    total_l += a_lenth
    mas1.append(-math.log2(count/length) * count/length)
    avr_len.append(len(huffman_codes_dict[char]))
    cntr += 1

print('H(Xˆ1)  | H(Xˆ1)/n | H(X|Xˆ0)')
summ_1 = sum(mas1)
print(f"{summ_1} | {summ_1} | {summ_1}")

# print("L:   " + str(sum(avr_len)/len(avr_len)))
print("L = " + str(total_l))

R = total_l / 1
print("R = " + str(R))
print("r = " + str(R - summ_1))
# l=6.617
# R=3.309



print("\n-----------------------------------------\n")


slov_2 = {}
for i in range(length-1):
    pair = text[i:i+2]
    if pair not in slov_2:
        slov_2[pair] = 1
    else:
        slov_2[pair] += 1

length_1 = length
cntr = 1
mas2 = []
huffman_tree1 = build_huffman_tree(slov_2)
huffman_codes_dict1 = huffman_codes(huffman_tree1)
avr_len1 = []
total_l1 = 0
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)   |  I(xi)   | p(xi) * I(xi)     |   code   |  length')
for char, count in slov_2.items():
    freq = count / length
    code_length = len(huffman_codes_dict1[char])
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_1:<3}"
          f" | {count/length_1:.6f} | {-math.log2(count/length_1):.6f} "
          f"| {(-math.log2(count/length_1) * count/length_1):.8f}        |"
          f" {(huffman_codes_dict1[char]):8}"
          f" |   {code_length}")
    a_lenth1 = freq * code_length
    total_l1 += a_lenth1
    mas2.append(-math.log2(count / length_1) * count / length_1)
    cntr += 1



summ_2 = sum(mas2)
print('H(Xˆ2)  | H(Xˆ2)/n | H(X|Xˆ1)')
print(f"{summ_2} | {summ_2/2} | {summ_2 - summ_1}")

# print("L:   " + str(sum(avr_len)/len(avr_len)))
print("L =  " + str(total_l1))

R1 = total_l1 / 2
print("R =  " + str(R1))
print("r =  " + str(R1 - summ_2/2))
# l=6.617
# R=3.309

print("\n-----------------------------------------\n")


slov_3 = {}

for i in range(length-2):
    trio = text[i:i+3]
    if trio not in slov_3:
        slov_3[trio] = 1
    else:
        slov_3[trio] += 1

length_2 = length
cntr = 1
mas3 = []
huffman_tree2 = build_huffman_tree(slov_3)
huffman_codes_dict2 = huffman_codes(huffman_tree2)
avr_len2 = []
total_l2 = 0
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)   |  I(xi)   | p(xi) * I(xi)     |    code    |  length')
for char, count in slov_3.items():
    freq = count / length
    code_length = len(huffman_codes_dict2[char])
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_2:<3} | {count/length_2:.6f}  "
          f"| {-math.log2(count/length_2):.6f} | {(-math.log2(count/length_2) * count/length_2):.8f}"
          f"       |  {(huffman_codes_dict2[char]):10}| {code_length:4}")
    a_lenth2 = freq * code_length
    total_l2 += a_lenth2
    mas3.append(-math.log2(count / length_2) * count / length_2)
    cntr += 1
summ_3 = sum(mas3)
print('H(Xˆ3)  | H(Xˆ3)/n | H(X|Xˆ2)')
print(f"{summ_3} | {summ_3/3} | {summ_3 - summ_2}")

print("L =  " + str(total_l2))

R1 = total_l2 / 3
print("R =  " + str(R1))
print("r =  " + str(R1 - summ_3/3))
# l=7.000
# R=3.500


print("\n-----------------------------------------\n")

