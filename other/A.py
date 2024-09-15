n = int(input())

a, b = [], []

for i in range(n):
    a_el, b_el = map(int, input().split())
    a.append(a_el)
    b.append(b_el)

a.sort()
b.sort()
# print(a, b)

cur = 0
maxx = 0
t = 0

i = j = 0

while i< n and j<n:
    if a[i] < b[j]:
        cur += 1
        if cur > maxx:
            maxx = cur
            t = a[i]
        i += 1
    else:
        cur -= 1
        j += 1
print(t)
