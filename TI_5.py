'''

Лабораторная работа №5
Код Гиблерта-Мура

Вероятность упорядочивать не нужно
Алгоритм:
1) куммулятивные вероятности
2) Вспомогательные вероятности - сдвигаем величину на pi/2
3) считаем длины кодовых слов

меньшая длина сжатия или быстрая смена источника
Л должна быть 5.8

'''

import math
import struct

text = "Там королевич мимоходом пленяет грозного царя.У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
length = len(text)

slov_1 = {}

for i in range(length):
    if text[i] not in slov_1:
        slov_1[text[i]] = 1
    else:
        slov_1[text[i]] += 1

print()

cntr = 1
mas1 = []

avr_len = []
total_l = 0
print('i   | Xi |  p(Xi)   |    qi      |     sigma     | li  | кодовое слово')

cnt = 0
communicative_freq = []
sigma = 0
for char, count in slov_1.items():



    freq = count / length
    sigma = cnt + freq / 2
    li = math.ceil(-math.log(freq, 2) + 1)


    s = struct.pack('!f', sigma)
    b = ''.join(format(c, '08b') for c in s)

    print(f"{cntr:<3} | {char:<3}"
          f"| {freq:.6f} | {cnt:4.8f} |"
          f" {sigma:.10f}  | {li}  | {b[-(li):]}")
    communicative_freq.append(cnt)
    cnt += freq

    a_lenth = freq * li
    total_l += a_lenth
    mas1.append(-math.log2(count / length) * count / length)
    cntr += 1

summ_1 = sum(mas1)

# print("L:   " + str(sum(avr_len)/len(avr_len)))
print("L = " + str(total_l))

R = total_l / 1
print("R = " + str(R))
print("r = " + str(abs(R - summ_1)))



print("\n-----------------------------------------\n")


slov_2 = {}
sigma = 0
for i in range(length-1):
    pair = text[i:i+2]
    if pair not in slov_2:
        slov_2[pair] = 1
    else:
        slov_2[pair] += 1

length_1 = length
cntr = 1
mas2 = []
avr_len1 = []
total_l1 = 0

cnt = 0
communicative_freq = []
print('i   | Xi |  p(Xi)   |    qi      |     sigma     | li  | кодовое слово')
for char, count in slov_2.items():
    freq = count / length_1
    sigma = cnt + freq / 2
    li = math.ceil(-math.log(freq, 2) + 1)

    s = struct.pack('!f', sigma)
    b = ''.join(format(c, '08b') for c in s)
    print(f"{cntr:<3} | {char:<3}"
          f"| {freq:.6f} | {cnt:4.8f} |"
          f" {sigma:.10f}  | {li} | {b[-(li):]}")
    communicative_freq.append(cnt)
    cnt += freq

    a_lenth1 = freq * li
    total_l1 += a_lenth1
    mas2.append(-math.log2(count / length_1) * count / length_1)
    cntr += 1



summ_2 = sum(mas2)


# print("L:   " + str(sum(avr_len)/len(avr_len)))
print("L =  " + str(total_l1))

R1 = total_l1 / 2
print("R =  " + str(R1))
print("r =  " + str(abs(R1 - summ_2/2)))

print("\n-----------------------------------------\n")


slov_3 = {}
sigma = 0
for i in range(length-2):
    trio = text[i:i+3]
    if trio not in slov_3:
        slov_3[trio] = 1
    else:
        slov_3[trio] += 1

length_2 = length
cntr = 1
mas3 = []
avr_len2 = []
total_l2 = 0

cnt = 0
communicative_freq = []
print('i   | Xi |  p(Xi)   |    qi      |     sigma     | li  | кодовое слово')
for char, count in slov_3.items():
    freq = count / length_2
    sigma = cnt + freq / 2
    li = math.ceil(-math.log(freq, 2) + 1)

    s = struct.pack('!f', sigma)
    b = ''.join(format(c, '08b') for c in s)
    print(f"{cntr:<3} | {char:<3}"
          f"| {freq:.6f} | {cnt:4.8f} | {li} | {b[-(li):]}")
    communicative_freq.append(cnt)
    cnt += freq

    a_lenth2 = freq * li
    total_l2 += a_lenth2
    mas3.append(-math.log2(count / length_2) * count / length_2)
    cntr += 1
summ_3 = sum(mas3)

print("L =  " + str(total_l2))

R1 = total_l2 / 3
print("R =  " + str(R1))
print("r =  " + str(abs(R1 - summ_3/3)))


print("\n-----------------------------------------\n")