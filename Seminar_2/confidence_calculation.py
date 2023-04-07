import random
list = []
for i in range(0, 100):
    list.append(random.randint(1, 3))
print(list)
a = sum(list)/(len(list))    
print(a)
if a > 1.5 or a <= 2.5:
    a = 2
elif a <=1.5:
    a =1
else:
     a = 3
print(a)
