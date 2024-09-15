'''

                ЛАБОРАТОРНАЯ №2

стационарные источники X = {x, p(x)} - дисперстный ансамбль

информационное характеристики источника
H(x) - энтропия источника = - sum(p(x) * log2(p(x)) - среднее колво информации, кот несет в сеье сообщение

Пример1 X = {{a, b}, p[a] = 1. p[b] = 0} => H = 0
Пример2 X = {{a, b}, p[a] = p[b] = 1/2} => -1/2*(-1) - 1/2*(-1) = 1

    2 подхода к иззмерению информации, пораждаемой дискретным источником
    1) рассм сиволы, орг в блоки длины n
        H(Xˆn) = -sum(x1 iz X|sum(x2 iz X|) p(x1, x2,..., xn)*log2(p(x1,x2,..,xn)
        - n-мерная энтропия источника = avr колво Inf в блоки длины n

        Энтропия на символ последовательности: длина n
        H(Xˆn)/n = H[n](X)

    2) когда декодер получает n-ый символ, первые (n-1) символов ему уже известны
    Источник-стационарный => важно знать лишь длину уде переданной посл: n-1
    H(Xn(X1X2...Xn) = H(X|Xˆn-1) <- условие энтропии
    H(X/Y) = - sum(x iz X)sum(y iz Y)p(x, y)log2(p(x/y)     x = xˆ1
    h = 1,2,3

            H(Xˆn)      H(X/X0) = H(X)
            Hn(X)       H(X/Xˆ1) = H(Xˆ2) - H(Xˆ1)
            H(X/Xˆn-1)


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

# print(slov_1)
print()

cntr = 1
mas1 = []
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)   |  I(xi)   | p(xi) * I(xi)')
for char, count in slov_1.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length:<3} | {count/length:.6f} | {-math.log2(count/length):.6f} | {-math.log2(count/length) * count/length}")
    mas1.append(-math.log2(count/length) * count/length)
    cntr += 1
print('H(Xˆ1)  | H(Xˆ1)/n | H(X|Xˆ0)')
summ_1 = sum(mas1)
print(f"{summ_1} | {summ_1} | {summ_1}")



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
mas2 = []
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)   |  I(xi)   | p(xi) * I(xi)')
for char, count in slov_2.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_1:<3} | {count/length_1:.6f} | {-math.log2(count/length_1):.6f} | {-math.log2(count/length_1) * count/length_1}")
    mas2.append(-math.log2(count / length_1) * count / length_1)
    cntr += 1
summ_2 = sum(mas2)
print()
print(f"{summ_2} | {summ_2/2} | {summ_2 - summ_1}")

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
mas3 = []
print('i   | Xi  | Ni  |  Ni/N  |  p(Xi)    |  I(xi)   | p(xi) * I(xi)')
for char, count in slov_3.items():
    print(f"{cntr:<3} | {char:<3} | {count:<3} | {count:<2}/{length_2:<3} | {count/length_2:.6f}  | {-math.log2(count/length_2):.6f} | {-math.log2(count/length_2) * count/length_2}")
    mas3.append(-math.log2(count / length_2) * count / length_2)
    cntr += 1
summ_3 = sum(mas3)
print()
print(f"{summ_3} | {summ_3/3} | {summ_3 - summ_2}")


print("\n-----------------------------------------\n")

