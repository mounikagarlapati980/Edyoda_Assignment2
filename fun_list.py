size=int(input("Enter Size:"))
lst=[]
for i in range(size):
    value1=int(input("Enter value1"))
    value2=int(input("Enter value2"))
    lst.append((value1,value2))
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j][1]>lst[j+1][1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

