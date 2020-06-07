
#assigning elements to different lists
n=[1,2,3,4]
n1=[]
n.append(5)
print("append",n)
n.insert(0,0)
print("insert method",n)
n1.append(1)
n1.append(2)
print("appending elements to empty list ",n1)

#accessing elements from a tuple
n=(1,2,3,4,1)
print("no of 1 in the tuple",n.count(1))
print("retriving index of first occurance of 2",n.index(2))

#deleting ddifferent dictionary elements
dict1={"name":"hari","age":21,"email":"x@gmail.com"}
print(dict1)
del dict1["name"]
print("after deleting",dict1)


