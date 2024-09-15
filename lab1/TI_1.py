import math

text = "Там королевич мимоходом пленяет грозного царя.У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
length = len(text)

slov_1 = {}

for i in range(length):
    if text[i] not in slov_1:
        slov_1[text[i]] = 1
    else:
        slov_1[text[i]] += 1

# print(slov_1)
print()

cntr = 1
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)')
for char, count in slov_1.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length:<3} | {count/length:.6f}")
    cntr += 1



print("\n-----------------------------------------\n")


slov_2 = {}
for i in range(length-1):
    pair = text[i:i+2]
    if pair not in slov_2:
        slov_2[pair] = 1
    else:
        slov_2[pair] += 1

length_1 = length - 1
cntr = 1
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)')
for char, count in slov_2.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_1:<3} | {count/length_1:.6f}")
    cntr += 1

print("\n-----------------------------------------\n")

slov_3 = {}

for i in range(length-2):
    trio = text[i:i+3]
    if trio not in slov_3:
        slov_3[trio] = 1
    else:
        slov_3[trio] += 1

length_2 = length - 2
cntr = 1
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)')
for char, count in slov_3.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_2:<3} | {count/length_2:.6f}")
    cntr += 1

print("\n-----------------------------------------\n")
