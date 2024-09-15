#from prettytable import PrettyTable


'''
        Лабораторная работа №8
        Двухпроходное кодирование с регулярным кодом Хаффмена
    c(x) = (c1(x), c2(x))
    регулярный код - более короткие слова лексикографически(в словаре) предшествуют более длинным
    а < .. < б
    0 < 1
    0...< 1...
    110.. < 111..

    per_aspera_ad_astra

    короткие ветви - вверху, длинные внизу

    знаем все длины кодовых слов

    регулярный код

    i: 1 - n
    длина кода: 2, 2 ,2 3, 3, 3, 4, 4, 4,

    на каждом ярусе символы в дереве расположены в алфавитном порядке(дерево строится однозначно)

    i  |  символ  | длина кода |
            a, e ,p r(3), ., d, s, t(4)

        1) таблица информации №1
        2) таблица подсчета затрат на служ инфу
        3) дерево
        4) посчитать длину
        5) посчитать длину x2
'''

import math
from functools import lru_cache
txt = 'Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут.'
txt = txt.replace(' ', '_')
txt = txt.replace('\n', '')

def count_letters(num_of_let, text):
    alf_letters = {}
    for i in range(len(text) - num_of_let + 1):
        let = text[i:i + num_of_let]
        alf_letters.setdefault(let, [0] * 4)
        alf_letters[let][0] += 1
        alf_letters[let][1] = (alf_letters[let][0] / (len(text) - num_of_let + 1))
        alf_letters[let][2] = 0
        alf_letters[let][3] = ''
    return alf_letters
    
def Print_Haff(alf):
    #my_table = PrettyTable()
    i=0
    #my_table.field_names = ['i', 'символ', 'Pi', '№ яруса', 'Ci']
    alf= sorted(alf, key=lambda item: item[1][2])
    for el in alf:
        i+=1
        #my_table.add_row([i, el[0],el[1][1], el[1][2], el[1][3]])
        print([i, el[0],el[1][1], el[1][2], el[1][3]])
    #print('1)')
    #print(my_table)
    
def code_huff(alf):
    num_of_let = len(list(alf.keys())[0])
    alf_dict = []
    for k, v in alf.items():
        alf_dict.append((k, v[1]))
    max_len=0
    while len(alf_dict) > 1:
        alf_dict = sorted(alf_dict, key=lambda item: item[1], reverse=True)
        min_p = alf_dict[-1]
        symbols = min_p[0]
        while len(symbols) > 0:
            letter = symbols[:num_of_let]
            alf[letter][2]+=1
            if alf[letter][2]>max_len:
                max_len=alf[letter][2]
            symbols = symbols[num_of_let:]
        before_min_p = alf_dict[-2]
        symbols = before_min_p[0]
        while len(symbols) > 0:
            letter = symbols[:num_of_let]
            alf[letter][2] +=1
            if alf[letter][2]>max_len:
                max_len=alf[letter][2]
            symbols = symbols[num_of_let:]
        alf_dict = alf_dict[:-2]
        alf_dict=[(min_p[0] + before_min_p[0], min_p[1] + before_min_p[1])]+alf_dict
    alf_res = sorted(alf.items(), key=lambda item: item[0])
    already_used=[]
    for i in range(1,max_len+1):
        for j in range (2**i):
            cod=int_to_bin(j, lenght=i)
            for el in alf_res:
                if (el[1][2]==i) and (el[1][3]=='') and not(cod.startswith(tuple(already_used))):
                    el[1][3]=cod
                    already_used.append(cod)
                    break
    return alf_res

@lru_cache(None)
def C(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return C(n-1, k) + C(n-1, k-1)
    else:
        return n
        
def int_to_bin(i, lenght=0):
    cod=''
    while i>0:
        cod=str(i%2)+cod
        i//=2
    if lenght:
        return '0'*(lenght-len(cod))+cod
    else:
        return cod

def sluzh_info(alf):
    max_len=0
    for el in alf:
        max_len = max(max_len, len(el[1][3]))
    table={}
    count_vertexes=1
    num_of_let=256
    sh_tree=''
    l1=0
    for i in range(max_len+1):
        table[i]=[count_vertexes]
        count_leaves=0
        for el in alf:
            if el[1][2]==i:
                count_leaves+=1
        table[i].append(count_leaves)
        table[i].append(f'0...{count_vertexes}')
        bits = round((math.log(count_vertexes+1, 2)), 4)
        bits=int(bits+1*(bits%1!=0))
        table[i].append(bits)
        c=C(num_of_let, count_leaves)
        combine = round((math.log(c, 2)), 4)
        combine = int(combine+1*(combine%1!=0))
        table[i].append(combine)
        sh_tree+=int_to_bin(count_leaves, bits)
        l1+=bits+combine
        num_of_let-=count_leaves
        count_vertexes=(count_vertexes-count_leaves)*2
    print()
    for k, v in table.items():
        print(k, ':', v)
    print(sh_tree)
    return l1

alf = count_letters(1, txt)
alf = code_huff(alf)
Print_Haff(alf)
l1 = sluzh_info(alf)
l=0
for let in txt:
    for el in alf:
        symb=el[0]
        if symb==let:
            l+=len(el[1][3])
print (l1)
print(l+l1)