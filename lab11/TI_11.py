# from prettytable import PrettyTable
import math
txt ='''Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут.'''
txt=txt.replace(' ', '_')
TXT=txt.replace('\n', '')

def int_to_bin(i, lenght=0):
	cod=''
	while i>0:
		cod=str(i%2)+cod
		i//=2
	return '0'*(lenght-len(cod))+cod
def find_max_posled(num_of_let, dict):
	len_posled=1
	while TXT[num_of_let:num_of_let+len_posled] in list(dict.keys()):
			len_posled+=1
	return len_posled-1
	
already=[]
k=0
num_of_let=0
l=0
dict={}
# my_table = PrettyTable()
my_table = []
print('k  ', 'dict ', '#', '\tCi\t\t', 'l')
#print('k\tdict\t№\t\tCi\tl')
while num_of_let<len(txt):
	let=txt[num_of_let]
	k+=1
	lenght = (math.log(k - (1 * (k != 1)), 2))
	lenght = int(lenght + (lenght != int(lenght)))
	if let not in already:
		already.append(let)
		symbol = (ord(let.encode("cp1251")))
		symbol=int_to_bin(symbol,lenght+8)
		dict[let]=k
		my_table.append([k, let, '_', symbol, lenght+8])
		print(f'{k}\t{let}\t_\t{symbol} {lenght+8}')
		num_of_let+=1
	else:
		len_posled=find_max_posled(num_of_let, dict)
		let=TXT[num_of_let:num_of_let+len_posled+1]
		dict[let]=k
		prev=list(dict.keys()).index(TXT[num_of_let:num_of_let+len_posled])+1
		symbol=int_to_bin(prev, lenght)
		num_of_let+=len_posled
		print(f'{k}\t{let}\t_{prev}\t{symbol} {lenght + 8}')
		my_table.append([k,let,prev,symbol,lenght])

summ = 0
for i in range(len(my_table)):
	summ += int(my_table[i][4])
	print(my_table[i])

print(summ)