list = [1,4,8,2,1]
a = len(list)
for i in range(a):
    for j in range(i,a):
        if list[j]<list[i]:
            g = list[i]
            list[i] = list[j]
            list[j] = g
print(list)