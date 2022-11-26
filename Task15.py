import random

b=random.randint(1,10)
a=[]

for i in range(0,b):
    c=random.randint(1,12)
    a.append(c)
print("Первый список: " + str(a))

b=random.randint(1,10)
y=[]
for i in range(0,b):
    c=random.randint(1,12)
    y.append(c)
print("Второй список: " + str(y))

#1.Сформировать третий список,содержащий элементы обоих списков
x=a+y
print("1.Третий список: " + str(x))

#2.Сформировать третий список,содержащий элементы обоих списков без повторений
x=a+y
z=[]
for i in x:
    if i not in z:
        z.append(i)
print("2.Третий список: " + str(z))

#3.Сформировать третий список,содержащий элементы общие для двух списков
w=[]
for i in a:
    if i in y:
        w.append(i)
if len(w)<1:
    print("3.Нет общих элементов")
else:
    print("3.Третий список: " + str(w))

#Сформировать третий список, содержащий только уникальные элементы каждого из списков
k=[]
for i in a:
    if i not in k:
        k.append(i)
n=[]
for i in y:
    if i not in n:
        n.append(i)
w=n+k
print("4.Третий список: " + str(w))

#Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
if min(a)!=max(a):
    h=[min(a), max(a)]
else:
    h=[min(a)]
if min(y)!=max(y):
    d=[min(y), max(y)]
else:
    d=[min(y)]
w=h+d
print("5.Третий список: " + str(w))