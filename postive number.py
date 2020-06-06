l1=[]
n=int(input("enter the size of array"))
print("enter elements")
for i in range(n):
    l1.append(int(input()))
l2=[]   
for i in range(len(l1)):
    if(l1[i]>0):
        l2.append(l1[i])
    else:
        continue

print(l2)