'''

                Лабораторная работа №4. Код Шеннона
X = {x1, x2, x3,  , p(x1). p(xn)}
1) сортировка вероятностей по невозрастанию p(x1) >= p(x2) >= p(x3) ...
2) коммулятивные вероятности: q1 = 0; q2 = p(xi), q3 = p(xi1) + p(xi2) +..
                              qn = p(x1)
3) для нового слова для Xij : lj = [-log2(pxj)] - округл вверх(целая часть)
4) новое слово cj для xij : первые lj символов после "," в двоичном разложении qj

пример
X = {a, b, c, d; p(a) = 0.25, p(b) = 0.5, p(c) = 0.125, p(d) = 0.125}
1) 0.5 >= 0.25 >= 0.125 >= 0.125 -> bacd
2) q1 = 0, q2 = 0.5, q3 = 0.75, q4 =
3) l1 = -log2(0.5) = 1; l2 = -log2(0.25) = 2; l3 = -log2(0.125) = 3
4) q1 = 0 => c1 = 0; q2 = 0.5 => c2 = 0.5 * 2 = [1],0  => [10] = c2
                                      0,0 * 2 = [0],0
  q3 = 0.75 => 0,75 * 2 = [1],5 =>  c3 = 110
               0.5 * 2 = [1],0
               0,0 * 2 = [0],0
    qn = 0,875 => 0,875 * 2 = [1],75 => c4 = 111
                  0,75 * 2 = [1],5
                  0,5 * 2 = [1],0
средняя длина кода
скорость
избыточность
'''

import math

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
print('i   | Xi |  p(Xi)   |    qi      | li  | code')
new_dic = sorted(slov_1.items(), key=lambda x: x[1], reverse=True)
sorted_dic = dict(new_dic)
q = 0
codes = {}
for char, count in sorted_dic.items():

    freq = count / length
    li = math.ceil(-math.log(freq, 2))

    q += freq
    q_int = int(math.floor((q - freq) * 2**li))

    code = bin(q_int)[2:].zfill(li)
    # print("xuy: ", code, end="")
    codes[char] = code

    a_lenth = freq * li
    total_l += a_lenth
    mas1.append(-math.log2(count / length) * count / length)

    print(f"{cntr:<3} | {char:<3}"
          f"| {freq:.6f} | {q:.4f} | {li} | {code}")
    cntr += 1

summ_1 = sum(mas1)

print("L = " + str(total_l))

R = total_l / 1
print("R = " + str(R))
print("r = " + str(R - summ_1))


# l=4.539
# R=4.539


print("\n-----------------------------------------\n")

slov_2 = {}

for i in range(length - 1):
    pair = text[i:i+2]
    if pair not in slov_2:
        slov_2[pair] = 1
    else:
        slov_2[pair] += 1

print()

cntr = 1
mas2 = []

avr_len = []
total_l = 0
print('i   | Xi |  p(Xi)   |    qi      | li  | code')
new_dic = sorted(slov_2.items(), key=lambda x: x[1], reverse=True)
sorted_dic = dict(new_dic)
q = 0
codes = {}
for pair, count in sorted_dic.items():
    freq = count / (length - 1)
    li = math.ceil(-math.log(freq, 2))

    q += freq
    q_int = int(math.floor((q - freq) * 2**li))
    code = bin(q_int)[2:].zfill(li)
    codes[pair] = code

    a_lenth = freq * li
    total_l += a_lenth
    mas2.append(-math.log2(count / (length - 1)) * count / (length - 1))
    cntr += 1
    print(f"{cntr:<3} | {pair:<5}"
          f"| {freq:.6f} | {q:.4f} | {li} | {code}")

summ_2 = sum(mas2)

print("L = " + str(total_l))

R = total_l / 2
print("R = " + str(R))
print("r = " + str(R - summ_2/2))
# l=6.486
# R=3.243
#
print("\n-----------------------------------------\n")



slov_3 = {}

for i in range(length - 2):
    triplet = text[i:i+3]
    if triplet not in slov_3:
        slov_3[triplet] = 1
    else:
        slov_3[triplet] += 1

print()

cntr = 1
mas3 = []

avr_len = []
total_l = 0
print('i   | Xi |  p(Xi)   |    qi      | li  | code')
new_dic = sorted(slov_3.items(), key=lambda x: x[1], reverse=True)
sorted_dic = dict(new_dic)
q = 0
codes = {}
for triplet, count in sorted_dic.items():

    freq = count / (length - 2)
    li = math.ceil(-math.log(freq, 2))

    q += freq
    q_int = int(math.floor((q - freq) * 2**li))
    code = bin(q_int)[2:].zfill(li)
    codes[triplet] = code

    a_lenth = freq * li
    total_l += a_lenth
    mas3.append(-math.log2(count / (length - 2)) * count / (length - 2))
    cntr += 1
    print(f"{cntr:<3} | {triplet:<8}"
          f"| {freq:.6f} | {q:.4f} | {li} | {code}")

summ_3 = sum(mas3)
print("L = " + str(total_l))

R = total_l / 3
print("R = " + str(R))
print("r = " + str(R - summ_3/3))