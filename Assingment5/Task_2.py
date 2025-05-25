l = []
for i in range(1, 11):
    l.append(i)
print("Original list", l)
l5 = l[0:5]
print("First 5 extracted elememts", l5)
lr = l5[::-1]
print("Reversed list is", lr)
