class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

class Huffman_Tree(object):
    def __init__(self, Dictionary):
        self.Dictionary_code=dict()
        self.List = [Node(name,val) for name, val in Dictionary.items()]
        while len(self.List) != 1:
            self.List.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.List[len(self.List)-1].value + self.List[len(self.List)-2].value))
            n.left = self.List.pop(-1)
            n.right = self.List.pop(-1)
            self.List.append(n)
        self.root = self.List[0]
        self.Buffer = list(range(10))

    def generate_code(self, tree, length):
        node = tree
        if (not node):
            return
        elif node.name:
            self.Dictionary_code.update({node.name: ''})
            for i in range(length):
                self.Dictionary_code[node.name]+=str(self.Buffer[i])
            return
        self.Buffer[length] = 0
        self.generate_code(node.left, length + 1)
        self.Buffer[length] = 1
        self.generate_code(node.right, length + 1)

    def show_code(self):
        self.generate_code(self.root, 0)
        return self.Dictionary_code

s = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
n=len(s)
print(n)
count=0
flag=0
Dictionary = dict()
print (s,"\n")
print ('         i          xi        ni       pi          ci          li')
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
tree = Huffman_Tree(Dictionary)
Dictionary_code=tree.show_code()
count_c=1
lh=0
for name,val in Dictionary_code.items():
    print('%10d' % count_c, '%10s' %name, '%10.0f' %(Dictionary[name]*n), '%10.3f' %Dictionary[name], '%10s' %val, '%10d' %len(val))
    count_c+=1
    lh=lh+(Dictionary[name]*len(val))
print('l=%.3f'%lh)
print('R=%.3f'%(lh/1))

Dictionary1=dict()
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
print('\n')
tree1 = Huffman_Tree(Dictionary1)
Dictionary_code1=tree1.show_code()
print ('         i         xi         ni        pi        ci            li')
count_c=1
lh=0
for name,val in Dictionary_code1.items():
    print('%10d' % count_c, '%10s' %name, '%10.0f' %(Dictionary1[name]*(n-1)), '%10.3f' %Dictionary1[name], '%10s' %val, '%10d' %len(val))
    count_c+=1
    lh = lh + (Dictionary1[name] * len(val))
print('l=%.3f' % lh)
print('R=%.3f' % (lh / 2))

Dictionary2=dict()
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
tree2 = Huffman_Tree(Dictionary2)
Dictionary_code2=tree2.show_code()
print('\n')
print ('         i         xi         ni        pi        ci            li')
count_c=1
lh=0
for name,val in Dictionary_code2.items():
    print('%10d' % count_c, '%10s' %name, '%10.0f' %(Dictionary2[name]*(n-2)), '%10.3f' %Dictionary2[name], '%10s' %val, '%10d' %len(val))
    count_c+=1
    lh = lh + (Dictionary2[name] * len(val))
print('l=%.3f' % lh)
print('R=%.3f' % (lh / 2))