import math
s = "Там королевич мимоходом пленяет грозного царя.У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
n=len(s)
print(n)
count=0
flag=0
Dictionary = dict()
print (s,"\n")
print ('         i     xi       pi         qi        Ii       li       ci')
for i in range(n):
    for j in range(0, i, 1):
        if (s[j] == s[i]):
            flag = 1
    for j in range(i, n, 1):
        if (s[i] == s[j])&(flag==0):
            count = count + 1
    if (count!=0):
        p = count / n
        Dictionary.update({s[i]:p})
    count = 0
    flag = 0
sorted_dictionary = {}
sorted_keys = sorted(Dictionary, key=Dictionary.get, reverse=True)
for i in sorted_keys:
    sorted_dictionary[i] = Dictionary[i]
count_c=1
q=[0]*n
lh=0
for name,val in sorted_dictionary.items():
    q[count_c] = q[count_c - 1] + val
    ci=''
    znam=q[count_c-1]
    for i in range(0, 10, 1):
        ci=ci+str((int(znam*2)))
        znam, cisl=math.modf(znam*2)
    Ii = '0.' + ci
    ci=ci[:(int((-math.log2(val)))+1)]
    print('%10d' % (count_c), '%5s' %name, '%10.3f' %val,'%10.3f'%q[count_c-1], '%10.7s' %Ii, '%5d' %(int((-math.log2(val)))+1),'%10s' %ci)
    lh=lh+(int(round((-math.log2(val))))*val)
    count_c+=1
print('l=%.3f' % lh)
print('R=%.3f' % (lh / 1))


Dictionary1 = dict()
print ("\n")
print ('         i     xi       pi         qi        Ii       li       ci')
for i in range(n-1):
    for j in range(0, i-1, 1):
        if (s[j] == s[i])&(s[j+1] == s[i+1]):
            flag = 1
    for j in range(i, n-1, 1):
        if (s[i] == s[j])&(flag==0)&(s[j+1] == s[i+1]):
            count = count + 1
    if (count!=0):
        s1=s[i]+s[i+1]
        p = count / (n-1)
        Dictionary1.update({s1: p})
    count = 0
    flag = 0
sorted_dictionary = {}
sorted_keys = sorted(Dictionary1, key=Dictionary1.get, reverse=True)
for i in sorted_keys:
    sorted_dictionary[i] = Dictionary1[i]
count_c=1
q=[0]*n
lh=0
for name,val in sorted_dictionary.items():
    q[count_c] = q[count_c - 1] + val
    ci=''
    znam=q[count_c-1]
    for i in range(0, 10, 1):
        ci=ci+str((int(znam*2)))
        znam, chisl=math.modf(znam*2)
    Ii = '0.' + ci
    ci=ci[:(int((-math.log2(val)))+1)]
    print('%10d' % (count_c), '%5s' %name, '%10.3f' %val,'%10.3f'%q[count_c-1], '%10.7s' %Ii, '%5d' %(int((-math.log2(val)))+1),'%10s' %ci)
    lh=lh+(int(round((-math.log2(val))))*val)
    count_c+=1
print('l=%.3f' % lh)
print('R=%.3f' % (lh / 2))

Dictionary2 = dict()
print ("\n")
print ('         i     xi       pi         qi        Ii       li       ci')
for i in range(n-2):
    for j in range(0, i-2, 1):
        if (s[j] == s[i])&(s[j+1] == s[i+1])&(s[j+2] == s[i+2]):
            flag = 1
    for j in range(i, n-2, 1):
        if (s[i] == s[j])&(flag==0)&(s[j+1] == s[i+1])&(s[j+2] == s[i+2]):
            count = count + 1
    if (count!=0):
        s1 = s[i] + s[i + 1] +s[i+2]
        p = count / (n - 2)
        Dictionary2.update({s1: p})
    count = 0
    flag = 0
sorted_dictionary = {}
sorted_keys = sorted(Dictionary2, key=Dictionary2.get, reverse=True)
for i in sorted_keys:
    sorted_dictionary[i] = Dictionary2[i]
count_c=1
q=[0]*n
lh=0
for name,val in sorted_dictionary.items():
    q[count_c] = q[count_c - 1] + val
    ci=''
    znam=q[count_c-1]
    for i in range(0, 10, 1):
        ci=ci+str((int(znam*2)))
        znam, chisl=math.modf(znam*2)
    Ii = '0.' + ci
    ci=ci[:(int((-math.log2(val)))+1)]
    print('%10d' % (count_c), '%5s' %name, '%10.3f' %val,'%10.3f'%q[count_c-1], '%10.7s' %Ii, '%5d' %(int((-math.log2(val)))+1),'%10s' %ci)
    lh=lh+(int(round((-math.log2(val))))*val)
    count_c+=1
print('l=%.3f' % lh)
print('R=%.3f' % (lh / 3))










