'''
отчет по первому блоку лабораторных работ 1-6
кодирование источника с известной статистикой
цель i-ой лаб  + результаты

Вывод - эффективность алгоритмов(скорость, избыточность) -> какой самый эффективный и какой наименее
2) как зависит скорость кодирования от длины кодируемого блока символов - 2 недели
'''

import math

txt = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
txt = txt.replace(' ', '_')


def count_letter(num_of_let, txt):
    alf_letters = {}
    for i in range(len(txt) - num_of_let + 1):
        let = txt[i:i + num_of_let]
        alf_letters.setdefault(let, [0] * 2)
        alf_letters[let][0] += 1
        alf_letters[let][1] = (round(alf_letters[let][0] / (len(txt) - num_of_let + 1), 4))
    return alf_letters


def count_q(alf):
    q = 0
    for k, v in alf.items():
        q += v[1] / 2
        v.append(q)
        q += v[1] / 2


def float_to_bin(p, lenght):
    cod = ''
    for _ in range(lenght):
        p *= 2
        cod += str(int(p))
        p %= 1
    return cod


def arifm_code(n, alf, txt):
    k = int(len(txt) / 6)
    avg_len = 0
    avg_r = 0
    Algos_code = ''
    for i in range(k):
        curr_txt = txt[:6]
        g = 1
        f = 0
        curr_block = curr_txt
        for i in range(int(6 / n)):
            curr_symb = curr_block[:n]
            f += alf[curr_symb][2] * g
            g *= alf[curr_symb][1]
            curr_block = curr_block[n:]
        len_code = int(-(math.log(g, 2))) + 1 + 1 * (-(math.log(g, 2)) != 0)
        cod = float_to_bin(f + g / 2, len_code)
        Algos_code += cod
        curr_len = len(cod) / (6 / n)
        avg_len += curr_len
        avg_r += curr_len / n
        txt = txt[6:]
    avg_len /= k
    avg_r /= k
    return avg_r, avg_len, Algos_code


i = 1
alf = count_letter(i, txt)
count_q(alf)
avg_r, avg_len, Algos_code = arifm_code(i, alf, txt)

print("i = 1")
print("_____________________________")
print(f"{Algos_code}\nL = {avg_len}\nR = {avg_r}\n")

i = 2
alf = count_letter(i, txt)
count_q(alf)
avg_r, avg_len, Algos_code = arifm_code(i, alf, txt)
print("i = 2")
print("_____________________________")
print(f"{Algos_code}\nL = {avg_len}\nR = {avg_r}\n")

i = 3
alf = count_letter(i, txt)
count_q(alf)
avg_r, avg_len, Algos_code = arifm_code(i, alf, txt)
print("i = 3")
print("_____________________________")
print(f"{Algos_code}\nL = {avg_len}\nR = {avg_r}\n")
