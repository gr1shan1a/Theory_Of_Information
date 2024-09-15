import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(node, current_code="", huffman_codes={}):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = {'frequency': node.freq, 'huffman_code': current_code, 'code_length': len(current_code)}
        return

    generate_huffman_codes(node.left, current_code + "0", huffman_codes)
    generate_huffman_codes(node.right, current_code + "1", huffman_codes)

def generate_character_dictionary(text):
    huffman_tree = build_huffman_tree(text)
    huffman_codes = {}
    generate_huffman_codes(huffman_tree, "", huffman_codes)
    character_dict = defaultdict(dict)
    num = 1
    for char, info in huffman_codes.items():
        character_dict[char] = {
            'probability': text.count(char) / len(text),
            'number': num,
            'frequency': info['frequency'],
            'huffman_code': info['huffman_code'],
            'code_length': info['code_length']
        }
        num += 1

    return character_dict

def duty_information(char_dict):
    max_len = 0
    for char in char_dict:
        max_len = max(max_len, char_dict[char]['code_length'])
    ascii_code = []
    duty_code = '0'
    already_used=[]
    for i in range(1, max_len + 2):
        for j in range(2**i):
            cod=int_to_bin(j,i)
            find = 0
            for char in char_dict:
                if cod==char_dict[char]['huffman_code']:
                    already_used.append(char_dict[char]['huffman_code'])
                    duty_code += '1'
                    shifr = char.encode("cp1251")
                    shifr = ord(shifr)
                    shifr = int_to_bin(shifr, 8)
                    ascii_code.append(shifr)
                    find = 1
            if not(cod.startswith(tuple(already_used))) and not(find):
                duty_code += '0'
    return duty_code, ascii_code

def int_to_bin(i, lenght=0):
    cod=''
    while i > 0:
        cod=str(i%2)+cod
        i //= 2
    if lenght:
        return '0' * (lenght-len(cod)) + cod
    else:
        return cod


text = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
char_dict = generate_character_dictionary(text)
duty_code, ascii_code = duty_information(char_dict)

fullcode = ""
for char in text:
        if char in char_dict:
            fullcode += char_dict[char]['huffman_code']

print(f"№\tSym\tCnt\t Cod \t\tLen")
print("----------------------------------------------")
# fullcode = ""
for char, info in char_dict.items():
    print(f"{info['number']}\t{char}\t{info['frequency']}\t {info['huffman_code']:<10}\t{info['code_length']}")


ascii_code1 = ""
for item in ascii_code:
    ascii_code1 += " "
    ascii_code1 += item

ascii_code_binary = ''.join([bin(int(code))[2:].zfill(8) for code in ascii_code])

l = duty_code + ascii_code1


print("\nC1(x) = " + duty_code + str(ascii_code1))
print("L1 = " + str(len(l) - l.count(' ')))
print("\nC2(x) = " + fullcode)
print("L2 = " + str(len(fullcode)))
print("\nC(x) = " + duty_code + str(ascii_code1) + fullcode)
print("L = " + str(len(duty_code + str(ascii_code1) + fullcode) - l.count(' ')))

# l = "000000000000001011011001101101101000011010110001101111111111111 00100000 11101101 11100000 11100101 11110010 11101010 11110011 11101000 11101110 11110101 11100010 11101011 11101100 11111000 11110000 00101110 11101111 11110110 11100111 11100011 11111111 11110001 11010011 11111011 11110100 00101101 11010010 11010111 11111100 11100100 00100001 11110111"
# print(len(l) - l.count(' '))