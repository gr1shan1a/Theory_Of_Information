txt = '''Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут.'''
txt = txt.replace(' ', '_')
txt = txt.replace('\n', '')
number_of_book = {}
letters=[]

def int_to_bin(i, lenght=0):
    cod=''
    while i>0:
        cod=str(i%2)+cod
        i//=2
    return '0'*(lenght-len(cod))+cod
def mov(i):
    bi=int_to_bin(i)
    bin_with_hatch=bi[1:]
    unar='1'*(len(bin_with_hatch))+'0'
    return unar+bin_with_hatch
for let in txt:
    k = let.encode("cp1251")
    symbol = (ord(k))
    number_of_book[let]=symbol
    letters.append([let, symbol]+[0]*3)
number_of_book = sorted(number_of_book.items(), key=lambda item: item[1])
numb_books={}
for el in number_of_book:
    numb_books[el[0]]=el[1]
print ("ASCII, Interval,      bin,       length")
cnt = 1
s = ''
for let in letters:
    number_of_book = sorted(numb_books.items(), key=lambda item: item[1])
    numb_books = {}

    for el in number_of_book:
        numb_books[el[0]] = el[1]
    for k in numb_books.keys():
        if k==let[0]:
            break
        numb_books[k]+=1
    let[2]=numb_books[let[0]]
    numb_books[let[0]]=0
    let[3]=mov(let[2])
    let[4]=len(let[3])
    s += str(let[3])
    print(let)
print(s)
print("Длина закодированного текста: ", sum(let[4] for let in letters))

