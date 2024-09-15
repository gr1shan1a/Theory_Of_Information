# from prettytable import PrettyTable
import math
txt = 'Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут.'
txt = txt.replace(' ', '_')
txt = txt.replace('\n', '')

def int_to_bin(i, lenght=0):
    cod=''
    while i>0:
        cod=str(i%2)+cod
        i//=2
    return '0'*(lenght-len(cod))+cod
def mov(i):
    bi=int_to_bin(i)
    bin_with_hatch=bi[1:]
    unar='1'*(len(bin_with_hatch)-1)+'0'
    return unar+bin_with_hatch
def find_max_posled(num_of_let, txt):
    let=txt[num_of_let]
    txt_before=txt[:num_of_let]
    flag=1
    len_posled=1
    while(flag) and (num_of_let+len_posled<=len(txt)):
        if txt[num_of_let:num_of_let+len_posled] in txt_before:
            len_posled += 1
            continue
        else:
            len_posled-=1
            flag=0
    if num_of_let + len_posled > len(txt):
        len_posled -= 1
    return txt_before.rfind(txt[num_of_let:num_of_let+len_posled]),len_posled

already=[]
num_of_let=0
i=1
l = 0
print('i','flag','Xi', 'd(w)', 'e','Ci', 'li')
while num_of_let+1<=len(txt):
    let= txt[num_of_let]
    if let not in already:
        already.append(let)
        symbol = (ord(let.encode("cp1251")))
        symbol=int_to_bin(symbol,8)
        print([i,0,let,'_',0,'0'+symbol, 9])
        num_of_let += 1
        l += 9
    else:
        num_prev, len_of_posled = find_max_posled(num_of_let,txt)
        Xi=txt[num_of_let:num_of_let+len_of_posled]
        d=num_of_let-num_prev-1
        w = (math.log(num_of_let, 2))
        w=int(w+(w!=int(w)))
        cod='1 '+int_to_bin(d,w)+' '+mov(len_of_posled)
        print([i, 1, Xi, f'{d}({num_of_let})', len_of_posled, cod, len(cod)-2])
        num_of_let += len_of_posled
        l += len(cod) -2
    i += 1

print('длина кода:', l)