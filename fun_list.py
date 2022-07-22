size=int(input("Enter Size:"))
lst=[]
for i in range(size):
    lst1=[]
    for j in range(2):
        value=int(input("Enter value"))
        lst1.append(value)
    t=tuple(lst1)
    lst.append(t)
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j][1]>lst[j+1][1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
