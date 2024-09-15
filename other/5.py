
line = "Там королевич мимоходом пленяет грозного царя.У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
import math

a = len(line)
mas_sim = []
# mas1.append(line[0])
flag = 0
for i in range(a - 1):
    flag = 0
    for j in range(i):
        if line[i] == line[j]:
            flag = 1
    if flag == 0:
        mas_sim.append(line[i])
a1 = len(mas_sim)
mas_count = []
for i in range(a1):
    mas_count.append(0)
    for j in range(a):
        if (mas_sim[i] == line[j]):
            mas_count[i] += 1

mas_pi = []
for i in range(a1):
    mas_pi.append(mas_count[i] / a)

for i in range(a1):
    for j in range(a1 - i - 1):
        if (mas_pi[j] < mas_pi[j + 1]):
            t1 = mas_pi[j]
            mas_pi[j] = mas_pi[j + 1]
            mas_pi[j + 1] = t1

            t2 = mas_sim[j]
            mas_sim[j] = mas_sim[j + 1]
            mas_sim[j + 1] = t2

            t3 = mas_count[j]
            mas_count[j] = mas_count[j + 1]
            mas_count[j + 1] = t3

mas_Ixi = []
length = 0
for i in range(a1):
    mas_Ixi.append(math.ceil((-math.log2(mas_pi[i]))))
    length += mas_Ixi[i] * mas_pi[i]
length = length

mas_k = []
for i in range(a1):
    if (i == 0):
        mas_k.append(0)
    else:
        mas_k.append(mas_k[i - 1] + mas_pi[i - 1])

mas_kod = []
for i in range(a1):
    q = mas_k[i]
    str_ = ''
    for i in range(mas_Ixi[i]):
        q *= 2
        if q // 1 == 1:
            str_ += '1'
            q -= 1
        else:
            str_ += '0'
    mas_kod.append(str_)

print("=========================================================")
for i in range(a1):
    print(i + 1, "   ", mas_sim[i], "    ", mas_count[i], "   ", "%.5f" % mas_pi[i], "    ", mas_Ixi[i], "   ",
          "%.8f" % mas_k[i], "   ", mas_kod[i])

# 2
a = len(line)
mas_sim2 = []
# mas1.append(line[0])
flag = 0
mas_for2 = []
for i in range(a - 1):
    mas_for2.append(line[i] + line[i + 1])
aa = len(mas_for2)
for i in range(a - 1):
    flag = 0
    for j in range(i):
        if mas_for2[i] == mas_for2[j]:
            flag = 1
    if flag == 0:
        mas_sim2.append(mas_for2[i])
a2 = len(mas_sim2)
mas_count2 = []
for i in range(a2):
    mas_count2.append(0)
    for j in range(aa):
        if (mas_sim2[i] == mas_for2[j]):
            mas_count2[i] += 1

mas_pi2 = []
for i in range(a2):
    mas_pi2.append(mas_count2[i] / aa)

for i in range(a2):
    for j in range(a2 - i - 1):
        if (mas_pi2[j] < mas_pi2[j + 1]):
            t1 = mas_pi2[j]
            mas_pi2[j] = mas_pi2[j + 1]
            mas_pi2[j + 1] = t1

            t2 = mas_sim2[j]
            mas_sim2[j] = mas_sim2[j + 1]
            mas_sim2[j + 1] = t2

            t3 = mas_count2[j]
            mas_count2[j] = mas_count2[j + 1]
            mas_count2[j + 1] = t3

mas_Ixi2 = []
length2 = 0
for i in range(a2):
    mas_Ixi2.append(math.ceil((-math.log2(mas_pi2[i]))))
    length2 += mas_Ixi2[i] * mas_pi2[i]

mas_k2 = []
for i in range(a2):
    if (i == 0):
        mas_k2.append(0)
    else:
        mas_k2.append(mas_k2[i - 1] + mas_pi2[i - 1])

mas_kod2 = []
for i in range(a2):
    q = mas_k2[i]
    str_ = ''
    for i in range(mas_Ixi2[i]):
        q *= 2
        if q // 1 == 1:
            str_ += '1'
            q -= 1
        else:
            str_ += '0'
    mas_kod2.append(str_)

print("=========================================================")
for i in range(a2):
    print(i + 1, "   ", mas_sim2[i], "   ", mas_count2[i], "    ", "%.5f" % mas_pi2[i], "    ", mas_Ixi2[i], "   ",
          "%.8f" % mas_k2[i], "    ", mas_kod2[i])

# 3
a = len(line)
mas_sim3 = []
# mas1.append(line[0])
flag = 0
mas_for3 = []
for i in range(a - 2):
    mas_for3.append(line[i] + line[i + 1] + line[i + 2])
aaa = len(mas_for3)
for i in range(aaa - 1):
    flag = 0
    for j in range(i):
        if mas_for3[i] == mas_for3[j]:
            flag = 1
    if flag == 0:
        mas_sim3.append(mas_for3[i])
a3 = len(mas_sim3)
mas_count3 = []
for i in range(a3):
    mas_count3.append(0)
    for j in range(aaa):
        if (mas_sim3[i] == mas_for3[j]):
            mas_count3[i] += 1

mas_pi3 = []
for i in range(a3):
    mas_pi3.append(mas_count3[i] / aaa)

for i in range(a3):
    for j in range(a3 - i - 1):
        if (mas_pi3[j] < mas_pi3[j + 1]):
            t1 = mas_pi3[j]
            mas_pi3[j] = mas_pi3[j + 1]
            mas_pi3[j + 1] = t1

            t2 = mas_sim3[j]
            mas_sim3[j] = mas_sim3[j + 1]
            mas_sim3[j + 1] = t2

            t3 = mas_count3[j]
            mas_count3[j] = mas_count3[j + 1]
            mas_count3[j + 1] = t3

mas_Ixi3 = []
length3 = 0
for i in range(a3):
    mas_Ixi3.append(math.ceil((-math.log2(mas_pi3[i]))))
    length3 += mas_Ixi3[i] * mas_pi3[i]

mas_k3 = []
for i in range(a3):
    if (i == 0):
        mas_k3.append(0)
    else:
        mas_k3.append(mas_k3[i - 1] + mas_pi3[i - 1])

mas_kod3 = []
for i in range(a3):
    q = mas_k3[i]
    str_ = ''
    for i in range(mas_Ixi3[i]):
        q *= 2
        if q // 1 == 1:
            str_ += '1'
            q -= 1
        else:
            str_ += '0'
    mas_kod3.append(str_)

print("=========================================================")
for i in range(a3):
    print(i + 1, "   ", mas_sim3[i], "   ", mas_count3[i], "   ", "%.5f" % mas_pi3[i], "   ", mas_Ixi3[i], "   ",
          "%.8f" % mas_k3[i], "   ", mas_kod3[i])

print("Средняя длина для 1 символа:", "%.5f" % length)
print("Средняя длина для 2 символа:", "%.5f" % length2)
print("Средняя длина для 3 символа:", "%.5f" % length3)

print("Средняя скорость для 1 символа:", "%.5f" % length)
print("Средняя скорость для 2 символа:", "%.5f" % (length2 / 2))
print("Средняя скорость для 3 символа:", "%.5f" % (length3 / 3))